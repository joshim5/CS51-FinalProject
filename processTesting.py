"""
Testing for the machine learning algorithms
"""

# Our machine learning algorithms
from svc import SVMLearning
from NeighborLearning import NeighborLearning
from RandomForestLearning import RandomForestLearning

# Split up into difference samples
from sklearn.cross_validation import train_test_split

# Read from the testing file
import json

# read data
with open("text.json") as json_file:
	json_data = json.load(json_file)

# format data
X = [x['value'] for x in json_data]
y = [y['instrument'] for y in json_data]

# Divide into training and testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)

# setup svm and test
print "******TESTING SVM******"
svm = SVMLearning(X_train, y_train)
svm.testReports(X_test, y_test)
svm.

# setup neighbor learning and test
print "******TESTING NEIGHBOR LEARNING******"
neighborL = NeighborLearning(X_train, y_train)
neighborL.testReports(X_test, y_test)

# setup random forest learning and test
print "******TESTING FOREST LEARNING******"
rLearning = RandomForestLearning(X_train, y_train)
rLearning.testReports(X_test, y_test)
