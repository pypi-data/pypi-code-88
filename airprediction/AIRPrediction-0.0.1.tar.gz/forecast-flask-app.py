from flask import Flask, jsonify
from flask_restful import Api, Resource, reqparse, abort
import air_forecasting_service

app = Flask(__name__)
api = Api(app)

forecast_get_args = reqparse.RequestParser()

forecast_get_args.add_argument("pollutant", type=str, help="Need pollutant")

locations = {}


def abort_location_doesnt_exist(location):
    if location not in locations:
        abort(404, message="Location is not valid!")


class Forecast(Resource):
    def get(self, location):
        abort_location_doesnt_exist(location)
        # Need machine learning portion for this section
        afs = air_forecasting_service()
        predicted_forecast = afs.predict(location)
        data = {"forecast": predicted_forecast}
        return jsonify(data)

    # May remove later if needed
    def post(self, location):
        args = forecast_get_args.parse_args()
        locations[location] = args
        return locations[location], 201


api.add_resource(Forecast, "/forecast/<string:location>")

if __name__ == "__main__":
    app.run(debug=True)
