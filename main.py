import json

def load_data():
    with open("data.json", "r") as read_file:
        data = json.load(read_file)
    return data

def save_data(data):
    with open("data.json", "w") as write_file:
        json.dump(data, write_file)

# data = load_data()

# data["name"] = "Bob"

# save_data(data)