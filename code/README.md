# CS51-FinalProject
Final project for CS51 by Joshua Meier, Elana Simon, Erik Godard, and Mandela Patrick

## Instructions for setup
First, install iPython Notebook, and related dependencies.

To continue working on the project, navigate to the root directory and run 

ipython notebook --port 9999

In Safari, select "project.ipynb"

## Dependencies
For the project to work, the following libraries must be installed: 

* scipy - http://www.scipy.org/
* numpy - http://www.numpy.org/
* matplotlib - http://matplotlib.org/
* pyaudio - https://people.csail.mit.edu/hubert/pyaudio/
* scikit-learn - http://scikit-learn.org/stable/
* SpeechRecognition - https://pypi.python.org/pypi/SpeechRecognition/

Note that (5) depends on (1), (2), and (3)

To run the feature extraction code, after installing the dependencies navigates to the project directory in terminal and type

    python example.py


To run the machine learning algorithms, run 

    python main.py

The three machine learning algorithms will be run, and you will see their output. The program will then prompt you to record a two second clip, which it will attempt to classify. 



That's it :)