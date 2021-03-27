"""This module connects to the external API to get facts about cats."""
import random

import requests


CAT_FACTS_URL = "https://cat-fact.herokuapp.com/facts"


def get_one_cat_fact():
    """Get the response from the external API - /facts endpoint, draw a random cat fact and return it"""
    response = requests.get(CAT_FACTS_URL)
    random_fact_id = random.randint(0, len(response.json()))

    return response.json()[random_fact_id]['text']