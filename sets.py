#Working with set in python
#note : sets appears in random order
myset = {"Guitar", "Drums", "Vocal", "programming"}
print(myset)

#using for loop with set

for x in myset:
    print(x)

#checking if item present in the set

if "Guitar" in myset:
    print("Yes, I am here")

#Also

print("Vocal" in myset)

#Once set is created items cannot be changed but added

myset.add("Bass")
print(myset)

#Multiple values can be added using update method

myset.update(["Violin", "Sarangi", "Electricguitar","Cooking", "Travelling"])
print(myset)

#length of the set
print(len(myset))

#removing items
myset.remove("Cooking")
print(myset)

#discaring the items using discard method is same as remove

myset.discard("Electricguitar")
print(myset)

#pop method is also used but it removes the last item so,
#as set are unordered we dont know which item is removed

#Now using clear method is also same as pop but it empties the set

emptyset = myset.copy()
print("This is empty set:", emptyset)
#delete method delete the whole set

del emptyset
#print(emptyset)#Gives undefined error


#constructing sets

constructedset = set(("building", "designing", "creating", "updating", "upgrading"))
print(constructedset)





