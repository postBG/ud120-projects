#!/usr/bin/python

""" 
    starter code for exploring the Enron dataset (emails + finances) 
    loads up the dataset (pickled dict of dicts)

    the dataset has the form
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person
    you should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))
m = len(enron_data) # size of data set
print m

peoples = enron_data.keys()
print peoples

n = len(enron_data[peoples[0]]) # number of features
print n

features = enron_data[peoples[0]].keys()
print features

cnt = 0 # number of poi
for i in range(m):
    if enron_data[peoples[i]]["poi"] == 1:
        cnt += 1
print cnt

print enron_data['PRENTICE JAMES']['total_stock_value']
print enron_data['COLWELL WESLEY']['from_this_person_to_poi']
print enron_data['SKILLING JEFFREY K']['exercised_stock_options']

print enron_data['LAY KENNETH L']['total_payments']
print enron_data['FASTOW ANDREW S']['total_payments']
print enron_data['SKILLING JEFFREY K']['total_payments']

have_salary = 0
have_email = 0
for x in enron_data.values():
    if x['email_address'] != 'NaN':
        have_email += 1
    if x['salary'] != 'NaN':
        have_salary += 1

print have_salary
print have_email

NaN_total_payments = 0
for x in enron_data.values():
    if x['total_payments'] == 'NaN':
        NaN_total_payments += 1

print NaN_total_payments
print (NaN_total_payments*100.0)/m

poi_NaN_total_payments = 0
for x in enron_data.values():
    if x['total_payments'] == 'NaN' and x['poi'] == 1:
        poi_NaN_total_payments += 1

print poi_NaN_total_payments
print (poi_NaN_total_payments*100.0)/m