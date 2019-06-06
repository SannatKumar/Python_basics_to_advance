# use of for loops

ocean = ["pacific", "atlantic", "indian", "persian", "arctic" ]

for oceanname in ocean:
    print(oceanname)

for oceanname in ocean:
    if oceanname == "indian":
        print(oceanname)


#using the range function it ends before the range meaning 50 in the below case

for x in range(50):
    print(x+5)

# using start and ending range

for y in (2, 54):
    print(y)

# using the given increment rather than the default in range

for y in (2, 100, 3):
    print(y)

# using nested loops

i = ["Mr.", "Ms.", "Madam", "Sir"]
j = ["Black", "White", "Red", "Green"]

for x in i:
    for y in j:
        print(x,y)
        