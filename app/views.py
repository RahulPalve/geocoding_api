from flask import request, jsonify
from flask_restful import Resource
from marshmallow import Schema, fields, validate, ValidationError
from app import gmaps


class GeoencodingInputType(Schema):

    address = fields.String(required=True,)
    output_format = fields.Str(
        required=True, validate=validate.OneOf(["xml", "json"]))


class GeoencodingAPI(Resource):
    """
    Add info here
    """

    def post(self, **kwargs):
        try:
            data = GeoencodingInputType().load(request.json)
            geocode = gmaps.geocode(data["address"])
            geocode_obj = geocode[0] if len(geocode) > 0 else None

            if geocode_obj:
                lat = geocode_obj["geometry"]["location"]["lat"]
                lng = geocode_obj["geometry"]["location"]["lng"]


        except ValidationError as err:
            return jsonify({"Invalid Request Format": err.messages}), 400
