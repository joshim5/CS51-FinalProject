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

instruments = ["oboe", "trumpet", "flute", "frenchhorn"]

values = []

path = "/Users/erikgodard/Documents/Classes/Freshman-Spring/CS51/CS51-FinalProject/newsounds/"

for x in instruments:
    currPath = path + x
    print x
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
            instrAvg[k] += avg[k]'''

json.dump(values, open("text2.json",'w'))


