# define a class
class Bike:
    name = ""
    gear = 0

# create object of class
bike1 = Bike()

# access attributes and assign new values
bike1.gear = 11
bike1.name = "Mountain Bike"

print(f"Name: {bike1.name}, Gears: {bike1.gear}")
# define a class
class Employee:
    # define a property
    employee_id = 0

# create two objects of the Employee class
employee1 = Employee()
employee2 = Employee()

# access property using employee1
employee1.employeeID = 1001
print(f"Employee ID: {employee1.employeeID}")

# access properties using employee2
employee2.employeeID = 1002
print(f"Employee ID: {employee2.employeeID}")
# create a class
class Room:
    length = 0.0
    breadth = 0.0
    
    # method to calculate area
    def calculate_area(self):
        print("Area of Room =", self.length * self.breadth)

# create object of Room class
study_room = Room()

# assign values to all the properties 
study_room.length = 42.5
study_room.breadth = 30.8

# access method inside class
study_room.calculate_area()
