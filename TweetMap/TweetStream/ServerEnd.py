from tweepy import  OAuthHandler
from TweetMap.TweetStream.TweetConnection import TweetConnection


if __name__ == '__main__':
    __customerKey = "YAaiofpQoANsCytPu9ZOk8a5n"
    __customerSecret = "wMAOre20wWzxzVLaPoXtX1DZfe7UzQSNgTmwTVqaVs6qxdQuWf"
    __accessToken = "824322521948442625-3VevdrekP2EKBLLZGKutLGvN1ZOcSqn"
    __accessSecret = "q4SyYEjYQOLNKoFCyd6WFnNnyxG0srilGb2NqIcxOjTxq"
    autho = OAuthHandler(__customerKey, __customerSecret)
    autho.set_access_token(__accessToken, __accessSecret)
    url = "https://stream.twitter.com/1.1/statuses/sample.json"

    connection = TweetConnection(autho,url,"")

    # test
    api = connection.getAPI()

