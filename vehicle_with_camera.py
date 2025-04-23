# Δημιουργεί ένα όχημα με κάμερα RGB και αποθηκεύει εικόνες από το περιβάλλον

import carla
import time
import os

client = carla.Client("localhost", 2000)
client.set_timeout(10.0)

world = client.get_world()
blueprint_library = world.get_blueprint_library()

# Δημιουργία οχήματος Tesla Model 3
vehicle_bp = blueprint_library.filter('vehicle.tesla.model3')[0]
spawn_point = world.get_map().get_spawn_points()[0]
vehicle = world.spawn_actor(vehicle_bp, spawn_point)

# Προσθήκη αισθητήρα κάμερας RGB
camera_bp = blueprint_library.find('sensor.camera.rgb')
camera_bp.set_attribute('image_size_x', '800')
camera_bp.set_attribute('image_size_y', '600')
camera_bp.set_attribute('fov', '90')

# Τοποθέτηση κάμερας στο όχημα
camera_transform = carla.Transform(carla.Location(x=1.5, z=2.4))
camera = world.spawn_actor(camera_bp, camera_transform, attach_to=vehicle)

# Δημιουργία φακέλου για εικόνες
os.makedirs("output", exist_ok=True)

# Callback για αποθήκευση κάθε frame
def save_image(image):
    image.save_to_disk(f"output/frame_{image.frame}.png")
    print(f"Saved frame {image.frame}")

camera.listen(lambda image: save_image(image))

# Κίνηση οχήματος
vehicle.apply_control(carla.VehicleControl(throttle=0.4, steer=0.1))

time.sleep(10)

# Τερματισμός και καθαρισμός
camera.stop()
camera.destroy()
vehicle.destroy()
print("Simulation ended.")
