from dateutil.parser import parse

FIELD_TYPECAST_FUNC_MAPPING = {
        'retweet_count': int,
        'favorite_count': int,
        'followers_count': int,
        'created_at': parse,
        'screen_name': unicode,
        'name': unicode,
        'tweet_text': unicode,
        'geo_location': lambda x: map(float, x.split(',')),
        'language': unicode
        }

RANGE_SUPPORTED_FIELDS = ['retweet_count', 'favorite_count', 'followers_count',
        'created_at']

REGEX_SUPPORTED_FIELDS = ['name', 'tweet_text']

GEO_SUPPORTED_FIELDS = ['geo_location']
