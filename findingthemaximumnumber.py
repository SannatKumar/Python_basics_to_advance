#finding the maximum number

L = ({2,3,4,1,7,3,8,98,100,23,45})

def find_max(L):
    maximum = 0
    for x in L:
        if x > maximum:
            maximum = x
    print(maximum)
find_max(L)
