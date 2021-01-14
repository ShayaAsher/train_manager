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
    
    #формула определения метаболизма
    target = 10 * data["weight"] + 6.25 * data["height"] - 5 * data["age"] 

    # корректировка по полу (Результат для ежедневного меню)
    if data["sex"] == "f":
        target -= 161
    else:
        target += 5

    # корректировка по активности ( результат для программы тренировок)
    active_coef = [1.2, 1.35, 1.5, 1.7, 1.8]
    intensity_activity = target * active_coef[data["active"] - 1]
    
    # то что выше, делает то что делают эти if
    # if  aktiv == 1:
    #     program = result * 1.2   
    # if  aktiv == 2:
    #     program = result * 1.35
    # if  aktiv == 3:
    #     program = result * 1.5
    # if  aktiv == 4:
    #     program = result * 1.7
    # if  aktiv == 5:
    #     program = result * 1.8

    response = {
        "target_menu": target,
        "intensity_sport": intensity_activity
    }

    return response

