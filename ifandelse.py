# Working with if elif and else

a = 22
b = 45
c = 66
d = 34

#simple if statement
if a > b:
    print("yes, it is.")

#simple if else

if a < b:
    print("Yes a is less than b")
else:
    print("No b is not smaller than a")

#simple if elif and else

if a > b:
    print(" a is greater than b")
elif b > c:
    print("b is greater than c")
elif d > c:
    print(" d is greater than c")
else:
    print("None of the above three conditions are true. Thank you")

# short hand if else

print("This is short hand ifelse") if a < b else print ("No the conditions doesn't meet to come here.")

#using and operator

if a < b and c > d:
    print("Sire, your conditions are met.")

#using or ooperator

if a > b or c > d:
    print(" Yes, or operator is successful. Thank you")
