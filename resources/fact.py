"""This module contains a class Facts which is called with the /facts endpoint."""

from flask_restx import Resource
from flask import request

from resources_funcs.fact_funcs import try_to_get_fun_facts


class Facts(Resource):
    def get(self):
        animal = request.args.get("animal")
        amount = request.args.get("amount")

        valid, result = try_to_get_fun_facts(animal, amount)

        if not valid:
            return {"message": result}, 400

        return {"fun fact": result}, 200
