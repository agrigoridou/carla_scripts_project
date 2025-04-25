import carla
import random
import time
import pygame
import numpy as np

# Αρχικοποίηση pygame
pygame.init()

# Σύνδεση με τον CARLA server
client = carla.Client('localhost', 2000)
client.set_timeout(10.0)
world = client.get_world()

# Βρίσκουμε ένα random όχημα
blueprint_library = world.get_blueprint_library()
vehicle_bp = random.choice(blueprint_library.filter('vehicle.*'))
spawn_point = random.choice(world.get_map().get_spawn_points())

# Κάνουμε spawn το όχημα
vehicle = world.spawn_actor(vehicle_bp, spawn_point)
print(f"Vehicle spawned: {vehicle.type_id}")

# Δημιουργία κάμερας
camera_bp = blueprint_library.find('sensor.camera.rgb')
camera_bp.set_attribute('image_size_x', '800')
camera_bp.set_attribute('image_size_y', '600')
camera_bp.set_attribute('fov', '90')

camera_transform = carla.Transform(carla.Location(x=1.5, z=2.4))  # Μπροστά και πάνω από το όχημα
camera = world.spawn_actor(camera_bp, camera_transform, attach_to=vehicle)
print("Camera attached to vehicle.")

# Λίστα για να αποθηκεύουμε τα actors ώστε να τα καταστρέψουμε στο τέλος
actor_list = [vehicle, camera]

# Παράθυρο Pygame
display = pygame.display.set_mode((800, 600), pygame.HWSURFACE | pygame.DOUBLEBUF)
pygame.display.set_caption("CARLA Camera View")

# Μετατροπή εικόνας από κάμερα
def process_img(image):
    array = np.frombuffer(image.raw_data, dtype=np.uint8)
    array = np.reshape(array, (image.height, image.width, 4))
    array = array[:, :, :3]  # Κρατάμε μόνο RGB
    array = array[:, :, ::-1]  # BGR -> RGB
    surface = pygame.surfarray.make_surface(array.swapaxes(0, 1))
    return surface

# Callback όταν λαμβάνουμε εικόνα από την κάμερα
image_surface = None

def camera_callback(image):
    global image_surface
    image_surface = process_img(image)

camera.listen(lambda image: camera_callback(image))

# Κύριο loop
try:
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                raise KeyboardInterrupt()

        if image_surface:
            display.blit(image_surface, (0, 0))
            pygame.display.flip()

except KeyboardInterrupt:
    print("\nExiting...")

finally:
    print("Destroying actors...")
    for actor in actor_list:
        actor.destroy()
    pygame.quit()
    print("Done.")
