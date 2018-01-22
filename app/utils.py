import twitter

from app import app, mongo

api = twitter.Api(consumer_key=app.config['TWITTER_CONSUMER_KEY'],
        consumer_secret=app.config['TWITTER_CONSUMER_SECRET'],
        access_token_key=app.config['TWITTER_ACCESS_TOKEN_KEY'],
        access_token_secret=app.config['TWITTER_ACCESS_TOKEN_SECRET'])


def twitter_driver(q):
    """"
    Util function fetches statuses from twitter
    """
    results = api.GetSearch(raw_query="q={}&count=100".format(q))
    payload = []
    for result in results:
        tweet_payload = {
                'user': {
                    'name': result.user.name,
                    'screen_name': result.user.screen_name,
                    'followers_count': result.user.followers_count,
                    },
                'retweet_count': result.retweet_count,
                'favorite_count': result.favorite_count,
                'created_at': result.created_at,
                'tweet_text': result.text,
                'geo_location': result.geo,
                'language': result.lang,
                'mentions': [u.screen_name for u in result.user_mentions],
                'urls': [url.expanded_url for url in result.urls]
                }
        payload.append(tweet_payload)
    return sink_to_mongo(payload)

def sink_to_mongo(statuses):
    """
    Utils function sink stauses to mongoDB
    """
    with app.app_context():
        result = mongo.db.status.insert_many(statuses)
        return result.acknowledged

