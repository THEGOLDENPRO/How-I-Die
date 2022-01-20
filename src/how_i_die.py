from importlib.resources import path
import eel
import json
import os
import random

json_file = open("deaths.json")
list_of_deaths:list = (json.load(json_file))["deaths"]
last_random_num = None

eel.init(".")

@eel.expose
def get_death():
    global last_random_num
    while True:
        random_num = random.randint(0, len(list_of_deaths) - 1)
        if not random_num == last_random_num:
            break
    
    last_random_num = random_num
    return list_of_deaths[random_num]

eel.start("index.html", size=(1000, 600))