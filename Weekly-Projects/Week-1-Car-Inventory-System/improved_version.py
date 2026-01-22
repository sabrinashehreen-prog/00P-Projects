"""
IN-CLASS LAB: Car and ElectricCar Classes
Date: 21 Jan 2026
Class: Object-Oriented Programming

This is the EXACT code I wrote during class.
It demonstrates basic OOP concepts I just learned.
"""

class Car:
    def __init__(self, brand, model, year, mileage): #initialize a car object with attributes
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = mileage

class ElectricCar(Car): #inherits from Car class.
    def __init__(self, brand, model, year, mileage, battery_cap): #initialze an class called ElectricCar with all the necessary attributes
        super().__init__(brand, model, year, mileage)  #call the constructors from parent class called Car
        self.battery_cap = battery_cap    #adding new attribute called battry_capacity

def display_info(car): #now dispaly info will override parent method and will show the newly added attribute 
        print(f" Brand: {car.brand}")
        print(f" Model: {car.model}")
        print(f" Year: {car.year}")
        print(f" Mileage: {car.mileage}")
        if isinstance (car, ElectricCar):
            print(f" Batterry Capacity: {car.battery_cap}")
        print()
        

#Object Instantiation(Car) means creating 3 objects for object Car with differnt values
car1 = Car("Toyota", "Camry", 2020, 15000)
car2 = Car("Mazda", "miata", 2018, 25000)
car3 = Car("Ford", "Mustang", 2022, 5000)

#Object Instantiation(ElectriCar) creating 2 ElectricCar objects with battery capacity
electric_car1 = ElectricCar("Tesla", "model 3", 2023, 12000, 75)
electric_car2 = ElectricCar("Nissan", "Leaf", 2021, 25000, 45)

print("=" * 40)
print("MY IN-CLASS CODE OUTPUT")
print("=" * 40)
display_info(car1)
display_info(car2)
display_info(car3)

display_info(electric_car1)
display_info(electric_car2)