from tweepy import  OAuthHandler
from TweetMap.TweetStream.TweetConnection import TweetConnection
from TweetMap.TweetStream.tweet_stream import tweet_stream


if __name__ == '__main__':
    __customerKey = ""
    __customerSecret = ""
    __accessToken = ""
    __accessSecret = ""
    autho = OAuthHandler(__customerKey, __customerSecret)
    autho.set_access_token(__accessToken, __accessSecret)
    url = "https://stream.twitter.com/1.1/statuses/sample.json"

    stream = tweet_stream(autho,url).createstream()
    stream.filter(locations=[-180,-90,180,90], stall_warnings = True, track = 'example.com/foobarbaz')


