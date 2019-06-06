# Working with dictionary

animaldictionary = {
    "Type": "pets",
    "Legs": "Four",
    "Ears": "2",
    "Location": "Home"
}

print(animaldictionary)

#Accessing individual item

print(animaldictionary["Ears"])

#Accessing the item by assigning to new variable

place = animaldictionary["Location"]
print(place) 

#Accessing item using get key

Organs = animaldictionary.get("Legs")
print(Organs)

#changing the value

animaldictionary["Location"] = "wild"
print(animaldictionary["Location"])
print("This is get method:", animaldictionary.get("Location"))

#looping through the dictionary for the variables

for variables in animaldictionary:
    print(variables)

#looping to get values using values function(values is a function)

for variables in animaldictionary.values():
    print(variables)

#looping to get both variables and values using items(items is a function)

for variables, worth in animaldictionary.items():
    print(variables,": ", worth)

#check if any model exists

if "Legs" in animaldictionary:
    print("Yes, I exist")

#print length of the dictionary

print(len(animaldictionary))

# Adding new models to the dictionary

animaldictionary["Tails"] = 1
print(animaldictionary)

#removing items using pop method
animaldictionary.pop("Legs")
print("After pop method", animaldictionary)

#popitem() method removes the last inserted item
#del removes the specified item

del animaldictionary["Ears"]
print("After use of delete", animaldictionary)

#copying the dictionary

copydictionary = dict(animaldictionary)
print("This is the copied one",copydictionary)

#clear empties the dictionary

copydictionary.clear()
print("After use of clear Method", copydictionary)

# deleting the entire dictionary

del copydictionary # Now its deleted

#another copying method

newcopying = dict(animaldictionary)
print("New Copied Dictionary: ", newcopying)

# constructor method

wordsdictionary = dict(type = "noun", language = "english", Area = "England")
print(wordsdictionary)




