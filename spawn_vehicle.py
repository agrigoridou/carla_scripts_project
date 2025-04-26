import carla
import random
import time

def spawn_vehicle():
    client = carla.Client('localhost', 2000)
    client.set_timeout(10.0)
    world = client.get_world()
    blueprint_library = world.get_blueprint_library()

    # Επιλέγουμε το όχημα από τη λίστα που έχουμε
    vehicle_bp = blueprint_library.find('vehicle.dodge.charger')
    if not vehicle_bp:
        print("Το μπλεπρίντ για το όχημα δεν βρέθηκε!")
        return False

    # Επιλέγουμε τυχαία σημείο για το spawn
    spawn_point = random.choice(world.get_map().get_spawn_points())

    # Προσπαθούμε να δημιουργήσουμε το όχημα
    vehicle = None
    for attempt in range(10):  # Δοκιμάζουμε μέχρι 10 φορές
        try:
            vehicle = world.spawn_actor(vehicle_bp, spawn_point)
            print(f"Το όχημα δημιουργήθηκε επιτυχώς στην προσπάθεια {attempt + 1}.")
            return vehicle
        except RuntimeError:
            print(f"Απέτυχε το spawn στην προσπάθεια {attempt + 1}. Δοκιμάζω ξανά...")
            time.sleep(1)  # Παύση 1 δευτερολέπτου πριν την επόμενη προσπάθεια

    print("Απέτυχε η δημιουργία οχήματος μετά από 10 προσπάθειες.")
    return False

def main():
    print("Προσπαθώ να δημιουργήσω το όχημα Dodge Charger...")
    vehicle = spawn_vehicle()

    if vehicle:
        print(f"Το όχημα {vehicle.type_id} δημιουργήθηκε επιτυχώς.")
    else:
        print("Η δημιουργία του οχήματος απέτυχε.")

    # Καθαρισμός ηθοποιών
    print("Καθαρίζω ηθοποιούς...")
    if vehicle:
        vehicle.destroy()
    print("Τέλος!")

if __name__ == '__main__':
    main()


//////////////////////////////////////////////////////////

sysadm:~/Desktop/carla_scripts_project-main$ python3 spawn_vehicle.py
Προσπαθώ να δημιουργήσω το όχημα Dodge Charger...
Απέτυχε το spawn στην προσπάθεια 1. Δοκιμάζω ξανά...
Απέτυχε το spawn στην προσπάθεια 2. Δοκιμάζω ξανά...
Απέτυχε το spawn στην προσπάθεια 3. Δοκιμάζω ξανά...
Απέτυχε το spawn στην προσπάθεια 4. Δοκιμάζω ξανά...
Απέτυχε το spawn στην προσπάθεια 5. Δοκιμάζω ξανά...
Απέτυχε το spawn στην προσπάθεια 6. Δοκιμάζω ξανά...
Απέτυχε το spawn στην προσπάθεια 7. Δοκιμάζω ξανά...
Απέτυχε το spawn στην προσπάθεια 8. Δοκιμάζω ξανά...
Απέτυχε το spawn στην προσπάθεια 9. Δοκιμάζω ξανά...
Απέτυχε το spawn στην προσπάθεια 10. Δοκιμάζω ξανά...
Απέτυχε η δημιουργία οχήματος μετά από 10 προσπάθειες.
Η δημιουργία του οχήματος απέτυχε.
Καθαρίζω ηθοποιούς...
Τέλος!
sysadm:~/Desktop/carla_scripts_project-main$ 
