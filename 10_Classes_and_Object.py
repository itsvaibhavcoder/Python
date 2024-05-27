#Define a class named 'Car'
class Car:
    #Class variable
    fuel_type = "Petrol"

    #Constructor method (initialize object properties)
    def __init__(self, brand, model, year):
        # Instance variables
        self.brand = brand
        self.model = model
        self.year = year
        self.is_running = False

    # Method to start the car
    def start(self):
        if not self.is_running:
            print(f"The {self.year} {self.brand} {self.model} is now running.")
            self.is_running = True
        else:
            print("The car is already running.")

    # Method to stop the car
    def stop(self):
        if self.is_running:
            print(f"The {self.year} {self.brand} {self.model} has stopped.")
            self.is_running = False
        else:
            print("The car is already stopped.")

# Create instances (objects) of the 'Car' class
car1 = Car("Toyota", "Camry", 2022)
car2 = Car("Honda", "Civic", 2021)

# Accessing object attributes
print(f"{car1.brand} {car1.model} ({car1.year}) - Fuel Type: {car1.fuel_type}")

# Calling object methods
car1.start()  # Output: The 2022 Toyota Camry is now running.
car1.stop()   # Output: The 2022 Toyota Camry has stopped.

car2.start()  # Output: The 2021 Honda Civic is now running.
car2.stop()   # Output: The 2021 Honda Civic has stopped.