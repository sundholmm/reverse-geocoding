from geopy.geocoders import Nominatim
from geopy.point import Point
from flask import Flask
from flask import request
from flask import json
from werkzeug.exceptions import HTTPException, UnprocessableEntity

app = Flask(__name__)


# Define custom error handler for returning
# the default errors as JSON instead of HTML
@app.errorhandler(HTTPException)
def handle_exception(e):
    response = e.get_response()
    response.data = json.dumps({
        "code": e.code,
        "name": e.name,
        "description": e.description,
    })
    response.content_type = "application/json"
    return response


# Get latitude and longitude from the corresponding request arguments,
# also require application name for geopy,
# raises HTTP status 422 if not provided,
# returns location as JSON
@app.route('/api/v1/reverse', methods=['GET'])
def reverse():
    if all(key in request.args for key in ('lat', 'lng', 'app_name')):
        lat = request.args.get('lat', type=float)
        lng = request.args.get('lng', type=float)
        app_name = request.args.get('app_name', type=str)
    else:
        raise UnprocessableEntity(
            "Either latitude, longitude or application name missing!")
    point = Point(lat, lng)
    geolocator = Nominatim(user_agent=app_name)
    location = geolocator.reverse(point)
    return location.raw
