# spawn_vehicle.py

import carla
import random
import time

def main():
    actor_list = []

    try:
        # Συνδέσου στο CARLA Server
        client = carla.Client('localhost', 2000)
        client.set_timeout(5.0)

        # Φέρε τον κόσμο
        world = client.get_world()

        # Φέρε τα blueprints
        blueprint_library = world.get_blueprint_library()

        # Διάλεξε όχημα
        vehicle_bp = blueprint_library.find('vehicle.dodge.charger')  # Εδώ μπορείς να αλλάξεις όχημα

        # Φέρε τα spawn points
        spawn_points = world.get_map().get_spawn_points()

        if not spawn_points:
            print('Δεν βρέθηκαν spawn points!')
            return

        # Διάλεξε τυχαίο spawn point
        spawn_point = random.choice(spawn_points)

        # Κάνε προσπάθεια για spawn
        vehicle = world.try_spawn_actor(vehicle_bp, spawn_point)
        if vehicle is None:
            print('Απέτυχε το spawn του οχήματος. Δοκίμασε ξανά!')
            return

        print(f'Όχημα {vehicle.type_id} δημιουργήθηκε στη θέση {spawn_point.location}')

        actor_list.append(vehicle)

        # Οδήγησέ το λίγο μπροστά για δοκιμή
        vehicle.set_autopilot(True)

        # Άφησε το simulation να τρέξει για λίγο
        time.sleep(15)

    finally:
        print('Καθαρίζω ηθοποιούς...')
        for actor in actor_list:
            actor.destroy()
        print('Τέλος!')

if __name__ == '__main__':
    main()





/////////////////////////////////


sysadm:~/Desktop/carla_scripts_project-main$ python3 spawn_vehicle.py
Απέτυχε το spawn του οχήματος. Δοκίμασε ξανά!
Καθαρίζω ηθοποιούς...
Τέλος!
sysadm:~/Desktop/carla_scripts_project-main$ 

