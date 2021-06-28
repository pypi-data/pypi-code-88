from os import device_encoding
from flask import Flask
from flask_restful import Api, Resource, reqparse

from werkzeug.datastructures import auth_property

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
class TestToml(Resource):
    def post(self, *args):
        print(args)







api.add_resource(TestToml, '/auth_sep10')


if __name__ == "__main__":
    app.run(debug=True)






