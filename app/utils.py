import StringIO
import csv

from flask import make_response
from app import app, mongo


def twitter_driver(result):
    """"
    Util function fetches statuses from twitter
    """
    tweet_payload = {
            'name': result.user.name,
            'screen_name': result.user.screen_name,
            'followers_count': result.user.followers_count,
            'retweet_count': result.retweet_count,
            'favorite_count': result.favorite_count,
            'created_at': result.created_at,
            'tweet_text': result.text,
            'geo_location': result.coordinates,
            'language': result.lang,
            }
    if result.coordinates:
        tweet_payload['geo_location'] = result.coordinates['coordinates']

    return sink_to_mongo(tweet_payload)

def sink_to_mongo(status):
    """
    Utils function sink stauses to mongoDB
    """
    with app.app_context():
        result = mongo.db.status.insert_one(status)
        return result.acknowledged

def write_to_csv(ls, fieldnames):
    si = StringIO.StringIO()
    cw = csv.DictWriter(si, fieldnames=fieldnames)

    cw.writeheader()
    for l in ls:
        cw.writerow(l)

    output = make_response(si.getvalue())
    output.headers["Content-Disposition"] = "attachment; filename=export.csv"
    output.headers["Content-type"] = "text/csv"
    return output

