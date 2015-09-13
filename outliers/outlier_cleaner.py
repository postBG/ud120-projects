#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        clean away the 10% of points that have the largest
        residual errors (different between the prediction
        and the actual net worth)

        return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error)
    """
    
    cleaned_data = []

    ### your code goes here
    error = predictions - net_worths
    sq_error = error * error

    not_outliears = sq_error.flatten().argsort()[:-10]
    for idx in not_outliears:
        cleaned_data.append((ages[idx], net_worths[idx], error[idx]))

    return cleaned_data

