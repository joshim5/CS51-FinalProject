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
* Python Speech Features - https://github.com/jameslyons/python_speech_features

To install Python Speech Features, navigate the to directory of the project in terminal and type 

    git clone https://github.com/jameslyons/python_speech_features.git

Once this has completed, type 

    cd ./python_speech_features

Then type

    python setup.py install

Once this has finished installing, the feature extraction library should be successfully installed. 


To run the feature extraction code, after installing the dependencies navigates to the project directory in terminal and type

    python example.py


To run the machine learning algorithms, run 

    python main.py

The three machine learning algorithms will be run, and you will see their output. The program will then prompt you to record a two second clip, which it will attempt to classify. 



That's it :)