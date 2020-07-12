import keys
import tweepy
from listener import TwitterListener
import matplotlib.pyplot as plotter

def main():
    auth = tweepy.OAuthHandler(keys.consumer_key, keys.consumer_secret)
    auth.set_access_token(keys.access_token, keys.access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
    sentiment_trump = {'Positive':0, 'Negative': 0, 'Neutral': 0}
    sentiment_biden = {'Positive':0, 'Negative': 0, 'Neutral': 0}
    trump = 'Trump'
    biden = 'Biden'
    #start listener
    runner1 = TwitterListener(api, sentiment_trump,trump)
    #start stream
    stream = tweepy.Stream(auth = api.auth, listener=runner1)
    #filter:
    stream.filter(track =[trump] , languages=['en'], is_async=False)  
    
    runner2 = TwitterListener(api, sentiment_biden,biden)
    stream2 = tweepy.Stream(auth = api.auth, listener=runner2)
    stream2.filter(track =[biden] , languages=['en'], is_async=False)  
    # print(sentiment)
    figureObject, axesObject = plotter.subplots(2)
    axesObject[0].set_title(trump)
    axesObject[0].pie(sentiment_trump.values(), labels = sentiment_trump.keys(), autopct='%1.2f', startangle=90,wedgeprops   = { 'linewidth' : 3,'edgecolor' : "orange" })
    axesObject[0].axis('equal')
    # figureObject2, axesObject2 = plotter.subplots()
    axesObject[1].set_title(biden)
    axesObject[1].pie(sentiment_biden.values(), labels = sentiment_biden.keys(), autopct='%1.2f', startangle=90,wedgeprops   = { 'linewidth' : 3, 'edgecolor' : "orange" })
    axesObject[1].axis('equal')

    # axesObject.show()
    # axesObject2.show()
    plotter.show()


if __name__ == '__main__':
    main()