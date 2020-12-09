import json

def load_data():
    with open("data.json", "r") as read_file:
        data = json.load(read_file)
    return data
