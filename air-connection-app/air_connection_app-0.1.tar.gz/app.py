from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restful import reqparse
from sqlalchemy import and_
import os
import sys
import logging


# Init db
db = SQLAlchemy()

# Init ma
ma = Marshmallow()


# Flight Class/Model
class Flight(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    source = db.Column(db.String(150))
    destination = db.Column(db.String(150))
    flight_company = db.Column(db.String(150))
    flight_number = db.Column(db.Integer, unique=True)
    flight_time = db.Column(db.String(150))
    free_seats = db.Column(db.String(150))
    price = db.Column(db.String(150))

    def __init__(self,
                 # id,
                 source,
                 destination,
                 flight_company,
                 flight_number,
                 flight_time,
                 free_seats,
                 price):
        # self.id = id
        self.source = source
        self.destination = destination
        self.flight_company = flight_company
        self.flight_number = flight_number
        self.flight_time = flight_time
        self.free_seats = free_seats
        self.price = price


parser = reqparse.RequestParser()
parser.add_argument('source', type=str, location='json', required=True)
parser.add_argument('destination', type=str, location='json', required=True)
parser.add_argument('flight_company', type=str, location='json', required=True)
parser.add_argument('flight_number', type=str, location='json', required=True)
parser.add_argument('flight_time', type=str, location='json', required=True)
parser.add_argument('free_seats', type=str, location='json', required=True)
parser.add_argument('price', type=str, location='json', required=True)


# Flight Schema
class FlightSchema(ma.Schema):
    class Meta:
        fields = ('id',
                  'source',
                  'destination',
                  'flight_company',
                  'flight_number',
                  'flight_time',
                  'free_seats',
                  'price')


# Init schema
flight_schema = FlightSchema()
flights_schema = FlightSchema(many=True)


def create_app(env="*"):  # noqa: C901
    app = Flask(__name__)
    logging.basicConfig(filename='air-connection-app.log', level=logging.DEBUG, format="%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s")  # noqa: C901 E501
    basedir = os.path.abspath(os.path.dirname(__file__))
    if env == "testing":
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        app.config["TESTING"] = True
    elif env == "dev":
        db_username = os.getenv("MYSQL_DATABASE_USER", "default")
        db_password = os.getenv("MYSQL_DATABASE_PASSWORD", "default")
        db_server = os.getenv("MYSQL_DATABASE_SERVER", "default")
        db_name = os.getenv("MYSQL_DATABASE_NAME", "default")
        app.config["SQLALCHEMY_DATABASE_URI"] = f"mysql+mysqlconnector://{db_username}:{db_password}@{db_server}/{db_name}"  # noqa: C901 E501
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    elif env == "prod":
        app.config['DATABASE_URI'] = 'mysql:///'
    db.init_app(app)
    ma.init_app(app)
    db.create_all(app=app)

    # Get All Flights
    @app.route('/flight', methods=['GET'])
    def get_flights():
        all_flights = Flight.query.all()
        result = flights_schema.dump(all_flights)
        return jsonify(result), 200

    # Get Single Flight
    @app.route('/flight/<id>', methods=['GET'])
    def get_flight(id):
        flight = Flight.query.get(id)
        if flight is not None:
            return flight_schema.jsonify(flight), 200
        return jsonify("I don't have such Flight id, please try again !"), 404

    # Create a Flight
    @app.route('/flight', methods=['POST'])
    def add_flight():
        args = parser.parse_args()
        flight_number = args['flight_number']
        exists_flight_number = Flight.query.filter_by(flight_number=flight_number).first()
        if exists_flight_number:
            return jsonify("This flight number is already exists, please try again!"), 400
        new_flight = Flight(**args)
        db.session.add(new_flight)
        db.session.commit()
        return flight_schema.jsonify(new_flight), 200

    # Update a Flight
    @app.route('/flight/<int:id>', methods=['PUT'])
    def update_flight(id):
        flight = Flight.query.get(id)
        if flight is None:
            return jsonify("Error 404! There's no record in the table"), 404
        args = parser.parse_args()

        source = args['source']
        destination = args['destination']
        flight_company = args['flight_company']
        flight_number = args['flight_number']
        flight_time = args['flight_time']
        free_seats = args['free_seats']
        price = args['price']
        print(flight_number, flight.flight_number)

        if flight_number != flight.flight_number:
            return jsonify("You can't change flight number, please try again!"), 400

        flight.source = source
        flight.destination = destination
        flight.flight_company = flight_company
        # flight.flight_number = flight_number
        flight.flight_time = flight_time
        flight.free_seats = free_seats
        flight.price = price
        db.session.commit()

        return flight_schema.jsonify(flight), 201

    # Delete Flight
    @app.route('/flight/<id>', methods=['DELETE'])
    def delete_flight(id):
        flight = Flight.query.get(id)
        if flight is not None:
            db.session.delete(flight)
            db.session.commit()
            return flight_schema.jsonify(flight), 201
        return jsonify("I don't have such id to delete, please try again !"), 404

    # Search Flight
    @app.route('/flight/search')
    def search():
        c1 = request.args['c1']
        c2 = request.args['c2']
        search_flights = db.session.query(Flight).filter(and_(Flight.source == c1, Flight.destination == c2)).all()  # noqa: E501
        result = flights_schema.dump(search_flights)
        if len(result) == 0:
            return "I don't have such way, please try again !", 404
        return jsonify(result, "Searched way successfully !"), 201

    # health check status
    @app.route("/status", methods=['GET'])
    def health_check():
        return "My Application is running", 200

    return app


# Run on AWS Server
if __name__ == '__main__':
    args = sys.argv
    app = create_app(args[1])
    app.run(debug=True, host='0.0.0.0', port=5000)
    # app.run(debug=True)
