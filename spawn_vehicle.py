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

        # Φιλτράρουμε ΜΟΝΟ σωστά driveable οχήματα
        vehicles = blueprint_library.filter('vehicle.*')
        vehicles = [
            v for v in vehicles
            if 'actor' not in v.id and 'ue4' not in v.id and not v.id.endswith('destroyed')
        ]

        spawn_points = world.get_map().get_spawn_points()

        if not spawn_points:
            print('Δεν υπάρχουν spawn points διαθέσιμα!')
            return

        max_attempts = 10
        vehicle = None

        for attempt in range(max_attempts):
            vehicle_bp = random.choice(vehicles)
            spawn_point = random.choice(spawn_points)
            print(f'Προσπάθεια {attempt+1}: Δοκιμάζω να δημιουργήσω {vehicle_bp.id}...')

            try:
                vehicle = world.try_spawn_actor(vehicle_bp, spawn_point)
                if vehicle is not None:
                    actor_list.append(vehicle)
                    print(f'Επιτυχία στην προσπάθεια {attempt+1} με όχημα {vehicle_bp.id}!')
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
