import tweepy
import ignrtis
from collections import Counter

auth = tweepy.OAuthHandler(ignrtis.con_key, ignrtis.con_key_srt)
auth.set_access_token(ignrtis.acc_tkn, ignrtis.acc_tkn_srt)

api = tweepy.API(auth)
links=[]
def getrecent():
    for tweet in tweepy.Cursor(api.search,q="soundcloud.app.goo.gl",count=100,result_type="recent",tweet_mode="extended").items(100):
        # print(tweet)
        urls= tweet.entities['urls']
        spotify=[d['expanded_url'] for d in urls if 'expanded_url' in d]
        links.extend(spotify)
        #print(tweet.full_text)
        # print(urls)
    return (dict(Counter(links)))

def gethots():
    for tweet in tweepy.Cursor(api.search,q="soundcloud.app.goo.gl",count=100,result_type="popular",tweet_mode="extended").items(100):
        # print(tweet)
        urls= tweet.entities['urls']
        spotify=[d['expanded_url'] for d in urls if 'expanded_url' in d]
        links.extend(spotify)
        #print(tweet.full_text)
        # print(urls)
    return (dict(Counter(links)))


