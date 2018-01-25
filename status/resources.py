import json
from flask import request
from flask_restful import Resource

from status import twitter_stream as ts
from status.app_settings import FIELD_TYPECAST_FUNC_MAPPING
from status.models import TwitterStatus


class TweetSinkResource(Resource):
    def post(self):
        payload = request.get_json()
        q = payload['q']
        if not q:
            # TODO bad request
            return

        ts.add_filter(q)
        return {'success': True}

    def delete(self):
        payload = request.get_json()
        q = payload['q']
        if not q:
            return

        ts.delete_filter(q)
        return {'success': True}

    def get(self):
        return ts.list_filters()


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
        _format = params.pop('format', None)
        results = TwitterStatus.filter_tweets(**params)
        from app.utils import write_to_csv
        if _format == 'csv':
            fieldnames = FIELD_TYPECAST_FUNC_MAPPING.keys()
            return write_to_csv(results, fieldnames)
        else:
            return {
                    'error': False,
                    'remark': 'success',
                    'data': results
                }

