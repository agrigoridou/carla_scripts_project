def print_available_vehicles(world):
    blueprint_library = world.get_blueprint_library()
    vehicles = [bp.id for bp in blueprint_library.filter('vehicle')]
    print("Διαθέσιμα οχήματα:", vehicles)

def main():
    client = carla.Client('localhost', 2000)
    client.set_timeout(10.0)
    world = client.get_world()

    # Εκτυπώνουμε τα διαθέσιμα οχήματα για να δούμε αν υπάρχει το Dodge Charger
    print_available_vehicles(world)
    
    print("Προσπαθώ να δημιουργήσω το όχημα Dodge Charger...")
    vehicle = spawn_vehicle()

    if vehicle:
        print(f"Το όχημα {vehicle.type_id} δημιουργήθηκε επιτυχώς.")
    else:
        print("Η δημιουργία του οχήματος απέτυχε.")
