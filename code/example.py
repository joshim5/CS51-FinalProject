from features import mfcc
from features import logfbank
import scipy.io.wavfile as wav
import os
import glob
import json


'''
Function that takes the path to a wav file and returns
the mfcc coefficients of that file
'''
def read(filename):
    (rate,sig) = wav.read(filename)
    mfcc_feat = mfcc(sig,rate)
    return mfcc_feat



instruments = ["oboe", "trumpet", "flute", "frenchhorn"]

#Array that will eventually contain all of our labelled data
values = []

#Get the directory the program is running from
currDir = os.path.dirname(os.path.realpath(__file__))

#we will be searching the sounds directory
path = currDir + "/sounds/"


#iterate over each instrument from which we are obtaining data
for x in instruments:
    #directory of the instruments sounds files
    currPath = path + x

    #for all files ending in .wav in the current directory
    for filename in glob.glob(os.path.join(currPath, '*.wav')):

        #call the read function and convert from numpy array to python array
        res = read(filename).tolist()
      
        #extract the first 300 rows on the matrix
        #don't do anything if the input sound file is not long enough
        try: 
            res = res[300]
        except:
            print "input not long enough"


        #add this labelled data to our values array
        values.append({"instrument":x, "value": res})

#dump the labelled data into a json file for later use
json.dump(values, open("data.json",'w'))


