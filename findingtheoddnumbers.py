# This program find the odd numbers in the array#
'''this commented section can take user array input
array = list()
num = input("Enter how many elements you want:")
print ("Enter numbers in array:")
for i in range(int(num)):
    n = input("num :")
    array.append(int(n))'''
# This section finds the unique number in the given array wherever you put the 2 or check the test case
# the idea is to find the unique number in a given array where rest of the numbers are same.
'''
array = ([2,1,1,1,1,1,1,1])
array = ([1,1,1,1,1,1,1,2])
'''
array = ([1,1,2,1,1,1,1,1])
dist = len(array) -2
second_array = array.copy()
x =(array[0])
del array[0]
i = 1
while i <= dist:
    if x in array:
        array.remove(x)
        unique_value= array[0]
    else:
        unique_value = x
    i+=1
print(unique_value)