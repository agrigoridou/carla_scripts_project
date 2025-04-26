import carla
import random
import time

# Σύνδεση στον CARLA server
client = carla.Client('localhost', 2000)
client.set_timeout(10.0)

# Λήψη του κόσμου
world = client.get_world()

# Λήψη των διαθέσιμων blueprints (μοντέλα οχημάτων)
blueprint_library = world.get_blueprint_library()
vehicle_blueprints = blueprint_library.filter('vehicle.*')

# Λήψη των διαθέσιμων spawn points
spawn_points = world.get_map().get_spawn_points()

if not spawn_points:
    print("Error: No spawn points available.")
    exit(1)

spawn_point = random.choice(spawn_points)

# Επιλέγουμε blueprint και προσπαθούμε να κάνουμε spawn
for attempt in range(10):
    vehicle_bp = random.choice(vehicle_blueprints)
    try:
        vehicle = world.spawn_actor(vehicle_bp, spawn_point)
        print(f"Vehicle spawned: {vehicle.type_id}")
        break
    except RuntimeError as e:
        print(f"Spawn failed with blueprint {vehicle_bp.id}, trying another one...")
else:
    print("Failed to spawn vehicle after 10 attempts.")
    exit(1)

# Εφαρμογή κίνησης προς τα εμπρός
vehicle.apply_control(carla.VehicleControl(throttle=0.5))

# Αναμονή 5 δευτερολέπτων
time.sleep(5)

# Καταστροφή του οχήματος
vehicle.destroy()
print("Vehicle destroyed.")
