import json

def load_data():
    with open("data.json", "r") as read_file:
        data = json.load(read_file)
    return data

def save_data(data):
    with open("data.json", "w") as write_file:
        json.dump(data, write_file)


def modify_data(data, **kwarg):
    for key, value in kwarg.items():
        if key in data.keys():
            data[key] = value
        

def calculate(data):
