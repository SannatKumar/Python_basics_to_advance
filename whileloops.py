#lets work with while loop here

k = 2
while k <=256:
    print(k)
    k = k*2

# using the break in while statement

i = 1
while i < 80:
    print("No, it hasn't been half way.")
    if i == 50:
        print("For your surprise we break the loop in 50. Do you mind? ")
        break
    i += 1
#use of continue and this omits the condition before its use.
j = 0
while j < 10:
    j += 1
    if j == 5:
        continue
    print(j)
