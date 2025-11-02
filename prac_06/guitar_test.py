"""
CP1404/CP5632 Practical 06
Guitar Test Program
Tests the Guitar class methods (get_age and is_vintage).
"""

from guitar import Guitar


def test_guitar_methods():
    """Test the get_age and is_vintage methods of the Guitar class."""
    gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
    another_guitar = Guitar("Another Guitar", 2013, 999.99)

    print(f"{gibson.name} get_age() - Expected 100. Got {gibson.get_age()}")
    print(f"{another_guitar.name} get_age() - Expected 9. Got {another_guitar.get_age()}")

    print(f"{gibson.name} is_vintage() - Expected True. Got {gibson.is_vintage()}")
    print(f"{another_guitar.name} is_vintage() - Expected False. Got {another_guitar.is_vintage()}")

    vintage_test_guitar = Guitar("Vintage Test Guitar", 1972, 1500.00)
    print(f"{vintage_test_guitar.name} is_vintage() - Expected True. Got {vintage_test_guitar.is_vintage()}")

    non_vintage_test_guitar = Guitar("Non-Vintage Test Guitar", 1973, 1499.99)
    print(f"{non_vintage_test_guitar.name} is_vintage() - Expected False. Got {non_vintage_test_guitar.is_vintage()}")


test_guitar_methods()