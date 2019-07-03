# Here we count prime numbers until the given numbers
print("Enter your Number: ")
x = int(input())
count = 0
for i in range(2,x):
    if i > 1:
        for j in range(2,i):
            if(i%j)==0:
                break
        else:
            count+=1
        
print(count)