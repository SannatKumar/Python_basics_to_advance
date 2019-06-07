#Here we work with objects and classes in python language

class ExampleClass:
    myval = 7

objexample = ExampleClass()
print(objexample.myval)

# Now here is the complex class with the use of built in __init__ function

class Country:
    def __init__(self, name, area, population):
        self.name = name
        self.area = area
        self.population = population
    def countryfunct(self):
        print("Hello")
        print("The country name is ", self.name)
        

record1 = Country("Nepal", 147000, 30000000)
print("The country area is", record1.area)
print("The country population is", record1.population)
record1.countryfunct()


#modify object properties

record1.area = 147181
print("The modified area of the country is ", record1.area )

#delete object properties

del record1.area
print("After deleting properties \n")
print(record1.age) # it gives attibute error 

# we can also simply delete the whole object by using

"""
del record1
"""




