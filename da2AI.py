class Car:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category
        self.available = True

class Customer:
    def __init__(self, name, interested_car):
        self.name = name
        self.interested_car = interested_car

class Dealership:
    def __init__(self, inventory):
        self.inventory = inventory
        self.revenue = 0

    def buy_car(self, customer):
        for car in self.inventory:
            if car.name == customer.interested_car.name and car.available:
                car.available = False
                self.revenue += car.price
                print(f"{customer.name} has bought {car.name} for ${car.price}")
                return True
        print(f"{customer.name} could not buy {customer.interested_car.name}")
        return False

inventory = [Car("Honda Civic", 20000, "sedan"), Car("Toyota Corolla", 22000, "sedan"), Car("Ford Mustang", 30000, "sports"), Car("Chevrolet Camaro", 35000, "sports")]
customers = [Customer("Customer1", Car("Honda Civic", 20000, "sedan")), Customer("Customer2", Car("Toyota Corolla", 22000, "sedan")), Customer("Customer3", Car("Ford Mustang", 30000, "sports"))]

dealership = Dealership(inventory)

print("Initial Inventory:")
for car in dealership.inventory:
    print(f"{car.name} - ${car.price} - {car.category}")

print("\nCustomers:")
for customer in customers:
    print(f"{customer.name} is interested in {customer.interested_car.name}")

print("\nCar sales:")
for customer in customers:
    dealership.buy_car(customer)

print(f"\nTotal revenue: ${dealership.revenue}")