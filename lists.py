#Learning to work with list
fruitlist = ["apple", "cucumber", "Banana", "Mango", "pear"]
print(fruitlist)

#accessing lists(indexing starts with 0)

print(fruitlist[0])
print(fruitlist[1])
print(fruitlist[4])
print(fruitlist[2:4])# this is same as accessing characters from string

#replacing the item in the fruitlist

fruitlist[4] = "Grapes" # This change the 4th item(indexing with 0) here pear with grapes

print(fruitlist)

#using the loop in the list
for x in fruitlist:
    print(x)

#checking whether the item is presented in the list
if "cucumber" in fruitlist:
    print("Yes, Cucumber is in the list")

#with the fruit that is not in the list

if "avacado" in fruitlist:
    print("Yes avacado is in the fruitlist")
else:
    print("No avacado is not in the fruitlist")

#find out the length of the list
print(len(fruitlist))

#add new fruit to the list

fruitlist.append("Orange")# only takes one argument
print(fruitlist)



