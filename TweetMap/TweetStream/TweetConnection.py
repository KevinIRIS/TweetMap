
__Author__ = 'Kai'

from tweepy.streaming import StreamListener
import json
from elasticsearch import Elasticsearch

maxTweets = 1000000

class TweetConnection (StreamListener):
    __raw_data = []
    def __init__(self):
        self.index = 0
        __domain = "search-ccnyutweetmap-a27vedwjsz5rus4g65yoovk2sy.us-east-1.es.amazonaws.com"
        self.__es = Elasticsearch(hosts= [{'host': __domain, 'port': 80,'use_ssl': False}])
        __body = {"mappings": { "tweet":{ "properties": {"username": {"type": "string"}, "timestamp": {"type": "date"}, "location": {"type": "geo_point"}, "text": {"type": "string"} } } } }
        if self.__es.indices.exists(index="tweet") is True:
            self.__es.indices.create(index="tweet", ignore=400, body = __body)



    def on_data(self, __raw_data):
        if __raw_data is not None:
            __infocount = 0
            print(__raw_data)
            json_data = json.loads(__raw_data)
            if json_data.get("user") is not None and json_data.get("user").get("name") is not None:
                __name = json_data.get("user").get("name")
                #print(__name, end = " ")
                __infocount = __infocount + 1
            if json_data.get("coordinates") is not None :
                __geo = json_data.get("coordinates").get("coordinates")
                __long = __geo[0]
                __lant = __geo[1]
                __infocount = __infocount + 1
            elif json_data.get("place") is not None:
                __geo = json_data.get("place").get("bounding_box").get("coordinates")[0]
                __long = __geo[0][0]
                __lant = __geo[0][1]
                __infocount = __infocount + 1
            if json_data.get("text") is not None:
                __content = json_data.get("text")
                __infocount = __infocount + 1
            if json_data.get("timestamp_ms") is not None:
                __time = json_data.get("timestamp_ms")
                __infocount = __infocount + 1

            if __infocount == 4: # all information we need
                self.index = self.index % maxTweets + 1
                dictionary = {"location": {"lat": __lant, "lon": __long}, "username": __name,"timestamp": __time, "text": __content}
                #print(dictionary)
                self.__es.index(index="tweet", doc_type='tweet', id=self.index, body=json.dumps(dictionary))









