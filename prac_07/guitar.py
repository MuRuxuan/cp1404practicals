class Guitar:
    """Represents a guitar with attributes for name, manufacturing year, and cost.

    Provides methods to calculate age, determine vintage status, and compare
    guitars by manufacturing year.
    """
    # Constants
    CURRENT_YEAR = 2023
    VINTAGE_AGE_THRESHOLD = 50

    def __init__(self, name="", year=0, cost=0.0):
        """Initialize a Guitar instance with name, year, and cost."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return formatted string representation of the guitar."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def __lt__(self, other):
        """Compare guitars by manufacturing year for sorting."""
        return self.year < other.year

    def get_age(self):
        """Calculate the current age of the guitar."""
        return self.CURRENT_YEAR - self.year

    def is_vintage(self):
        """Determine if the guitar qualifies as vintage."""
        return self.get_age() >= self.VINTAGE_AGE_THRESHOLD