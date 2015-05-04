# import statements
from svc import SVMLearning
from NeighborLearning import NeighborLearning
from RandomForestLearning import RandomForestLearning

# setup svm and test
svm = SVMLearning(X_train, y_train)
ans1 = svm.classify([test_vector1, test_vector2])
print ans1[0], ans1[1]

# setup neighbor learning and test
neighborL = NeighborLearning(X_train, y_train)
ans2 = neighborL.classify([test_vector1, test_vector2])
print ans2[0], ans2[1]

# setup random forest learning and test
rLearning = RandomForestLearning(X_train, y_train)
ans3 = rLearning.classify([test_vector1, test_vector2])
print ans3[0], ans3[1]