import time

# Initialize parking spots
parking_spots = [
    {"id": 1, "status": "available"},
    {"id": 2, "status": "available"},
    {"id": 3, "status": "available"},
    {"id": 4, "status": "available"},
    {"id": 5, "status": "available"}
]

# Define function to find available parking spots
def find_available_spots():
    available_spots = []
    for spot in parking_spots:
        if spot["status"] == "available":
            available_spots.append(spot)
    return available_spots

# Define function to reserve a parking spot
def reserve_spot(spot_id):
    for spot in parking_spots:
        if spot["id"] == spot_id:
            if spot["status"] == "available":
                spot["status"] = "reserved"
                return True
            else:
                return False

# Define function to release a parking spot
def release_spot(spot_id):
    for spot in parking_spots:
        if spot["id"] == spot_id:
            if spot["status"] == "reserved":
                spot["status"] = "available"
                return True
            else:
                return False

# Define function to simulate car arrival
def simulate_car_arrival():
    time.sleep(3)
    available_spots = find_available_spots()
    if len(available_spots) > 0:
        spot = available_spots[0]
        reserve_spot(spot["id"])
        print("Car parked in spot", spot["id"])
        return True
    else:
        print("No available parking spots")
        return False

# Define function to simulate car departure
def simulate_car_departure():
    time.sleep(3)
    spot_id = int(input("Enter spot ID: "))
    released = release_spot(spot_id)
    if released:
        print("Spot", spot_id, "released")
        return True
    else:
        print("Spot", spot_id, "not reserved or already released")
        return False

# Main program loop
while True:
    action = input("Enter action (arrive/depart): ")
    if action == "arrive":
        simulate_car_arrival()
    elif action == "depart":
        simulate_car_departure()
    else:
        print("Invalid action")