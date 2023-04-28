from nltk.sentiment import SentimentIntensityAnalyzer
import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
import extract

# Create an instance of the SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()

comments = extract.fetch_comments("https://www.youtube.com/watch?v=ePL5YSe2kLw")

# Iterate through the rows of the DataFrame and apply sentiment analysis on each row
def scoring(df):
    new=[]
    for index, row in df.iterrows():
        # Extract the text from the "text" column of the current row
        text = row["comment"]
        # Apply the sentiment analysis method on the text and append the results to a list
        scores = sia.polarity_scores(text)
        new.append(scores)
        # Create a new DataFrame from the list of sentiment scores
    sentiment_score=pd.DataFrame(new)
    return sentiment_score

#for calculating an average count 
def counting(sentiment_score):
    countp=0
    countn=0
    countneu=0

    for i in sentiment_score.values:
        if i[0]>i[2]:
            countn=countn+1
        elif i[0]<i[2]:
            countp=countp+1
        else:
            countneu=countneu+1
    return countn,countp,countneu
    


#for making a graphical representation 
#y=[countp,countn,countneu]
#mylabels=["positive","negative","neutral"]
#plt.pie(y,labels=mylabels)
#plt.show()