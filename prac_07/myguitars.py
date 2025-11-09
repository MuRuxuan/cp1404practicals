from guitar import Guitar


def main():
    """Manage guitar collection by loading, displaying, adding, and saving guitars."""
    # Constants
    GUITARS_FILENAME = 'guitars.csv'

    # Load and display existing guitars
    guitars = load_guitars(GUITARS_FILENAME)
    print(f"Loaded {len(guitars)} guitars from {GUITARS_FILENAME}")

    # Sort guitars by year
    guitars.sort()

    # Display all guitars with vintage status
    display_guitars(guitars)

    # Add new guitars
    add_new_guitars(guitars)

    # Save updated collection
    save_guitars(guitars, GUITARS_FILENAME)
    print(f"Saved {len(guitars)} guitars to {GUITARS_FILENAME}")


def load_guitars(filename):
    """Load guitar data from a CSV file."""
    guitars = []
    try:
        with open(filename, 'r') as in_file:
            for line in in_file:
                name, year_str, cost_str = line.strip().split(',')
                # Validate and convert numeric values
                if not year_str.isdigit():
                    print(f"Skipping invalid year: {year_str}")
                    continue
                year = int(year_str)

                try:
                    cost = float(cost_str)
                except ValueError:
                    print(f"Skipping invalid cost: {cost_str}")
                    continue

                guitars.append(Guitar(name, year, cost))
    except FileNotFoundError:
        print(f"No existing file {filename} found. Starting with empty collection.")
    return guitars


def display_guitars(guitars):
    """Display a list of guitars with their details and vintage status."""
    print("\nGuitars in collection:")
    for index, guitar in enumerate(guitars, 1):
        vintage_label = " (vintage)" if guitar.is_vintage() else ""
        print(f"{index}. {guitar}{vintage_label}")


def add_new_guitars(guitars):
    """Allow user to add new guitars to the collection."""
    print("\nAdd new guitars to your collection:")
    name = input("Enter guitar name (blank to finish): ").strip()

    while name:
        # Validate year input
        year = get_validated_integer("Enter manufacturing year: ", 1900, 2023)

        # Validate cost input
        cost = get_validated_float("Enter cost: $", 0, 100000)

        # Add new guitar
        new_guitar = Guitar(name, year, cost)
        guitars.append(new_guitar)
        print(f"Added: {new_guitar}")

        # Get next name
        name = input("Enter guitar name (blank to finish): ").strip()


def get_validated_integer(prompt, min_value, max_value):
    """Get and validate integer input within a specified range."""
    while True:
        try:
            value = int(input(prompt).strip())
            if min_value <= value <= max_value:
                return value
            print(f"Please enter a number between {min_value} and {max_value}")
        except ValueError:
            print("Please enter a valid integer")


def get_validated_float(prompt, min_value, max_value):
    """Get and validate float input within a specified range."""
    while True:
        try:
            value = float(input(prompt).strip())
            if min_value <= value <= max_value:
                return value
            print(f"Please enter a number between {min_value} and {max_value}")
        except ValueError:
            print("Please enter a valid number")


def save_guitars(guitars, filename):
    """Save guitar collection to a CSV file."""
    with open(filename, 'w') as out_file:
        for guitar in guitars:
            print(f"{guitar.name},{guitar.year},{guitar.cost}", file=out_file)


main()