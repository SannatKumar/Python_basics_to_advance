# here we will learn how to analysis sentiment based on pyhton polarity
#This is the natural language library
from textblob import TextBlob
# Now user pass the string

user_string = str(input("Enter your string to analyse the sentiment: \n"))
if user_string == '' or user_string.isdigit():
    print("Nothing or number has been entered. Please try again")
 
#implemeting the textblob function to use srting
my_string = TextBlob(user_string)

#checking the senitment value and processing it to get the positive integer
full_value = my_string.sentiment.polarity
short_value = (float("%.1f" % full_value) + 2.0) * 10
final_value =int(short_value)
#if else statement to give the result
if final_value <= 19:
    print("Sad or Negative")
elif final_value >19 and final_value <=21:
    print("Neutral")
else:
    print("Happy or Positive")








