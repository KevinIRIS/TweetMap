import json
from django.http import HttpResponse
from elasticsearch import Elasticsearch



domain = "search-ccnyutweetmap-a27vedwjsz5rus4g65yoovk2sy.us-east-1.es.amazonaws.com"
index = "tweet"


def get_geo(request, lat, long):
    es = Elasticsearch([{'host': domain, 'port': 80,'use_ssl': False}])
    data = es.search(index= index , body={ "query":
      { "bool" :
            { "must" : { "match_all" : {} },
              "filter" :
                  { "geo_distance" :
                        { "distance" : "1000km", "location" : str(lat) + "," + str(long) }
                    }
              }
        }
    })['hits']
    response = HttpResponse(json.dumps(data), content_type="application/json")
    return response

