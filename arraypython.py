# Lets create arrays

my_array = ["nursery", "elementary", "junior", "high", "degree"]
print(my_array)
print(my_array[2])
print(len(my_array))

#lets work with numbers

mynumber_array = [1,2,3,4,5,6,7,8,9]
for x in mynumber_array:
    print(x)

mynumber_array.append(0)
print("After appending", mynumber_array)

#using pop method

mynumber_array.pop(5)
print("After pop", mynumber_array)

#using remove method to the specific value

mynumber_array.remove(4)
print("After remove method", mynumber_array)

#lets use sorting
my_array.sort()
print("After Sorting", my_array)

#lets use count method which provides the count of the specific item
total = my_array.count("nursery")
print(total)