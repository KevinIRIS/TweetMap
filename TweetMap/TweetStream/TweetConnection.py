
__Author__ = 'Kai'

from tweepy.streaming import StreamListener
from tweepy import  Stream
from tweepy import  OAuthHandler
from tweepy import API

class TweetConnection (StreamListener):
    __raw_data = []

    def __init__(self, auth, url,filter):
        self.url = url
        self.auth = auth  #OAuthHandler(customerKey, customerSecret)
        self.filter = filter
        self.stream = self.createstream()

    def createstream(self):
        stream = Stream(self.auth , self.url)
        stream.filter(filter)
        return stream

    def reconnect(self):
        stream = Stream(self.auth , self.url)
        stream.filter(filter)
        return stream

    def getAPI(self):
        return API(self.auth)


