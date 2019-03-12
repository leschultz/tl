'''
The data for experiments Tl
'''

from matplotlib import pyplot as pl

import pandas as pd

import os

path = './data/tl.xlsx'

data = pd.read_excel(path)  # Load Tl data
data = data[data.duplicated(keep=False)]  # Remove duplicates

y = data['PROPERTY: Tl (K)']

mainelements = []
for i in data['FORMULA']:
    mainelements.append(str(i)[:2])

data['main'] = mainelements
print(data)

fig, ax = pl.subplots()
ax.plot(
        data['main'],
        y,
        marker='.',
        linestyle='none',
        label=str(len(mainelements))+' compositions'
        )

ax.set_ylabel('T [K]')
ax.set_xlabel('Main Element')
ax.legend()
ax.grid()

pl.show()
