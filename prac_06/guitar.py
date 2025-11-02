"""
CP1404/CP5632 Practical 06
Guitar Class
Represents a guitar with attributes for name, year, and cost.
"""

CURRENT_YEAR = 2022


class Guitar:
    """Represent a Guitar object."""

    def __init__(self, name="", year=0, cost=0):
        """Initialise a Guitar instance"""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a formatted string representation of the Guitar object."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        """Calculate the age of the guitar"""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Check if the guitar is vintage (50+ years old)"""
        return self.get_age() >= 50