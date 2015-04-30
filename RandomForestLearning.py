# Superclass
from superlearning import SuperLearning

class RandomForestLearning(SuperLearning):
	"""
	Initializer
	Sets up the Random Forest based on given training data.

	Parameters:
		X_train: array of arrays of flaots
			X represents a set of data.
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
   		# Prepare principal components of the train data
   		X_test_pca = self.pca.transform(X_test)

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
