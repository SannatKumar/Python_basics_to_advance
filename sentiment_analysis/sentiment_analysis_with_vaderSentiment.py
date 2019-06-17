# learning sentiment analysis with vaderSentiment

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyser = SentimentIntensityAnalyzer()

#creating a function

def sentiment_analyzer_scores(user_string):
    score = analyser.polarity_scores(user_string)
    #this loop removes negatives and decimal, and it brings the code to the int range of between 10 to 30
    for x in score:
        score[x] = int((float("%.1f" % score[x]) + 2.0) * 10)
    
    negative_score = score["neg"]
    neutral_score = score["neu"]
    positive_score = score["pos"]
    compound_score = score["compound"]
    print("Negative: ", negative_score)
    print("Neutral: ", neutral_score)
    print("Positive: ", positive_score)
    print("Compound: ", compound_score)
    print("Based on your Informtaion, The sentiment of the sentence is: \n")
    if compound_score <= 15:
        print("Sad or Negative")
    elif compound_score > 15 and compound_score <=25:
        print("Neutral")
    else:
        print("Happy or Positive")
    
user_string = str(input("Enter your string to analyse the sentiment: \n"))
if user_string == '' or user_string.isdigit():
    print("Nothing or number has been entered. Please try again")
    
sentiment_analyzer_scores(user_string)
