import pandas as pd

import pickle
import re


def removetrailingzero(x):
    '''
    Remove the trailing zero of a string of a float.
    '''

    split = x.split('.')
    if split[-1] == '0':
        x = split[0]

    return x


def formatpercent(x):
    '''
    Remove trailing zeroes from a list of float.
    The returned list is of floats
    '''

    x = [str(i) for i in x]
    x = [removetrailingzero(i) for i in x]

    return [removetrailingzero(i) for i in x]


# Import set of compositions
with open('compositions.pkl', 'rb') as outfile:
    comps = pickle.load(outfile)

# Convert the decimals to percentages
systems = {}
for key, value in comps.items():

    # Check if system is binary
    elements = key.split('-')
    if len(elements) != 2:
        continue

    decimals = []
    for item in value:
        item = re.findall('\d+\.\d+', item)

        if not item:
            continue

        item = float(item[0])
        decimals.append(item)

    percentages2 = [i*100 for i in decimals]
    percentages1 = [100-i for i in percentages2]

    percentages1 = formatpercent(percentages1)
    percentages2 = formatpercent(percentages2)

    element1, element2 = key.split('-')

    compositions = []
    for i, j in zip(percentages1, percentages2):

        ifloat = float(i)
        jfloat = float(j)
        zerofloat = float(0)

        if (ifloat > jfloat) & (jfloat != zerofloat):
            composition = elements[0]+i+elements[1]+j

        if (jfloat > ifloat) & (ifloat != zerofloat):
            composition = elements[1]+j+elements[0]+i

        if ifloat == zerofloat:
            composition = elements[1]+j

        if jfloat == zerofloat:
            composition = elements[0]+i

        compositions.append(composition)

    systems[key] = compositions

# The compositions regardless of the potential used:
compositions = []
for key, value in systems.items():
    for item in value:
        compositions.append(item)

compositions = list(set(compositions))
print(compositions)

systems = pd.DataFrame(systems)
print(systems)

