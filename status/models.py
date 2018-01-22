from dateutil.parser import parse

from app import mongo
from status.app_settings import QUERY_INTEGERS_PARAMS, QUERY_DATE_PARAMS, USER_PARAMS

class TwitterStatus():
    def __init__(self):
        pass

    @classmethod
    def filter_tweets(self, **filters):
        """
        filter tweets
        """
        query = {}

        for filter_name, filter_value in filters.iteritems():
            if filter_value:
                # TODO make general logic
                if filter_name in QUERY_INTEGERS_PARAMS:
                    filter_value = int(filter_value)

                if filter_name.endswith('lt') or filter_name.endswith('gt'):
                    filter_name, operator = filter_name.rsplit('_', 1)
                    if filter_name in QUERY_INTEGERS_PARAMS:
                        filter_value = {'$' + operator: int(filter_value)}
                    if filter_name in QUERY_DATE_PARAMS:
                        filter_value = {'$' + operator: parse(filter_value)}

                if filter_name in USER_PARAMS:
                    if not query.get('user'):
                        query['user'] = {}
                    query['user'][filter_name] = filter_value
                else:
                    query[filter_name] = filter_value

        return list(mongo.db.status.find(query, {'_id': 0}))

