# 𝗤𝘂𝗲𝘀𝘁𝗶𝗼𝗻 2:
# Design the required class(es) so that the following expected output is 
# generated. Do not change any given code.

# Write you code here
class Vehicle:
    def __init__(self, v_id, type, max_passenger):
        self.v_id = v_id
        self.type = type
        self.max_passenger = max_passenger
        self.passengers = list()
        self.passenger_count = 0
    def addPassenger(self, p):
        if self.passenger_count < self.max_passenger:
            print(f"{p.name} has taken the {self.type}")
            self.passengers.append(p)
            self.passenger_count += 1
        else:
            print(f"{self.type} is loaded. {p.name} cannot take the {self.type}")
    def details(self):
        print(f"Details of {self.v_id} {self.type}:")
        print(f"Total passengers: {self.passenger_count}")

        for passenger in self.passengers:
            print(f"Passenger name : {passenger.name}, Destination: {passenger.dest}, Fare: {passenger.fare}")

class Passenger:
    def __init__(self, name, dest=None):
        if dest == None:
            print("Destination cannot be empty!")
        self.name = name
        self.dest = dest
        self.fare = None
    def calculateFare(self, v):
        print(f"Calculating fare for {self.name}")

        try:
            self.fare = fareChart[self.dest] * 10
        except:
            self.fare = fareChart["Others"] * 10          
    def setDestination(self, dest=None):
        if dest == None:
            print("Destination cannot be empty!")
        self.dest = dest

fareChart = {'Banani': 2, 'Mohakhali':3, 'Mohammadpur':4, 'New Market':5, 'Others':6}
v1 = Vehicle("Dhaka-123", "Bus", 3)
p1 = Passenger("Sam", "Banani")
print("1.===========================")
v1.addPassenger(p1)
print("2.===========================")
p1.calculateFare(v1)
print("3.===========================")
p2 = Passenger("John", "Mohakhali")
p3 = Passenger("Bran")
print("4.===========================")
p3.setDestination()
print("5.===========================")
p3.setDestination("Kakrail")
print("6.===========================")
v1.addPassenger(p2)
print("7.===========================")
p2.calculateFare(v1)
print("8.===========================")
v1.addPassenger(p3)
print("9.===========================")
p3.calculateFare(v1)
p4 = Passenger("Mark", "Mohammadpur")
print("10.===========================")
p4.setDestination()
print("11.===========================")
v1.addPassenger(p4)
v1.addPassenger(Passenger("Jack", "New Market"))
print("12.===========================")
v1.details()
v2 = Vehicle("Chittagong-798", "Car", 0)
print("13.===========================")
v2.addPassenger(p1)
v2.addPassenger(p3)
print("14.===========================")
v2.details()

# Output:
# 1.===========================
# Sam has taken the Bus.
# 2.===========================
# Calculating fare for Sam
# 3.===========================
# Destination cannot be empty!
# 4.===========================
# Destination cannot be empty!
# 5.===========================
# Destination of Bran is updated to Kakrail
# 6.===========================
# John has taken the Bus.
# 7.===========================
# Calculating fare for John
# 8.===========================
# Bran has taken the Bus.
# 9.===========================
# Calculating fare for Bran
# 10.===========================
# Destination cannot be empty!
# 11.===========================
# Bus is loaded. Mark cannot take the Bus.
# Bus is loaded. Jack cannot take the Bus.
# 12.===========================
# Details of Dhaka-123 Bus:
# Total Passengers: 3
# Passenger name : Sam, Destination: Banani, Fare: 20
# Passenger name : John, Destination: Mohakhali, Fare: 30
# Passenger name : Bran, Destination: Kakrail, Fare: 60
# 13.===========================
# Car is loaded. Sam cannot take the Car.
# Car is loaded. Bran cannot take the Car.
# 14.===========================
# Details of Chittagong-798 Car:
# Total Passengers: 0
