from __future__ import print_function

from time import time
import logging
import matplotlib.pyplot as plt

from sklearn.cross_validation import train_test_split
from sklearn.datasets import fetch_lfw_people
from sklearn.grid_search import GridSearchCV
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.decomposition import RandomizedPCA
from sklearn.svm import SVC

# PCA
import numpy as np
from sklearn.decomposition import PCA


print(__doc__)

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')

# Erik+Mandela: Music analysis, returning PCAs

# X -> data
# y -> array with results
#X = [[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2], [-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]]
#y = [-1, -2, -3, 1, 2, 3, -1, -2, -3, 1, 2, 3]
X = np.array([[-5,-5], [-4,-4], [-3,-3], [-2,-2], [-1,-1], [0,0], [5,5], [4,4], [3,3], [2,2], [1,1]])
y = [-5,-4,-3,-2,-1,0,5,4,3,2,1]
pca = PCA(n_components=2)
pca.fit(X)

# divide the data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.7)

# Extract the following
X_train_pca = pca.transform(X_train)
X_test_pca = pca.transform(X_test)

# With this information, we can now continue with the machine learning

###############################################################################
# Train a SVM classification model

print("Fitting the classifier to the training set")
t0 = time()
# TODO: Determine params
param_grid = {'C': [1e3, 5e3, 1e4, 5e4, 1e5],
              'gamma': [0.0001, 0.0005, 0.001, 0.005, 0.01, 0.1], }

#TODO: is this an appropriate kernel?
clf = GridSearchCV(SVC(kernel='rbf', class_weight='auto'), param_grid)
clf = clf.fit(X_train_pca, y_train)
print("done in %0.3fs" % (time() - t0))
print("Best estimator found by grid search:")
print(clf.best_estimator_)


###############################################################################
# Quantitative evaluation of the model quality on the test set

print("Predicting people's names on the test set")
t0 = time()
y_pred = clf.predict(X_test_pca)
print("done in %0.3fs" % (time() - t0))

# Compare y_test (correct answers) to y_pred (what our SVM thinks is the answers)
#print(classification_report(y_test, y_pred, target_names=target_names))
#print(confusion_matrix(y_test, y_pred, labels=range(n_classes)))

# User interactions
y_pred = clf.predict([[0,1], [6,6], [3,3]])
y_test = [0,6,3]
print(classification_report(y_test, y_pred))

