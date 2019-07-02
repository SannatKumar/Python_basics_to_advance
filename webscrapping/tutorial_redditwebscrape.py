import praw
from textblob import TextBlob 
import math

reddit = praw.Reddit(client_id ='CcjEZXsR0CiujQ',
                     client_secret = 'h6OipNV5vYEt9YqrL0Au8_MgZ7s',
                     user_agent = 'subSentiment')

with open('sb.txt') as f:

    
    for line in f:
        subreddit = reddit.subreddit(line.strip())

        day_start = 1510635601
        day_end = 1510721999

        sub_submissions = subreddit.submissions(day_start, day_end)

        sub_sentiment = 0
        num_comments = 0

        for submission in sub_submissions:
            if not submission.stickied:
                submission.comments.replace_more(limit = 0)
                for comment in submission.comments.list():
                    blob = TextBlob(comment.body)

                    comment_sentiment = blob.sentiment.polarity
                    sub_sentiment += comment_sentiment
                    num_comments += 1
        print('/r/' + str(subreddit.display_name))
        try:
            print("Ratio: " + str(math.floor(sub_sentiment/num_comments*100))+ '/n')
        except:
            print("no comment sentiment." +'/n')
            ZeroDivisionError

