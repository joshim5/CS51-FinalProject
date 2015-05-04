from svc import SVMLearning
from NeighborLearning import NeighborLearning
from RandomForestLearning import RandomForestLearning


from features import mfcc
from features import logfbank
import scipy.io.wavfile as wav
import os
import glob
import json

# Split up into difference samples
from sklearn.cross_validation import train_test_split

# Read from the testing file
import json

import pyaudio
import wave


#for our audio recording
CHUNK = 1024
FORMAT = pyaudio.paInt32
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 2
WAVE_OUTPUT_FILENAME = "output.wav"


class Interface():
    def __init__(self):
        # read data
        with open("text.json") as json_file:
            json_data = json.load(json_file)

        self.p = pyaudio.PyAudio()

        # format data
        self.X = [x['value'] for x in json_data]
        self.y = [y['instrument'] for y in json_data]

        # Divide into training and testing
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X, self.y, test_size=0.25)

        self.test_svm()
        self.test_neighbor()
        self.test_forest()

        #allow user to play a clip and then classify it
        self.classify_song()



    def test_svm(self):
        # setup svm and test
        print "******TESTING SVM******"
        self.svm = SVMLearning(self.X_train, self.y_train, True)
        self.svm.testReports(self.X_test, self.y_test)

    def test_neighbor(self):
        # setup neighbor learning and test
        print "******TESTING NEIGHBOR LEARNING******"
        self.neighborL = NeighborLearning(self.X_train, self.y_train)
        self.neighborL.testReports(self.X_test, self.y_test)

    def test_forest(self):
        # setup random forest learning and test
        print "******TESTING FOREST LEARNING******"
        self.rLearning = RandomForestLearning(self.X_train, self.y_train, True)
        self.rLearning.testReports(self.X_test, self.y_test)

    def read_data(self, filename):
        '''
        Takes a path to a file as input
        Returns the mfcc for that file
        '''

        (rate,sig) = wav.read(filename)
        mfcc_feat = mfcc(sig,rate)


        mfcc_feat = mfcc_feat.tolist()
        try: 
            mfcc_feat = mfcc_feat[300]
        except:
            raise RuntimeError('sample too short')

        return mfcc_feat

    def record(self):
        '''Audio recording code based very closely on the documentation'''
        '''https://people.csail.mit.edu/hubert/pyaudio/#docs'''

       
        stream = self.p.open(format=FORMAT,
        channels=CHANNELS,
        rate=RATE,
        input=True,
        frames_per_buffer=CHUNK)

        print("* recording")

        frames = []

        for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
            data = stream.read(CHUNK)
            frames.append(data)

        print("* done recording")

        stream.stop_stream()
        stream.close()
        self.p.terminate()

        wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(self.p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
        wf.close()

    

    def classify_song(self):

        x = raw_input("Press enter to record: ")

        #record for two seconds and save to output.wav
        self.record()
        
        #open the wav file and extract the mfccs
        ret = self.read_data("output.wav")


        #classify with out trained svm
        answer_string = self.svm.classify([ret])

        #classify with our nearest neighbors
        answer_string1 = self.neighborL.classify([ret], self.X_test)

        #classify with random forests
        answer_string2 = self.rLearning.classify([ret])


        #print results
        print "SVM:", answer_string[0]
        print "Neighbor:", answer_string1[0]
        print "Forest:", answer_string2[0]


inst = Interface()

