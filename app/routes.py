from app import rest_api
from .views import GeoencodingAPI

rest_api.add_resource(GeoencodingAPI, "/getAddressDetails/")
