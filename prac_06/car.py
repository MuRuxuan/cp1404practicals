class Car:
    """Represent a Car object."""

    def __init__(self, name="", fuel=0):
        """Initialise a Car instance"""
        self.name = name
        self.fuel = fuel
        self.odometer = 0

    def add(self, amount):
        """Add fuel to the car"""
        self.fuel += amount

    def drive(self, distance):
        """Drive the car a given distance."""

        if distance > self.fuel:
            distance = self.fuel
        self.fuel -= distance
        self.odometer += distance
        return distance

    def __str__(self):
        """Return a string representation of the Car object."""
        return f"{self.name}, fuel={self.fuel}, odometer={self.odometer}"