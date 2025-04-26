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
        vehicle_bp = blueprint_library.find('vehicle.dodge.charger_2020')

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
                    print(f'Απέ
