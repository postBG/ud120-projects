#!/usr/bin/python 

""" 
    skeleton code for k-means clustering mini-project

"""




import pickle
import numpy
import matplotlib.pyplot as plt
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit




def Draw(pred, features, poi, mark_poi=False, name="image.png", f1_name="feature 1", f2_name="feature 2"):
    """ some plotting code designed to help you visualize your clusters """

    ### plot each cluster with a different color--add more colors for
    ### drawing more than 4 clusters
    colors = ["b", "c", "k", "m", "g"]
    for ii, pp in enumerate(pred):
        plt.scatter(features[ii][0], features[ii][1], color = colors[pred[ii]])

    ### if you like, place red stars over points that are POIs (just for funsies)
    if mark_poi:
        for ii, pp in enumerate(pred):
            if poi[ii]:
                plt.scatter(features[ii][0], features[ii][1], color="r", marker="*")
    plt.xlabel(f1_name)
    plt.ylabel(f2_name)
    plt.savefig(name)
    plt.show()



### load in the dict of dicts containing all the data on each person in the dataset
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
### there's an outlier--remove it! 
data_dict.pop("TOTAL", 0)

### the input features we want to use 
### can be any key in the person-level dictionary (salary, director_fees, etc.) 
feature_1 = "salary"
feature_2 = "exercised_stock_options"
feature_3 = "total_payments"
poi  = "poi"
features_list = [poi, feature_1, feature_2, feature_3]
data = featureFormat(data_dict, features_list )
poi, finance_features = targetFeatureSplit( data )


# Find range of exercised_stock_options
names = data_dict.keys()
exercised_stock_opt = featureFormat(data_dict, ['exercised_stock_options'])

min = exercised_stock_opt[0][0]
min_idx = 0
max = exercised_stock_opt[0][0]
max_idx = 0

print names

for idx in range(len(exercised_stock_opt)):
    tmp = exercised_stock_opt[idx][0]
    if tmp < min and tmp != 0 :
        min = tmp
        min_idx = idx
    if tmp > max and tmp != 0:
        max = tmp
        max_idx = idx

print names[max_idx]
print names[min_idx]
print max_idx
print min_idx
print exercised_stock_opt[max_idx][0]
print exercised_stock_opt[min_idx][0]

# Find range of salary
salary_list = featureFormat(data_dict, ['salary'])

salary_min = salary_list[0][0]
salary_min_idx = 0
salary_max = salary_list[0][0]
salary_max_idx = 0

for idx in range(len(salary_list)):
    tmp = salary_list[idx][0]
    if tmp < salary_min and tmp != 0 :
        salary_min = tmp
        salary_min_idx = idx
    if tmp > salary_max and tmp != 0:
        salary_max = tmp
        salary_max_idx = idx

print salary_list[salary_max_idx][0]
print salary_list[salary_min_idx][0]

### in the "clustering with 3 features" part of the mini-project,
### you'll want to change this line to 
### for f1, f2, _ in finance_features:
### (as it's currently written, line below assumes 2 features)
for f1, f2, f3 in finance_features:
    plt.scatter( f1, f2)
plt.show()



from sklearn.cluster import KMeans
#features_list = ["poi", feature_1, feature_2, feature_3]
features_list = ["poi", feature_1, feature_2]
data2 = featureFormat(data_dict, features_list )
poi, finance_features = targetFeatureSplit( data2 )
clf = KMeans(n_clusters=2)
pred = clf.fit_predict( finance_features )
Draw(pred, finance_features, poi, name="clusters_before_scaling.pdf", f1_name=feature_1, f2_name=feature_2)


### cluster here; create predictions of the cluster labels
### for the data and store them to a list called pred

try:
    Draw(pred, finance_features, poi, mark_poi=False, name="clusters.pdf", f1_name=feature_1, f2_name=feature_2)
except NameError:
    print "no predictions object named pred found, no clusters to plot"





