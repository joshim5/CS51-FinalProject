# Superclass
from superlearning import SuperLearning

# PCA
import numpy as np
from sklearn.decomposition import PCA
from sklearn.decomposition import RandomizedPCA

# Machine Learning
from sklearn.grid_search import GridSearchCV
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.decomposition import PCA
from sklearn.svm import SVC
from sklearn.decomposition import RandomizedPCA

class SVMLearning(SuperLearning):
	"""
	Initializer
	Sets up the SVM based on given training data.	

	Parameters:
		X_train: array of arrays of floats
			X represents a set of data
			This is the data itself. An array of vectors enconding the sounds from the instruments.
		y_train: array of strings
			y represents a list of labels
			These are labels. 

	Returns:
		Newly created object
	"""
	def __init__(self, X_train, y_train, PCA_option = False):
		# Call the super class's initilaizer
		super(SVMLearning, self).__init__(X_train, y_train, PCA_option)	

		# Various parameters for use in grid search
		# Our choices are adopted from the standard ones 
		# given in scikit-learn documentation
		param_grid = {'C': [1e3, 5e3, 1e4, 5e4, 1e5],
   	          'gamma': [0.0001, 0.0005, 0.001, 0.005, 0.01, 0.1], }	

   	    # Setup the classifier
   		self.clf = GridSearchCV(SVC(kernel='rbf', class_weight='auto'), param_grid)
   		self.clf = self.clf.fit(self.X_train_pca, self.y_train)	

	"""
   	TestReports
   	This method prepares reports used in analysis.
   	In particular, it creates a
   		-  classification reports
   		-  confusion matrix	
   	Parameters:
		X_train: array of arrays of floats
			This is the data itself. An array of vectors enconding the sounds from the instruments.
		y_train: array of strings
			These are labels. 
		fileName: optional string
			Where the testReport should be saved.
			If no file is given, the report will print to the screen.	
	Returns:
		Nothing
   	"""
	def testReports(self, X_test, y_test, fileName = None):
		X_test_pca = None
   		# Prepare principal components of the test data
   		if self.PCA_option:
			X_test_pca = self.pca.transform(X_test)

		# Otherwise, put the original vectors into the pca variable
		else:
			X_test_pca = X_test

   		# Predict the labels
   		y_pred = self.clf.predict(X_test_pca)	

   		# Setup how the reports should look
   		target_names = ['Flute', 'Frenchhorn', 'Oboe', 'Trumpet']

   		# Create the reports
   		classification = classification_report(y_test, y_pred, target_names=target_names)
   		confusion = confusion_matrix(y_test, y_pred)

   		# If no fileName is given, print to screen
   		if fileName == None:
   			print(classification)
   			print(confusion)	

   		# Otherwise, write to the indicated file
   		else:
   			f = open(fileName, 'w')
   			f.write(classification)
   			f.write("\n")
   			f.write(confusion)
   			f.close()	
	"""
   	Classify
   	Classify the instrument of a single sound vector	
   	Parameters:
   		test_vectors: array of array of floats
   			This is an array of the sound vectors that will be classified	
   	Returns:
   		Array of strings encoding the result
   	"""	

   	def classify(self, test_vectors):
   		# Prepare a principal component of the test_vectors
   		X_test_pca = None
   		if self.PCA_option:
   			X_test_pca = self.pca.transform(test_vector)

		# Otherwise, put the original vectors into the pca variable
		else:
			X_test_pca = X_test

   		# Predict the labels
   		y_pred = self.clf.predict(X_test_pca)

   		return y_pred
