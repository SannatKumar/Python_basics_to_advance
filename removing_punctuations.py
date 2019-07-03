# Removing the symbols and punctuations as part of data cleaning

def string_cleaning(string):
    punctuations = '''!()-_[]{}:;'"\,<>.?/@#$%^&*~`'''
    processed_string = ""
    for char in string:
        if char not in punctuations:
            processed_string = processed_string+char
    print(processed_string)
  
string = input("Enter a string to clean it:\n")
string_cleaning(string)
