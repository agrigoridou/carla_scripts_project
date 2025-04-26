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

vehicle = None

# Προσπάθεια να κάνουμε spawn (μέχρι 20 φορές)
for attempt in range(20):
    spawn_point = random.choice(spawn_points)
    vehicle_bp = random.choice(vehicle_blueprints)
    try:
        vehicle = world.spawn_actor(vehicle_bp, spawn_point)
        print(f"[SUCCESS] Vehicle spawned: {vehicle.type_id}")
        break
    except RuntimeError as e:
        print(f"[Attempt {attempt+1}] Failed to spawn {vehicle_bp.id} at spawn point {spawn_point.location}, trying again...")

if vehicle is None:
    print("[ERROR] Failed to spawn a vehicle after multiple attempts.")
    exit(1)

# Κίνηση προς τα εμπρός με σταδιακή επιτάχυνση
print("Starting vehicle movement...")

vehicle.apply_control(carla.VehicleControl(throttle=0.3))
time.sleep(2)

vehicle.apply_control(carla.VehicleControl(throttle=0.6))
time.sleep(2)

vehicle.apply_control(carla.VehicleControl(throttle=0.8))
time.sleep(2)

# Φρενάρισμα
vehicle.apply_control(carla.VehicleControl(throttle=0.0, brake=1.0))
time.sleep(2)

# Καταστροφή του οχήματος
vehicle.destroy()
print("Vehicle destroyed successfully.")
