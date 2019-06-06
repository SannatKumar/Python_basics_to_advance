# Here how function works

# lets start with simple function

def name_print(name):
    print("Hello ", name, "This is your first simple function")

print("Hi, Please give us your name: ")
name = input()

name_print(name)

# The above function takes the string input from the user and pass it as a parameter to the function
# and the functioin does it work

# Now we can see how it works with several or default value

def dear_animal(animal = "Dog"):
    print("My dearest pet animal is: " + animal)

dear_animal("Cat")
dear_animal("Cow")
dear_animal()
dear_animal("Horse")
dear_animal("Hen")

# So in above function the idea is if you do not pass any parameter to the function then it takes the default parameter

# Now we can pass lists to the function

def list_function(country_list):
    for x in country_list:
        print(x)


country_list= list(("Norway", "Finland", "France", "Denmark", "Sweden")) # this create the list name constructed list

list_function(country_list)

# Again we can pass dictionaries to the function

def dict_function(language_dictionary):
    for x,y in language_dictionary.item():
        print("Type:", x)
        print("Value:", y)

language_dictionary = {
    "Type" : "Noun",
    "Location" : "England",
    "Uses" : "Communication"
}



