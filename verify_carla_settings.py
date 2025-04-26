import carla

# Σύνδεση στον CARLA server
client = carla.Client('localhost', 2000)
client.set_timeout(10.0)

# Λήψη του κόσμου (world) από τον CARLA server
world = client.get_world()

# Έλεγχος για synchronous mode
settings = world.get_settings()
if settings.synchronous_mode:
    print("CARLA είναι σε synchronous mode.")
else:
    print("CARLA είναι σε asynchronous mode.")

# Έλεγχος για ενεργά οχήματα και πεζούς
actors = world.get_actors()

# Φιλτράρισμα των οχημάτων και πεζών
vehicles = [actor for actor in actors if 'vehicle' in actor.type_id]
pedestrians = [actor for actor in actors if 'walker' in actor.type_id]

# Εμφάνιση των ενεργών οχημάτων και πεζών
print(f"Αριθμός ενεργών οχημάτων: {len(vehicles)}")
print(f"Αριθμός ενεργών πεζών: {len(pedestrians)}")

if len(vehicles) > 0:
    print("Υπάρχουν ενεργά οχήματα στον κόσμο.")
else:
    print("Δεν υπάρχουν ενεργά οχήματα στον κόσμο.")

if len(pedestrians) > 0:
    print("Υπάρχουν ενεργοί πεζοί στον κόσμο.")
else:
    print("Δεν υπάρχουν ενεργοί πεζοί στον κόσμο.")
