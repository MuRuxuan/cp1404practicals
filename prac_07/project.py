from datetime import datetime


class Project:
    """
    Represent a project with its basic attributes and operations.

    A project contains a name, start date, priority, cost estimate,
    and a completion percentage. It supports friendly string formatting
    and checking whether the project is complete.
    """

    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        """
        Initialize a Project instance with provided attributes.

        start_date is a datetime.date object.
        priority and completion_percentage are integers.
        cost_estimate is a float.
        """
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __str__(self):
        """Return a formatted description of the project for display."""
        return (f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, "
                f"priority {self.priority}, estimate: ${self.cost_estimate:.2f}, "
                f"completion: {self.completion_percentage}%")

    def is_complete(self):
        """Return True if the project is fully completed (100%)."""
        return self.completion_percentage == 100

    def __lt__(self, other):
        """
        Provide ordering support for sorting projects by priority.

        Lower priority value means higher urgency.
        """
        return self.priority < other.priority
