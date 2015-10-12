#!/usr/bin/python


"""
    starter code for the evaluation mini-project
    start by copying your trained/tested POI identifier from
    that you built in the validation mini-project

    the second step toward building your POI identifier!

    start by loading/formatting the data

"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)

### your code goes here 

from sklearn.cross_validation import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.3, random_state=42)

poi_in_test = 0
for i in labels_test:
    if i == 1.0:
        poi_in_test += 1

print "the number of POIs in test set: ", poi_in_test
print "the number of people in test set: ", len(labels_test)
#from sklearn import tree
#clf = tree.DecisionTreeClassifier()
#clf = clf.fit(features_train, labels_train)


