"""
Here, we describe the file
"""

# Basic functions for time and logging
from time import time
import logging

# Machine learning libraries
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.decomposition import PCA

"""
describe the class here
"""
class SuperLearning(object):
	"""
	Initializer
	Basic training data models should be prepared here.
	Therefore, it is very likely that this class will be inherited.

	Parameters:
		X_train: array of arrays of floats
			This is the data itself. An array of vectors enconding the sounds from the instruments.
		y_train: array of strings
			These are labels. 
	"""
	def __init__(self, X_train, y_train, PCA_option):
		self.X_train = X_train
		self.y_train = y_train
		self.PCA_option = PCA_option

		# Taking principal components of the training data
		if self.PCA_option:
			self.pca = PCA(n_components=13)
			self.pca.fit(X_train)
			self.X_train_pca = self.pca.transform(X_train)

		# Put the original vectors into the pca variable
		else:
			self.pca = None
			self.X_train_pca = X_train
