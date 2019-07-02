# Here we use function to check the palindrome

def isPalindrome(string):
    rev = string[::-1]
    if(rev == string):
        return True
    else:
        return False
  
string = input("Enter a string to check if its Palindrome:\n")
isPalindrome(string)

bool = isPalindrome(string)

if bool == 1:
    print("Yes it is")
else:
    print("No, it is not")
    