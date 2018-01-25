from app import api

from status.resources import StatusListResource, TweetSinkResource

api.add_resource(StatusListResource, '/api/tweets')

api.add_resource(TweetSinkResource, '/api/tweet_filters')

