#!/usr/bin/python

import pickle
import numpy
numpy.random.seed(42)


### the words (features) and authors (labels), already largely processed
### these files should have been created from the previous (Lesson 10) mini-project.
words_file = "../text_learning/your_word_data.pkl" 
authors_file = "../text_learning/your_email_authors.pkl"
word_data = pickle.load( open(words_file, "r"))
authors = pickle.load( open(authors_file, "r") )



### test_size is the percentage of events assigned to the test set (remainder go into training)
### feature matrices changed to dense representations for compatibility with classifier
### functions in versions 0.15.2 and earlier
from sklearn import cross_validation
features_train, features_test, labels_train, labels_test = cross_validation.train_test_split(word_data, authors, test_size=0.1, random_state=42)

from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer(sublinear_tf=True, max_df=0.5,
                             stop_words='english')
features_train = vectorizer.fit_transform(features_train)
features_test  = vectorizer.transform(features_test).toarray()


### a classic way to overfit is to use a small number
### of data points and a large number of features
### train on only 150 events to put ourselves in this regime
features_train = features_train[:150].toarray()
labels_train   = labels_train[:150]



### your code goes here
print len(features_train)

from sklearn import tree
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features_train, labels_train)

print "Accuracy on train examples: ", clf.score(features_train, labels_train)
print "Accuracy on test examples: ", clf.score(features_test, labels_test)

feature_importances = clf.feature_importances_
most_importance_value = max(feature_importances)
most_importance_feature = numpy.argmax(feature_importances)

feature_names = vectorizer.get_feature_names()
signatures = []
for i in range(len(feature_importances)):
    if feature_importances[i] > 0.2:
        signatures.append(feature_names[i])


# if importance is more than 0.2, then we will consider it as signature
# which means it simply decides data's class
print "most importance value: ", most_importance_value
print "most importance feature index: ", most_importance_feature
print "number of signatures: ", len(signatures)
print "signatures: ", signatures