import json


def load_categories():
    with open("categories.json", "r", encoding="utf-8") as file:
        return json.load(file)


def save_categories(categories):
    with open("categories.json", "w", encoding="utf-8") as file:
        json.dump(categories, file, indent=4)