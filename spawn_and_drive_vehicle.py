import carla
import random
import time

client = carla.Client('localhost', 2000)
client.set_timeout(10.0)

world = client.get_world()
blueprint_library = world.get_blueprint_library()

# Παίρνουμε μόνο οχήματα που είναι actually usable
vehicle_blueprints = blueprint_library.filter('vehicle.*')

spawn_points = world.get_map().get_spawn_points()

if not spawn_points:
    print("Error: No spawn points available.")
    exit(1)

spawn_point = random.choice(spawn_points)

# Επιλέγουμε blueprint μέχρι να πετύχουμε valid spawn
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

# Κίνηση προς τα εμπρός
vehicle.apply_control(carla.VehicleControl(throttle=0.5))

time.sleep(5)

vehicle.destroy()
print("Vehicle destroyed.")
