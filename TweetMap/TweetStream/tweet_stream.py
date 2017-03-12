from tweepy.streaming import StreamListener
from tweepy import  Stream
from tweepy import  OAuthHandler
from tweepy import API
from TweetMap.TweetStream.TweetConnection import TweetConnection

class tweet_stream():

    def __init__(self, auth, url):
        self.url = url
        self.auth = auth  # OAuthHandler(customerKey, customerSecret)
        self.filter = filter
        self.listener = TweetConnection()

    def createstream(self):
        self.stream = Stream(self.auth, self.listener)
        return self.stream

    def reconnect(self):
        self.stream = Stream(self.auth, self.listener)
        return self.stream

