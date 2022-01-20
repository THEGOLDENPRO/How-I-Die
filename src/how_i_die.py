import eel
import json
import random
from pygame import mixer 
json_file = open("deaths.json")
list_of_deaths:dict = (json.load(json_file))["deaths"]
last_random_num = None

eel.init(".")

@eel.expose
def get_death():
    global last_random_num

    # Generate random number.
    while True:
        random_num = random.randint(1, len(list_of_deaths) - 1)
        if not random_num == last_random_num:
            break
        
    # Play sound.
    mixer.init()
    mixer.music.load("./audio/death.mp3")
    mixer.music.set_volume(0.2)
    mixer.music.play()

    # Return message and author to the front end.
    last_random_num = random_num
    return list_of_deaths[str(random_num)]["message"], list_of_deaths[str(random_num)]["author"]

eel.start("index.html", size=(1000, 600), shutdown_delay=0.0)