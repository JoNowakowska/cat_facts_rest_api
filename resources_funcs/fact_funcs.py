"""Contains functions used in resources/fact."""
from cat_facts_external_api import get_one_cat_fact


def get_fun_facts(amount):
    """Connect to fun facts external api and return as many fun facts as defined by amount."""
    result = []
    if not amount:
        amount = 1
    for i in range(int(amount)):
        fact = get_one_cat_fact()
        result.append(fact)

    return result


def try_to_get_fun_facts(animal, amount):
    """If a proper animal provided return fun fact(s) else return a proper message."""
    valid = False

    if animal == "cat":
        valid = True
        result = get_fun_facts(amount)
    elif not animal:
        result = ["Please provide an animal to learn a fun fact of it."]
    else:
        result = ["Sorry, we only have fun facts about cats. Try again."]

    return valid, result
