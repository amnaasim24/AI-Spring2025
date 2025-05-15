import time

class HospitalEnvironment:
    def __init__(self):
        self.corridors = ["Corridor1", "Corridor2", "Corridor3"]
        self.patient_rooms = {"Room101": "Patient1", "Room102": "Patient2", "Room103": "Patient3"}
        self.nurse_stations = ["NurseStation1", "NurseStation2"]
        self.medicine_storage = {"MedicineA": 5, "MedicineB": 3, "MedicineC": 7}

class DeliveryRobot:
    def __init__(self, environment):
        self.environment = environment
        self.current_location = "Corridor1"
        self.medicine_inventory = {}

    def move_to(self, location):
        print(f"Moving from {self.current_location} to {location}...")
        time.sleep(1)
        self.current_location = location
        print(f"Arrived at {location}.")

    def pick_up_medicine(self, medicine, quantity):
        if medicine in self.environment.medicine_storage and self.environment.medicine_storage[medicine] >= quantity:
            self.environment.medicine_storage[medicine] -= quantity
            self.medicine_inventory[medicine] = self.medicine_inventory.get(medicine, 0) + quantity
            print(f"Picked up {quantity} units of {medicine}.")
        else:
            print(f"Error: {medicine} is not available in sufficient quantity.")

    def deliver_medicine(self, room, patient, medicine, quantity):
        if medicine in self.medicine_inventory and self.medicine_inventory[medicine] >= quantity:
            self.medicine_inventory[medicine] -= quantity
            print(f"Delivered {quantity} units of {medicine} to {patient} in {room}.")
            self.scan_patient_id(room, patient)
        else:
            print(f"Error: Not enough {medicine} in inventory to deliver to {patient}.")

    def scan_patient_id(self, room, patient):
        print(f"Scanning patient ID for {patient} in {room}...")
        time.sleep(1)
        print(f"Patient ID verified for {patient}.")

    def alert_staff(self, message):
        print(f"Alerting staff at {self.environment.nurse_stations[0]}: {message}")

def execute_delivery_plan(robot, delivery_schedule):
    for task in delivery_schedule:
        room, patient, medicine, quantity = task
        print(f"\nProcessing delivery for {patient} in {room}...")

        robot.move_to("MedicineStorage")
        robot.pick_up_medicine(medicine, quantity)

        robot.move_to(room)
        robot.deliver_medicine(room, patient, medicine, quantity)

        if medicine == "MedicineC":
            robot.alert_staff(f"Critical medicine delivered to {patient} in {room}.")

hospital = HospitalEnvironment()
robot = DeliveryRobot(hospital)

delivery_schedule = [
    ("Room101", "Patient1", "MedicineA", 2),
    ("Room102", "Patient2", "MedicineB", 1),
    ("Room103", "Patient3", "MedicineC", 1),
]

execute_delivery_plan(robot, delivery_schedule)

print("\nFinal Medicine Storage:", hospital.medicine_storage)
print("Robot's Medicine Inventory:", robot.medicine_inventory)