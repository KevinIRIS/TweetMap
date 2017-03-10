
__Author__ = 'Kai'

from tweepy.streaming import StreamListener
import json

class TweetConnection (StreamListener):
    __raw_data = []
    count = 0
    def on_data(self, __raw_data):
        if __raw_data is not None:
            json_data = json.loads(__raw_data)






