import json


def load_categories():

    with open("categories.json", "r", encoding="utf-8") as file:
        return json.load(file)