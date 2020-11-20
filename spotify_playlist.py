import tweepy
import ignrtis
from collections import Counter, OrderedDict
from operator import itemgetter

auth = tweepy.OAuthHandler(ignrtis.con_key, ignrtis.con_key_srt)
auth.set_access_token(ignrtis.acc_tkn, ignrtis.acc_tkn_srt)

api = tweepy.API(auth)
links=[]
def getrecent():
    for tweet in tweepy.Cursor(api.search,q="open.spotify.com/playlist",count=300,result_type="recent",tweet_mode="extended").items(300):
        
        urls= tweet.entities['urls']
        spotify=[d['expanded_url'] for d in urls if 'expanded_url' in d]
        links.extend(spotify)
        #print(tweet.full_text)
        # print(urls)
    tosent=dict(Counter(links))
    d = OrderedDict(sorted(tosent.items(), key=itemgetter(1),reverse=True))
    count=0
    outdict={}
    for i,j in d.items():
        if (i.find('spoti')!=-1):
            outdict[i]=j
            count+=1
        if(count==5):
            break
    return (outdict)

def gethots():
    for tweet in tweepy.Cursor(api.search,q="open.spotify.com/playlist",count=300,result_type="popular",tweet_mode="extended").items(300):
        
        urls= tweet.entities['urls']
        spotify=[d['expanded_url'] for d in urls if 'expanded_url' in d]
        links.extend(spotify)
        #print(tweet.full_text)
        # print(urls)
    tosent=dict(Counter(links))
    d = OrderedDict(sorted(tosent.items(), key=itemgetter(1),reverse=True))
    count=0
    outdict={}
    for i,j in d.items():
        if (i.find('spoti')!=-1):
            outdict[i]=j
            count+=1
        if(count==5):
            break
    return (outdict)
