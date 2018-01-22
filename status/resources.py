from flask import request
from flask_restful import Resource

from status.models import TwitterStatus


class StatusListResource(Resource):
    def get(self):
        """
        Filters stauses on params
        params
        :screen_name:
        :retweet_count:
        :favorite_count:
        :created_at:
        :tweet_text:
        :geo_location:
        :language:
        :mentions:
        :urls:
        """
        params = request.args.to_dict()
        result = TwitterStatus.filter_tweets(**params)
        return {
                'error': False,
                'remark': 'success',
                'data': result
                }
