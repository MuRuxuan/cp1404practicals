"""
CP1404/CP5632 Practical 06
Used Cars Program
This program demonstrates the use of the Car class with names.
"""

from car import Car


def main():
    """Demo test code to show how to use Car class with names."""
    limo = Car("Limo", 100)

    limo.add(20)

    print(f"Fuel in limo after adding: {limo.fuel}")

    distance_driven = limo.drive(115)
    print(f"Distance driven by limo: {distance_driven} km")

    print(limo)

    toyota = Car("Toyota Corolla", 50)
    honda = Car("Honda Civic", 75)

    toyota.drive(30)
    honda.drive(50)

    print("\nAll Car Objects:")
    print(toyota)
    print(honda)



main()