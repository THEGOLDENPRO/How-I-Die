import eel
import json
import random
import os
import sys
from pygame import mixer 

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

json_file = open(resource_path("deaths.json"))
list_of_deaths:dict = (json.load(json_file))["deaths"]
last_random_num = None

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

eel.init(resource_path("."))

@eel.expose
def get_death():
    global last_random_num

    # Generate random number.
    while True:
        random_num = random.randint(1, len(list_of_deaths))
        if not random_num == last_random_num:
            break
        
    # Play sound.
    mixer.init()
    mixer.music.load(resource_path("./audio/death.mp3"))
    mixer.music.set_volume(0.2)
    mixer.music.play()

    # Return message and author to the front end.
    last_random_num = random_num
    return list_of_deaths[str(random_num)]["message"], list_of_deaths[str(random_num)]["author"]

eel.start("web/index.html", size=(1000, 600), shutdown_delay=0.0)
