import mysql.connector as mariadb
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyser = SentimentIntensityAnalyzer()

#lets open the demo file
data = [line.rstrip('\n') for line in open("dataset.txt", encoding="utf-8")]
for user_string in data:
    if user_string == '' or user_string.isdigit():
        print("Nothing or number has been entered. Please try again")
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
        print("Based on your Information, The sentiment of the sentence is: \n")
        if compound_score <= 17:
            results = "Sad or Negative"
        elif compound_score > 17 and compound_score <=21:
            results = "Neutral"
        else:
            results = "Happy or Positive"

        print(results)
        # '192.168.1.172'
        '''mariadb_connection = mariadb.connect(host='localhost',
                                            port=80,
                                            user='root',
                                            password="Rapassword",
                                            database="raspberry_pi_data"
                                            )
        cursor = mariadb_connection.cursor()

        sql = "INSERT INTO nltk_results (UserInput, Results) VALUES (%s, %s)"
        val = (user_string, results)
        cursor.execute(sql, val)
        mariadb_connection.commit()
        '''#creating a function


