import carla

client = carla.Client('localhost', 2000)
client.set_timeout(10.0)

world = client.get_world()
map = world.get_map()

spawn_points = map.get_spawn_points()

if not spawn_points:
    print("No spawn points found!")
else:
    print(f"Found {len(spawn_points)} spawn points:\n")
    for idx, spawn_point in enumerate(spawn_points):
        location = spawn_point.location
        rotation = spawn_point.rotation
        print(f"[{idx}] Location(x={location.x:.2f}, y={location.y:.2f}, z={location.z:.2f}) | Rotation(pitch={rotation.pitch:.2f}, yaw={rotation.yaw:.2f}, roll={rotation.roll:.2f})")
