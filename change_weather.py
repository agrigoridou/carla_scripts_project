# Αλλάζει τις καιρικές συνθήκες στον προσομοιωτή CARLA

import carla

client = carla.Client("localhost", 2000)
client.set_timeout(10.0)

world = client.get_world()

# Ορισμός νέου καιρού
weather = carla.WeatherParameters(
    cloudiness=80.0,         # Συννεφιά 80%
    precipitation=30.0,      # Βροχή 30%
    sun_altitude_angle=70.0  # Ήλιος ψηλά στον ουρανό
)

# Εφαρμογή του καιρού στον κόσμο
world.set_weather(weather)
print("Weather changed.")
