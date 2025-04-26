import carla
import random
import time

def main():
    actor_list = []
    try:
        client = carla.Client('localhost', 2000)
        client.set_timeout(5.0)

        world = client.get_world()

        blueprint_library = world.get_blueprint_library()
        vehicle_bp = random.choice(blueprint_library.filter('vehicle.*'))

        spawn_points = world.get_map().get_spawn_points()

        if not spawn_points:
            print('Δεν υπάρχουν spawn points διαθέσιμα!')
            return

        max_attempts = 10
        vehicle = None

        for attempt in range(max_attempts):
            spawn_point = random.choice(spawn_points)
            try:
                vehicle = world.try_spawn_actor(vehicle_bp, spawn_point)
                if vehicle is not None:
                    actor_list.append(vehicle)
                    print(f'Επιτυχής δημιουργία οχήματος στην προσπάθεια {attempt+1}!')
                    break
                else:
                    print(f'Απέτυχε το spawn στην προσπάθεια {attempt+1}. Δοκιμάζω ξανά...')
            except RuntimeError as e:
                print(f'Σφάλμα στην προσπάθεια {attempt+1}: {e}')

        if vehicle is None:
            print('Απέτυχε η δημιουργία οχήματος μετά από 10 προσπάθειες.')
            return

        vehicle.set_autopilot(True)
        time.sleep(10)

    finally:
        print('Καθαρίζω ηθοποιούς...')
        for actor in actor_list:
            actor.destroy()
        print('Τέλος!')

if __name__ == '__main__':
    main()




//////////////////////////////////////////////////////////////////


sysadm:~/Desktop/carla_scripts_project-main$ python3 spawn_vehicle.py
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
Καθαρίζω ηθοποιούς...
Τέλος!
sysadm:~/Desktop/carla_scripts_project-main$ 
