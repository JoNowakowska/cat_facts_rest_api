"""
This is the main module of the app. It contains the app instance (app).
"""


from flask import Flask
from flask_restx import Api

from resources.fact import Fact
from resources.translate import TranslateEnPl

app = Flask(__name__)


api = Api(app)
api.add_resource(Fact, '/fact')
api.add_resource(TranslateEnPl, '/translate_en_pl')


if __name__ == '__main__':
    app.run(port=5000, debug=True)