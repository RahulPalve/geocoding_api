from flask import request, jsonify
from flask_restful import Resource
from marshmallow import Schema, fields, validate, ValidationError
from app import gmaps, mongo
from app.utils import handle_output_format, clean_address


class GeoencodingInputType(Schema):

    address = fields.String(required=True,)
    output_format = fields.Str(
        required=True, validate=validate.OneOf(["xml", "json"]))


class GeoencodingAPI(Resource):
    """
    Geoencoding API, resolve latitude and longitude from adress
    """
    @handle_output_format
    def post(self, **kwargs):
        try:
            data = GeoencodingInputType().load(request.json)
            response = {"coordinates": {}, "address": data["address"]}

            geocode_obj = mongo.db.cached_geocodes.find_one(
                {"address": clean_address(data["address"])}
            )

            if geocode_obj:
                response["coordinates"]["lat"] = geocode_obj["lat"]
                response["coordinates"]["lng"] = geocode_obj["lng"]

            else:
                geocode_obj = gmaps.geocode(data["address"], region="in")
                response["coordinates"]["lat"] = geocode_obj[0]["geometry"]["location"]["lat"]
                response["coordinates"]["lng"] = geocode_obj[0]["geometry"]["location"]["lng"]

                mongo.db.cached_geocodes.insert_one(
                    {
                        "address": clean_address(data["address"]),
                        "lat": response["coordinates"]["lat"],
                        "lng": response["coordinates"]["lng"]
                    }
                )

            return response, 200

        except ValidationError as err:
            return {"Invalid Request Format": err.messages}, 400
