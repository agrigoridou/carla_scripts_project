# carla_scripts_project
Εxamples

# CARLA Scripts Collection 🚗

Αυτός ο φάκελος περιέχει βασικά παραδείγματα Python για την προσομοίωση στον CARLA Simulator v0.10.0 (UE5).

## Περιεχόμενα

- `test_connection.py`: Έλεγχος σύνδεσης με τον CARLA server.
- `list_vehicle_blueprints.py`: Λίστα διαθέσιμων blueprint οχημάτων.
- `spawn_and_drive_vehicle.py`: Spawn και οδήγηση ενός οχήματος.
- `camera_sensor_save_images.py`: Προσθήκη κάμερας σε όχημα και αποθήκευση εικόνων.
- `change_weather.py`: Αλλαγή καιρικών συνθηκών στον κόσμο.
- `waypoint_autonomous_drive.py`: Αυτόνομη οδήγηση σε σειρά waypoints.

## Προαπαιτούμενα

- Ubuntu 22.04  
- Python 3.10.12  
- CARLA Simulator (v0.10.0 για UE5)  
- Πρέπει να τρέχει ο CARLA server:  
  ```bash
  cd CarlaUE5/Build/Package/Carla-0.10.0-Linux-Shipping/Linux
  ./CarlaUnreal.sh
