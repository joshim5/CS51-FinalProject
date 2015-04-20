# Import statements

"""
Setup variables, initialize machine learning library, setup audio collecting, setup event handlers
"""
def initialize ():


"""
Called when a button is clicked that denotes the starting of recording
"""
def startRecording ():

"""
Setup a callback to endRecording that is called after a fixed amount (10 - 15 seconds) later
"""
def startRecording ():

"""
Called after a set amount of time (10 -15 seconds) has passed since the start of the recording
Stop recording and call extract audio, passing in the audio that was recorded
Do any cleanup associated with the recordings 
"""
def endRecording ():

"""
takes as an argument the classification of a sound not in the training set and outputs its classification to the screen
"""
def outputResult ():


"""Machine Learning Functions"""

"""Takes as input the audio that was recorded
Runs feature extraction on the audio using the Yaafe library
Returns an associative array containing the features and their respective values"""
def extractAudio ():


"""
Calls extract audio on each of the values in our training set
Maintains an array consisting of all of the returned values
"""
def extractTrainingData ():

"""
Takes as input the results from calling extractTrainingData
Using scikit-learn, trains a neural network using the extracted features
Outputs the results so that they can be stored in a variable or saved for later use in additional instances of the program
"""
def trainNeuralNetwork ():

"""
Takes as input the features extracted from the sounds not in our training set
Using the neural network that was previously trained, this functions runs the neural network with these features as input. 
The neural network will then return a classification, which this function will return
"""
def recognizeSound ():
