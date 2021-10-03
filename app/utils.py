import simplexml
from functools import wraps
from flask import request, make_response


def handle_output_format(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        resp = f(*args, **kwargs)
        output_format = request.json.get("output_format")

        if output_format == "xml":
            headers = resp[2] if len(resp) == 3 else None
            response = make_response(
                simplexml.dumps({"root": resp[0]}), resp[1])
            response.headers.extend(headers or {})
            response.mimetype = "application/xml"
            return response

        else:
            return resp
    return decorated_function


def clean_address(address):
    address = ''.join(e for e in address if e.isalnum())
    return address.lower()
