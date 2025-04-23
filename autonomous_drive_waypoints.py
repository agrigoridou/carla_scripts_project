# Οδήγηση οχήματος αυτόνομα μέσω προκαθορισμένων waypoints

import carla
import time

client = carla.Client("localhost", 2000)
client.set_timeout(10.0)

world = client.get_world()
blueprint_library = world.get_blueprint_library()

# Δημιουργία οχήματος Tesla Model 3
vehicle_bp = blueprint_library.filter('vehicle.tesla.model3')[0]
spawn_point = world.get_map().get_spawn_points()[0]
vehicle = world.spawn_actor(vehicle_bp, spawn_point)

# Επιλογή πρώτων 5 waypoints από τον χάρτη
waypoints = world.get_map().get_spawn_points()[:5]

# Οδήγηση μέσω των waypoints
for wp in waypoints:
    vehicle.set_transform(wp)
    print(f"Moved to: {wp.location}")
    time.sleep(2)

# Καταστροφή του οχήματος
vehicle.destroy()
print("Vehicle destroyed.")
