from app import api

from status.resources import StatusListResource

api.add_resource(StatusListResource, '/status')

