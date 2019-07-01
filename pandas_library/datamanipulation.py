import pandas as pd  #pandas imported as pd

from pandas import DataFrame, read_csv

import matplotlib.pyplot as plt

import sys  # determines python verison
import matplotlib  # determines matplot version

# %matplotlib inline

print("Python version" + sys.version)
print('Pandas version ' + pd.__version__)
print('Matplotlib version' + matplotlib.__version__)

# CREATE_DATA

names = ['Nepal', 'Finland', 'Thailand', 'Japan', 'Sweden', 'China', 'India']
population = [29300000, 5503000, 69040000, 126800000, 9995000, 1386000000, 1339000000]
capital = ['Kathmandu', 'Helsinki', 'Bangkok', 'Tokyo', 'Stockholm', 'Beijing', 'New Delhi']

# The zip function will merge it
CountryDataSet = list(zip(names, population, capital))

# print(CountryDataSet)

# creating a dataframe object as df
df = pd.DataFrame(data=CountryDataSet, columns=['Names', 'Populations', 'Capital'])
print(df)

# Exporting the dataframe to a csv file

df.to_csv('countrydata.csv', index=False, header=False)

# GET_DATA
# r means passing the string as it is(Raw string)
Location = r'C:\\Users\\Raj\Documents\\jupyter_panadas_library\\countrydata.csv'
# df = pd.read_csv(Location)
# print("Get_data\n", df)

# Setting the header to None so that data doesn't come into header position

# df = pd.read_csv(Location, header=None)
# print("After Header None\n", df)

# or try giving names to header
df = pd.read_csv(Location, names=['Country', 'Population', 'Capital'])
print(df)

# If we have to delete the file
'''
import os
os.remove(Location)
'''
# PREPARE DATA
# Now lets check the data types

print(df.dtypes)

print(df.Population.dtypes)
print(df.Country.dtypes)
print(df.Capital.dtypes)

# ANALYSE THE DATA
# sorting the data and printing the highest population data
# if the ascending arguments has value True then the result is minimum
Sorted = df.sort_values(['Population'], ascending=False)
print(Sorted.head(1))

# another method of sorting
# Below brings only the data not the whole row as above
print(df['Population'].max())


# PRESENT DATA

# Creating the graph

df['Population'].plot()

# Maximum Population Value

MaxPopulation = df['Population'].max()

# Country and Capital Name associated with max value

MaxName = df['Country'][df['Population'] == df['Population'].max()].values

Text = str(MaxPopulation) + " - " + MaxName

# Add text to the graph

plt.annotate(Text, xy=(1, MaxPopulation), xytext=(1, 4), xycoords=('axes fraction', 'data'), textcoords="offset points")
plt.show()

print("The most popular name")
print(Sorted.head(1))