import time
import tweepy

class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        print status.text


def twitter_stream():

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(key, secret)

    api = tweepy.API(auth)
    return api

    mystreamlistener = MyStreamListener()
    myStream = tweepy.Stream(auth=api.auth, listener=mystreamlistener)

    return myStream


def main():

    myStream = twitter_stream()
    myStream.filter(track=['modi', 'USA'])
    time.sleep(5)
    myStream.disconnect()

    myStream.filter(track=['modi', 'USA', 'music', 'actor'])
    time.sleep(5)
    myStream.disconnect()

if __name__ == '__main__':
    main()

