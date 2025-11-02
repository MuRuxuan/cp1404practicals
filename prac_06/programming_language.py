"""
CP1404/CP5632 Practical 06
ProgrammingLanguage Class
Represents a programming language with relevant attributes and methods.
"""


class ProgrammingLanguage:
    """Represent a Programming Language object."""

    def __init__(self, name="", typing="", reflection=False, year=0):
        """Initialise a ProgrammingLanguage instance."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Check if the programming language uses dynamic typing."""
        return self.typing == "Dynamic"

    def __str__(self):
        """Return a string representation of the ProgrammingLanguage object."""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"