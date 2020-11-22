import tweepy
import ignrtis
import pickle #for storing dictionary
import threading
import concurrent.futures
from collections import Counter, OrderedDict
from operator import itemgetter

auth = tweepy.OAuthHandler(ignrtis.con_key, ignrtis.con_key_srt)
auth.set_access_token(ignrtis.acc_tkn, ignrtis.acc_tkn_srt)

api = tweepy.API(auth,wait_on_rate_limit=True)
links=[]
toSent=None

def getToSent():
    for tweet in tweepy.Cursor(api.search,q="soundcloud.app.goo.gl",count=100,result_type="recent").items(1000):
        # print(tweet)
        urls= tweet.entities['urls']
        spotify=[d['expanded_url'] for d in urls if 'expanded_url' in d]
        links.extend(spotify)
        #print(tweet.full_text)
        # print(urls)
    tosent=dict(Counter(links))
    with open("sample1.txt", "wb") as myFile:
        pickle.dump(tosent)
    tosent=getToSent()
    d = OrderedDict(sorted(tosent.items(), key=itemgetter(1),reverse=True))
    count=0
    outdict={}
    for i,j in d.items():
        if (i.find('soundcloud')!=-1):
            outdict[i]=j
            count+=1
        if(count==6):
            break
    return (outdict)

def getToSentCache():
    with open("sample1.txt", "rb") as myFile:
        tosent=pickle.load(myFile)
    tosent=getToSent()
    d = OrderedDict(sorted(tosent.items(), key=itemgetter(1),reverse=True))
    count=0
    outdict={}
    for i,j in d.items():
        if (i.find('soundcloud')!=-1):
            outdict[i]=j
            count+=1
        if(count==6):
            break
    return (outdict)

def getrecent():
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future = executor.submit(getToSentCache)
        return_value = future.result()
        yield return_value
    
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future = executor.submit(getToSent)
        return_value = future.result()
        return return_value

def gethots():
    for tweet in tweepy.Cursor(api.search,q="soundcloud.app.goo.gl",count=100,result_type="mixed").items(1000):
        # print(tweet)
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
        if (i.find('soundcloud')!=-1):
            outdict[i]=j
            count+=1
        if(count==6):
            break
    return (outdict)


