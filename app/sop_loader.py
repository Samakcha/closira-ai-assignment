import json


def load_sop():
    with open("data/sop.json", "r") as file:
        sop_data = json.load(file)

    return sop_data