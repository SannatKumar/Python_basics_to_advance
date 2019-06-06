# How to work with tuples
#tuples are unchangeable

ourtuple = ("one", "two", "three", "four", "five", "six", "seven")
print(ourtuple)

#accessing the value of tuples by index
print(ourtuple[0])

# looping through tuple

for x in ourtuple:
    print(x)


#lets check while loop
y = 0
while y < 5:
    print(ourtuple[y])
    y += 1

# use if else in tuples

if "two" in ourtuple:
    print("Hi, I am here")
else:
    print("Hi, I am not here")

#Getting the length of the tuple

print(len(ourtuple))

# constructing tuple

mytuple = tuple(("a", "b", "c", "d", "e"))
print(mytuple)