# First lets import all the necessary library

import pandas as pd
from numpy import random
import matplotlib.pyplot as plt
import sys # Determine the python version number
import matplotlib #Determine matplotlib version number

print('Python version' + sys.version)
print('Pandas version' + pd.__version__)
print('Matplotlib version ' + matplotlib.__version__)

# Assign few names to the list
names = ['Ashok', 'Sarala', 'Homa', 'Soma', 'Mika', 'John', 'Brian']

# This generates the random number from the lists
random.seed(500)
random_names = [names[random.randint(low = 0, high = len(names))] for i in range(1000)]
print(random_names[:10])

# lets do same for the birth

births = [random.randint(low=0, high=1000) for i in range(1000)]
print(births[:10])

# Merging the names with the births
BabyDataSet = list(zip(random_names, births))
print(BabyDataSet)

# Now lets create the DataFrame object to hold the list

df = pd.DataFrame(data = BabyDataSet, columns = ['Names', 'Births'])
print(df[:10])

# Now lets export the data to the txt file

df.to_csv('births1989.txt', index=False, header=False)

# Now locating the file

Location = r'C:\Users\Raj\PycharmProjects\numpy_learn\venv\births1989.txt'
df = pd.read_csv(Location)

# The info might show 999 data beacuse indexing starts from 0
print(df.info)

# Now lets check few databases from head and tail

print(df.head())

print(df.tail())

df = pd.read_csv(Location, names = ["Names", "Births"])

print(df)

# lets delete the file in need else lets comment it out for now
'''
import os
os.remove(Location)
'''

# this prints the unique names from the  list
# print(df['Names'].unique())

y = df['Names'].unique()
for x in y:
    print(x)

# Below describes the data and prints the unique values
print(df['Names'].describe())

# lets group the data so that it appears only once

aggr_name=df.groupby('Names')

df=aggr_name.sum()
print(df)

# ANALYZING THE DATA

Sorted=df.sort_values(['Births'], ascending=False)
print(Sorted.head(1))

# Using the max value and it just prints the value

print(df['Births'].max())

# PRESENTING DATA

df['Births'].plot.bar()

print("The most popular name")
print(df.sort_values(by='Births', ascending=False))
plt.show()






