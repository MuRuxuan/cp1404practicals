"""
Estimated time: 3 hours
CP1404/CP5632 Practical - Project Management Program

This program manages a list of projects. Users can load and save project
data from text files, display projects grouped by completion status,
filter projects by start date, add new projects, update existing projects,
and quit with an optional save. All interactions match the provided example.
"""

from project import Project
import datetime
from operator import attrgetter

DATE_FORMAT = "%d/%m/%Y"
DEFAULT_FILENAME = "projects.txt"
HEADER = "Name\tStart Date\tPriority\tCost Estimate\tCompletion\n"

MIN_PRIORITY = 0
MAX_PRIORITY = 10
MIN_COMPLETION = 0
MAX_COMPLETION = 100


def main():
    """Coordinate the execution of the project management program."""
    print("Welcome to Pythonic Project Management")
    projects = load_projects(DEFAULT_FILENAME)
    print(f"Loaded {len(projects)} projects from {DEFAULT_FILENAME}")

    menu_text = (
        "- (L)oad projects\n"
        "- (S)ave projects\n"
        "- (D)isplay projects\n"
        "- (F)ilter projects by date\n"
        "- (A)dd new project\n"
        "- (U)pdate project\n"
        "- (Q)uit"
    )

    choice = ""
    while choice != "Q":
        print(menu_text)
        choice = input(">>> ").strip().upper()

        if choice == "L":
            handle_load(projects)
        elif choice == "S":
            handle_save(projects)
        elif choice == "D":
            display_projects(projects)
        elif choice == "F":
            filter_projects(projects)
        elif choice == "A":
            add_project(projects)
        elif choice == "U":
            update_project(projects)
        elif choice == "Q":
            handle_quit(projects)
        else:
            print("Invalid choice. Please try again.")


# ========== File Handling ==========

def handle_load(projects):
    """Load project data from a user-specified filename."""
    filename = input("Filename: ").strip()
    if filename:
        loaded = load_projects(filename)
        projects.clear()
        projects.extend(loaded)
        print(f"Loaded {len(projects)} projects from {filename}")


def handle_save(projects):
    """Save project data to a user-specified filename."""
    filename = input("Filename: ").strip()
    if filename:
        save_projects(projects, filename)


def load_projects(filename):
    """Load project data from a tab-separated text file."""
    projects = []
    try:
        with open(filename, "r", encoding="utf-8") as file:
            file.readline()  # discard header
            for line in file:
                if line.strip():
                    name, date_str, priority, cost, completion = line.strip().split("\t")
                    start_date = datetime.datetime.strptime(date_str, DATE_FORMAT).date()
                    cost_value = float(cost.replace("$", "").strip())
                    projects.append(
                        Project(name, start_date, int(priority), cost_value, int(completion))
                    )
    except FileNotFoundError:
        print(f"File {filename} not found. Starting with empty project list.")
    return projects


def save_projects(projects, filename):
    """Save project data in tab-separated format to the specified file."""
    with open(filename, "w", encoding="utf-8") as file:
        file.write(HEADER)
        for project in projects:
            file.write(
                f"{project.name}\t"
                f"{project.start_date.strftime(DATE_FORMAT)}\t"
                f"{project.priority}\t"
                f"${project.cost_estimate:.2f}\t"
                f"{project.completion_percentage}\n"
            )
    print(f"Saved {len(projects)} projects to {filename}")


# ========== Display ==========

def display_projects(projects):
    """Display incomplete and completed projects in separate sorted lists."""
    incomplete_projects = sorted(
        [p for p in projects if not p.is_complete()],
        key=attrgetter("priority")
    )
    completed_projects = sorted(
        [p for p in projects if p.is_complete()],
        key=attrgetter("priority")
    )

    print("\nIncomplete projects: ")
    for project in incomplete_projects:
        print(f"  {project}")

    print("Completed projects: ")
    for project in completed_projects:
        print(f"  {project}")


# ========== Filtering ==========

def filter_projects(projects):
    """Prompt for a date and display all projects starting after that date."""
    date_str = input("Show projects that start after date (dd/mm/yy): ").strip()
    try:
        filter_date = datetime.datetime.strptime(date_str, DATE_FORMAT).date()
    except ValueError:
        print("Invalid date format.")
        return

    filtered = [p for p in projects if p.start_date > filter_date]
    filtered.sort(key=attrgetter("start_date"))

    for project in filtered:
        print(project)


# ========== Add Project ==========

def add_project(projects):
    """Add a new project using validated user input."""
    print("Let's add a new project")

    name = get_non_empty_string("Name: ")

    start_date = get_valid_date("Start date (dd/mm/yy): ")

    priority = get_valid_int("Priority: ", MIN_PRIORITY, MAX_PRIORITY)

    cost_str = get_non_empty_string("Cost estimate: $")
    cost_value = get_valid_float(cost_str)

    completion = get_valid_int("Percent complete: ", MIN_COMPLETION, MAX_COMPLETION)

    projects.append(Project(name, start_date, priority, cost_value, completion))


# ========== Update Project ==========

def update_project(projects):
    """Update an existing project's completion percentage and/or priority."""
    for index, project in enumerate(projects):
        print(f"{index} {project}")

    index = get_valid_int("Project choice: ", 0, len(projects) - 1)
    project = projects[index]
    print(project)

    new_percentage = input("New Percentage: ").strip()
    if new_percentage:
        project.completion_percentage = get_valid_int(
            new_percentage, MIN_COMPLETION, MAX_COMPLETION
        )

    new_priority = input("New Priority: ").strip()
    if new_priority:
        project.priority = get_valid_int(new_priority, MIN_PRIORITY, MAX_PRIORITY)


# ========== Quit ==========

def handle_quit(projects):
    """Handle program exit, offering to save data to the default file."""
    answer = input(f"Would you like to save to {DEFAULT_FILENAME}? ").strip().lower()
    if "no" not in answer:
        save_projects(projects, DEFAULT_FILENAME)
    print("Thank you for using custom-built project management software.")


# ========== Input Validation Helpers ==========

def get_non_empty_string(prompt):
    """Return a non-empty user input string."""
    text = input(prompt).strip()
    while not text:
        print("Input cannot be empty.")
        text = input(prompt).strip()
    return text


def get_valid_date(prompt):
    """Return a valid date parsed using DATE_FORMAT."""
    date_str = input(prompt).strip()
    while True:
        try:
            return datetime.datetime.strptime(date_str, DATE_FORMAT).date()
        except ValueError:
            print("Invalid date format. Use dd/mm/yyyy.")
            date_str = input(prompt).strip()


def get_valid_int(prompt_or_value, minimum, maximum):
    """
    Return a valid integer within a specific range.
    Accepts either a prompt string (normal use) or a raw value string (update mode).
    """
    while True:
        try:
            value = int(prompt_or_value)
            if minimum <= value <= maximum:
                return value
            print(f"Value must be between {minimum} and {maximum}.")
        except ValueError:
            print("Invalid integer.")
        prompt_or_value = input(f"Enter a number between {minimum} and {maximum}: ").strip()


def get_valid_float(value_str):
    """Return a valid floating-point number from the provided string."""
    while True:
        try:
            return float(value_str)
        except ValueError:
            print("Invalid number format.")
            value_str = input("Please enter a valid number: ").strip()


main()
