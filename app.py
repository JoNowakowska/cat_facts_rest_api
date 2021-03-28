"""This is the main module of the app. It contains the app instance (app)."""

from flask import Flask
from flask_restx import Api

from resources.fact import Facts
from resources.translate import Translate

app = Flask(__name__)


api = Api(app)
api.add_resource(Facts, '/facts')
api.add_resource(Translate, '/translate')


if __name__ == '__main__':
    app.run(port=5000, debug=True)