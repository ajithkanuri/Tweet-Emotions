import tweepy
import preprocessor as p 
from textblob import TextBlob

class TwitterListener(tweepy.StreamListener):
    def __init__(self, api, sentiment_dict, word):
        self.api = api
        self.requests_max = 100
        self.sentiment_dict = sentiment_dict
        self.word = word
        self.count = 0
        p.set_options(p.OPT.URL, p.OPT.RESERVED) 
        super().__init__(api)  
    def on_status(self, status):
        try:
            tweet = status.extended_tweet.full_text
        except:
            tweet = status.text
        if tweet.startswith('RT'):
            return
        tweet = p.clean(tweet)
        
        #check to see if word is in tweet
        if self.word.lower() not in tweet.lower():
            return 
        #sentiment analysis 
        senti_blob = TextBlob(tweet)
        store = senti_blob.sentiment.polarity
        if store > 0:
            self.sentiment_dict['Positive'] +=1
        elif store == 0:
            self.sentiment_dict['Neutral'] +=1
        else:
            self.sentiment_dict['Negative'] +=1
            
        self.count+=1
        return self.count< self.requests_max
    