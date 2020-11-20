import tweepy
import ignrtis
from collections import Counter

auth = tweepy.OAuthHandler(ignrtis.con_key, ignrtis.con_key_srt)
auth.set_access_token(ignrtis.acc_tkn, ignrtis.acc_tkn_srt)

api = tweepy.API(auth)
links=[]
for tweet in tweepy.Cursor(api.search,q="open.spotify.com/artist",count=1000,result_type="recent",tweet_mode="extended").items(1000):
    
    urls= tweet.entities['urls']
    spotify=[d['expanded_url'] for d in urls if 'expanded_url' in d]
    links.extend(spotify)
    #print(tweet.full_text)
    # print(urls)
print (Counter(links))


# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text)

# status = api.get_status(id, tweet_mode="extended")
# try:
#     print(status.retweeted_status.full_text)
# except AttributeError:  # Not a Retweet
#     print(status.full_text)


#override tweepy.StreamListener to add logic to on_status
# class MyStreamListener(tweepy.StreamListener):

#     def on_status(self, status):
#         print(status.text)
# myStreamListener = MyStreamListener()
# myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)
# myStream.filter(track=[''])
