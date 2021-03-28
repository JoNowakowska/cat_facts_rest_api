"""This module contains a class Translate which is called with the /translate endpoint."""

from flask_restx import Resource, reqparse

from google_translate_external_api import translate_text


data_parser = reqparse.RequestParser()
data_parser.add_argument('target',
                         required=True,
                         help='Please add a target language you want to translate your text to.')
data_parser.add_argument('text',
                         required=True,
                         action="append",
                         help='Please enter a string you want to translate.')


class Translate(Resource):
    def post(self):
        data = data_parser.parse_args()
        target = data.get("target").upper()
        text = data.get("text")

        try:
            translated = translate_text(target, text)
        except Exception as e:
            status_code = 500
            # the below should return a valid status code if error is on Google API's end, otherwise it rises ValueError
            try:
                status_code = int(str(e)[:3])
            except:
                pass
            return {"Something went wrong!": f"{e}"}, status_code

        return {f"Cat fact translated to {target}": translated}, 200
