# Δημιουργεί ένα όχημα και το κινεί προς τα εμπρός για λίγα δευτερόλεπτα

import carla
import random
import time

client = carla.Client("localhost", 2000)
client.set_timeout(10.0)

world = client.get_world()
blueprint_library = world.get_blueprint_library()

# Επιλογή τυχαίου οχήματος Tesla Model 3
vehicle_bp = random.choice(blueprint_library.filter('vehicle.tesla.model3'))

# Επιλογή τυχαίου σημείου για spawn
spawn_point = random.choice(world.get_map().get_spawn_points())

# Δημιουργία του οχήματος
vehicle = world.spawn_actor(vehicle_bp, spawn_point)
print(f"Vehicle spawned: {vehicle.type_id}")

# Κίνηση προς τα εμπρός
vehicle.apply_control(carla.VehicleControl(throttle=0.5))

# Αναμονή 5 δευτερολέπτων
time.sleep(5)

# Καταστροφή του οχήματος
vehicle.destroy()
print("Vehicle destroyed.")
