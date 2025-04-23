# Εμφανίζει όλα τα διαθέσιμα blueprints οχημάτων στο CARLA

import carla

client = carla.Client("localhost", 2000)
client.set_timeout(10.0)

# Απόκτηση του κόσμου και της βιβλιοθήκης blueprints
world = client.get_world()
blueprint_library = world.get_blueprint_library()

# Εκτύπωση όλων των διαθέσιμων οχημάτων
for blueprint in blueprint_library.filter('vehicle.*'):
    print(blueprint.id)
