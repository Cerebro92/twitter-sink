from datetime import datetime
from dateutil.parser import parse

from app import mongo
from status.app_settings import (FIELD_TYPECAST_FUNC_MAPPING,
                            RANGE_SUPPORTED_FIELDS, REGEX_SUPPORTED_FIELDS,
                            GEO_SUPPORTED_FIELDS)

class TwitterStatus():
    def __init__(self):
        pass

    @classmethod
    def serialize(self, d):
        """
        serialize tweet
        """
        for k, v in d.iteritems():
            if isinstance(v, datetime):
                v = v.isoformat()
            if isinstance(v, unicode):
                v = v.encode("utf8")
            d[k] = v
        return d

    @classmethod
    def filter_tweets(self, **filters):
        """
        filter tweets
        """
        query = {}
        operator = None

        for fname, fvalue in filters.iteritems():

            if fname.endswith('_lt') or fname.endswith('_gt'):
                fname, operator = fname.rsplit('_', 1)

                if fname not in RANGE_SUPPORTED_FIELDS:
                    # TODO
                    raise Exception

            try:
                # type cast filter values
                _typecast_func = FIELD_TYPECAST_FUNC_MAPPING[fname]
                fvalue = _typecast_func(fvalue)
            except IndexError:
                # TODO Error
                return []

            if fname in REGEX_SUPPORTED_FIELDS:
                fvalue = {'$regex': fvalue, '$options': 'ix'}

            if fname in GEO_SUPPORTED_FIELDS:
                fvalue = {'$near': {'$geometry': {'type': 'Point',
                            'coordinates': fvalue}, '$maxDistance': 100}}

            if operator:
                fvalue = {'$' + operator: fvalue}

            query[fname] = fvalue


        tweets = list(mongo.db.status.find(query, {'_id': 0}))

        return map(self.serialize, tweets)

