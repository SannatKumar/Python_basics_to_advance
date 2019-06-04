# Another list
countrylist = ["Nepal", "India", "Japan", "Finland", "China"]
countrylist[4] = "Switzerland" # this replaces the index value of the list
print(countrylist)

# Adding to the list

countrylist.append("Germany") # This adds the country to the list
print(countrylist)

#Inserting item to any place as per index

countrylist.insert(4, "Sweden")
print(countrylist)

#removing something from the list

#lets make a copy of the list

ourcountrylist = countrylist.copy() # this sfunction makes the copy of the list
print("This is our country list: ", ourcountrylist)

#removing the items from the list

ourcountrylist.remove("Germany")
print(ourcountrylist)
 
#using pop to remove the selective index

ourcountrylist.pop(3) # this removes the 4th country name from the list
print(ourcountrylist)
ourcountrylist.pop()
print("Without index", ourcountrylist) # it removes the last value of the list

#del works somehow same as pop
nationlist = countrylist.copy()
print("This is our new nation list:", nationlist)
del nationlist[3]
print("After use of del: ", nationlist) # It deletes the 4th value from the list

#deleting the list
del ourcountrylist



# using the clear method
anothercountrylist = countrylist.copy()
print("This is our new countrylist: ", anothercountrylist)

# using clear method
anothercountrylist.clear()
print("After use of clear", anothercountrylist)

#using the reverse method
othercountrylist = countrylist.copy()
print("After copying country list", othercountrylist)
othercountrylist.reverse()
print("Reverse list", othercountrylist)







