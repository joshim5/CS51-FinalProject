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

CHUNK = 1024
FORMAT = pyaudio.paInt32
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 1
WAVE_OUTPUT_FILENAME = "output.wav"






class Interface():
    def __init__(self):
        # read data
        with open("text1.json") as json_file:
            json_data = json.load(json_file)

        self.p = pyaudio.PyAudio()

        # format data
        self.X = [x['value'] for x in json_data]
        self.y = [y['instrument'] for y in json_data]

        # Divide into training and testing
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X, self.y, test_size=0.25)

    def test_svm(self):
        # setup svm and test
        print "******TESTING SVM******"
        svm = SVMLearning(self.X_train, self.y_train)
        svm.testReports(self.X_test, self.y_test)

    def test_neighbor(self):
        # setup neighbor learning and test
        print "******TESTING NEIGHBOR LEARNING******"
        neighborL = NeighborLearning(self.X_train, self.y_train)
        neighborL.testReports(self.X_test, self.y_test)

    def test_forest(self):
        # setup random forest learning and test
        print "******TESTING FOREST LEARNING******"
        rLearning = RandomForestLearning(self.X_train, self.y_train)
        rLearning.testReports(self.X_test, self.y_test)

    def read_data(self, filename):
        avg = [0]*13

        (rate,sig) = wav.read(filename)
        mfcc_feat = mfcc(sig,rate)

        for row in mfcc_feat:
            for k,v in enumerate(row):
                avg[k] += v
        for k,v in enumerate(avg):
            avg[k] = avg[k]/len(mfcc_feat)

        return avg
    

    def classify_song(self):
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

        ret = self.read_data("output.wav")


        svm = SVMLearning(self.X_train, self.y_train, True)
        neighborL = NeighborLearning(self.X_train, self.y_train, True)
        rLearning = RandomForestLearning(self.X_train, self.y_train, True)



        answer_string = svm.classify([ret])
        answer_string1 = neighborL.classify([ret], self.X_test)
        answer_string2 = rLearning.classify([ret])
        print answer_string[0]
        print answer_string1[0]
        print answer_string2[0]


inst = Interface()
inst.test_svm()
inst.test_neighbor()
inst.test_forest()
inst.classify_song()
