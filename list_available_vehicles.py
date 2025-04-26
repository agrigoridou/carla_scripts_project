# Εμφανίζει όλα τα διαθέσιμα blueprints οχημάτων στο CARLA

import carla

def list_available_vehicles():
    client = carla.Client('localhost', 2000)
    client.set_timeout(5.0)
    world = client.get_world()
    blueprint_library = world.get_blueprint_library()

    # Φιλτράρουμε ΜΟΝΟ τα οχήματα
    vehicles = blueprint_library.filter('vehicle.*')

    print(f"Σύνολο διαθέσιμων οχημάτων: {len(vehicles)}")
    for vehicle in vehicles:
        print(vehicle.id)

if __name__ == '__main__':
    list_available_vehicles()
