import time
import tweepy

from app import app

consumer_key = app.config['TWITTER_CONSUMER_KEY']
consumer_secret = app.config['TWITTER_CONSUMER_SECRET']
key=app.config['TWITTER_ACCESS_TOKEN_KEY']
secret=app.config['TWITTER_ACCESS_TOKEN_SECRET']


from app.utils import twitter_driver

class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        twitter_driver(status)

class TwitterStream(object):

    # The Singleon 
    # inspired from
    # http://python-3-patterns-idioms-test.readthedocs.io/en/latest/Singleton.html
    __instance = None
    def __new__(cls, filters=[]):
        if not TwitterStream.__instance:
            TwitterStream.__instance = object.__new__(cls)
            TwitterStream.__instance.stream = cls.get_stream()
            TwitterStream.__instance.filters = filters

        return TwitterStream.__instance

    @classmethod
    def get_stream(self):
        """Create Twitter stream"""

        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(key, secret)

        api = tweepy.API(auth)

        mystreamlistener = MyStreamListener()
        myStream = tweepy.Stream(auth=api.auth, listener=mystreamlistener)

        return myStream

    def add_filter(self, q):
        # disconnect and reconnect again with refershed filters
        if q in self.filters:
            raise Exception

        self.filters.append(q)
        self.restart()

    def delete_filter(self, q):
        if q not in self.filters:
            raise Exception

        self.filters.remove(q)
        self.restart()

    def list_filters(self):
        return self.filters

    def restart(self):
        if self.stream.running:
            self.stream.disconnect()

        self.stream.filter(track=self.filters, async=True)

