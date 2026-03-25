class Vehicle:
    def __init__(self, name, fuel_capacity, cost_per_gallon, miles_per_gallon):
        self._name = name
        self._fuel_capacity = fuel_capacity
        self._cost_per_gallon = cost_per_gallon
        self._miles_per_gallon = miles_per_gallon

    # Getter for name
    @property
    def name(self):
        return self._name

    # Property for range (miles on full tank)
    @property
    def range(self):
        return self._fuel_capacity * self._miles_per_gallon

    # Property for cost per mile
    @property
    def cost_per_mile(self):
        return self._cost_per_gallon / self._miles_per_gallon


# Create vehicles
car = Vehicle("Car", 12, 3.50, 30)
motorcycle = Vehicle("Motorcycle", 4, 3.50, 60)
bus = Vehicle("Bus", 100, 4.00, 6)
plane = Vehicle("Plane", 5000, 5.00, 0.2)

# Put them in a list
vehicles = [car, motorcycle, bus, plane]

# Sort by cost per mile (lowest to highest)
vehicles.sort(key=lambda v: v.cost_per_mile)

# Print table
print(f"{'Name':<12} {'Range (miles)':<15} {'Cost per mile ($)':<18}")
print("-" * 45)

for v in vehicles:
    print(f"{v.name:<12} {v.range:<15.2f} {v.cost_per_mile:<18.4f}")