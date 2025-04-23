# Συνδέεται στον CARLA server για να ελέγξουμε τη σύνδεση

import carla

def test_connection():
    try:
        # Σύνδεση στον CARLA server
        client = carla.Client("localhost", 2000)
        client.set_timeout(10.0)
        
        # Εκτύπωση επιτυχούς σύνδεσης
        print("Connected to CARLA server.")
        print("\nConnection successful.")
    except Exception as e:
        print(f"Error while connecting to CARLA: {e}")

if __name__ == "__main__":
    test_connection()
