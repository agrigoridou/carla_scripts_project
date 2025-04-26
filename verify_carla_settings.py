import carla
import random
import time

# Σύνδεση με τον client και τον κόσμο
client = carla.Client('localhost', 2000)
client.set_timeout(10.0)

world = client.get_world()

# Ελέγχει αν το CARLA είναι σε synchronous ή asynchronous mode
settings = world.get_settings()
if settings.synchronous_mode:
    print("CARLA είναι σε synchronous mode.")
else:
    print("CARLA είναι σε asynchronous mode.")

# Παίρνουμε το blueprint library
blueprint_library = world.get_blueprint_library()

# Ενεργοποιούμε τα οχήματα και πεζούς
vehicle_blueprints = blueprint_library.filter('vehicle.*')
walker_blueprints = blueprint_library.filter('walker.pedestrian.*')

# Παίρνουμε τα spawn points
spawn_points = world.get_map().get_spawn_points()

if not spawn_points:
    print("Δεν υπάρχουν διαθέσιμα spawn points!")
    exit(1)

# Δημιουργούμε 5 οχήματα
print("Δημιουργία οχημάτων...")
for _ in range(5):
    vehicle_bp = random.choice(vehicle_blueprints)
    spawn_point = random.choice(spawn_points)
    try:
        vehicle = world.spawn_actor(vehicle_bp, spawn_point)
    except RuntimeError as e:
        print(f"Αποτυχία δημιουργίας οχήματος: {e}")

# Δημιουργούμε 5 πεζούς
print("Δημιουργία πεζών...")
for _ in range(5):
    walker_bp = random.choice(walker_blueprints)
    spawn_point = random.choice(spawn_points)
    try:
        walker = world.spawn_actor(walker_bp, spawn_point)
    except RuntimeError as e:
        print(f"Αποτυχία δημιουργίας πεζού: {e}")

# Περιμένουμε λίγο για να διασφαλίσουμε ότι οι ηθοποιοί είναι στο σύστημα
time.sleep(2)

# Έλεγχος αν υπάρχουν ενεργά οχήματα και πεζοί
active_vehicles = world.get_actors().filter('vehicle.*')
active_walkers = world.get_actors().filter('walker.pedestrian.*')

print(f"Αριθμός ενεργών οχημάτων: {len(active_vehicles)}")
print(f"Αριθμός ενεργών πεζών: {len(active_walkers)}")

# Έλεγχος αν υπάρχουν ενεργά οχήματα ή πεζοί
if len(active_vehicles) == 0:
    print("Δεν υπάρχουν ενεργά οχήματα στον κόσμο.")
else:
    print("Υπάρχουν ενεργά οχήματα στον κόσμο.")

if len(active_walkers) == 0:
    print("Δεν υπάρχουν ενεργοί πεζοί στον κόσμο.")
else:
    print("Υπάρχουν ενεργοί πεζοί στον κόσμο.")



/////////////////////////////////////////////////////////////////////


sysadm@icsd20048vm:~/Desktop/carla_scripts_project-main$ python3 verify_carla_settings.py
CARLA είναι σε asynchronous mode.
Δημιουργία οχημάτων...
Αποτυχία δημιουργίας οχήματος: std::exception
Αποτυχία δημιουργίας οχήματος: std::exception
Αποτυχία δημιουργίας οχήματος: std::exception
Αποτυχία δημιουργίας οχήματος: std::exception
Αποτυχία δημιουργίας οχήματος: std::exception
Δημιουργία πεζών...
Αποτυχία δημιουργίας πεζού: std::exception
Αποτυχία δημιουργίας πεζού: std::exception
Αποτυχία δημιουργίας πεζού: std::exception
Αποτυχία δημιουργίας πεζού: std::exception
Αποτυχία δημιουργίας πεζού: std::exception
Αριθμός ενεργών οχημάτων: 0
Αριθμός ενεργών πεζών: 0
Δεν υπάρχουν ενεργά οχήματα στον κόσμο.
Δεν υπάρχουν ενεργοί πεζοί στον κόσμο.
sysadm@icsd20048vm:~/Desktop/carla_scripts_project-main$ 
