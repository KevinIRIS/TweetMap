
__Author__ = 'Kai'

from tweepy.streaming import StreamListener
import json
from elasticsearch import Elasticsearch

maxTweets = 1000000

class TweetConnection (StreamListener):
    __raw_data = []

    def __init__(self):
        count = 0
        __domain = ""
        self.__es = Elasticsearch(hosts= [{'host': __domain, 'port': 80,'use_ssl': False}])
        __body = {"mappings": { "tweet":{ "properties": {"username": {"type": "string"}, "timestamp": {"type": "date"}, "location": {"type": "geo_point"}, "text": {"type": "string"} } } } }
        if self.__es.indices.exists(index="tweet") is False:
            self.__es.indices.create(index="tweet", ignore=400, body = __body)



    def on_data(self, __raw_data):
        global index
        if __raw_data is not None:
            __infocount = 0
            print(__raw_data)
            json_data = json.loads(__raw_data)
            if json_data.get("user") is not None and json_data.get("user").get("name") is not None:
                __name = json_data.get("user").get("name")
                print(__name, end = " ")
                __infocount = __infocount + 1
            if json_data.get("geo") is not None:
                __geo = json_data.get("geo").get("coordinates")
                __long = __geo[0]
                __lant = __geo[1];
                __infocount = __infocount + 1
            if json_data.get("text") is not None:
                __content = json_data.get("text")
                __infocount = __infocount + 1
            if json_data.get("timestamp_ms") is None:
                __time = json_data.get("timestamp_ms")
                __infocount = __infocount + 1

            if __infocount == 4: # all information we need
                index = index % maxTweets + 1
                dictionary = {"location": {"lat": __long, "lon": __lant}, "username": __name,"timestamp": __time, "text": __content}
                self.__es.index(index="tweet", doc_type='tweet', id=index, body=json.dumps(dictionary))
                __package = json.dumps(dictionary)







