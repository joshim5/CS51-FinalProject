from features import mfcc
from features import logfbank
import scipy.io.wavfile as wav
import os
import glob
import json


def read(filename):
    (rate,sig) = wav.read(filename)
    mfcc_feat = mfcc(sig,rate)
    fbank_feat = logfbank(sig,rate)
    return mfcc_feat


    #change this later!!!


instruments = ["Oboe", "Trumpet", "Flute", "FrenchHorn"]

values = []

path = "/Users/erikgodard/Documents/Classes/Freshman-Spring/CS51/CS51-FinalProject/sounds/"

for x in instruments:
    currPath = path + x
    instrAvg = [0]*13
    for filename in glob.glob(os.path.join(currPath, '*.wav')):
        avg = [0]*13

        res = read(filename)

        for row in res:
            for k,v in enumerate(row):
                avg[k] += v
        for k,v in enumerate(avg):
            avg[k] = avg[k]/len(res)
            instrAvg[k] += avg[k]
        values.append({"instrument":x, "value": avg})
    for k,v in enumerate(instrAvg):
        instrAvg[k] = instrAvg[k]/ len(glob.glob(os.path.join(currPath, '*.wav')))
    print x, instrAvg

print values

json.dump(values, open("text.json",'w'))


