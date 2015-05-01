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


instruments = ["oboe", "trumpet", "flute", "frenchhorn"]

values = []

path = "/Users/erikgodard/Documents/Classes/Freshman-Spring/CS51/CS51-FinalProject/sounds/new/"

for x in instruments:
    currPath = path + x
    instrAvg = [0]*13
    for filename in glob.glob(os.path.join(currPath, '*.wav')):
        avg = [0]*13

        res = read(filename).tolist()
        try: 
            res = res[300]
        except:
            print "input not long enough"
        values.append({"instrument":x, "value": res})
        '''for row in res:
            for k,v in enumerate(row):
                avg[k] += v
        for k,v in enumerate(avg):
            avg[k] = avg[k]/len(res)
            instrAvg[k] += avg[k]
        values.append({"instrument":x, "value": avg})'''
    for k,v in enumerate(instrAvg):
        instrAvg[k] = instrAvg[k]/ len(glob.glob(os.path.join(currPath, '*.wav')))
    print x, instrAvg

json.dump(values, open("text1.json",'w'))


