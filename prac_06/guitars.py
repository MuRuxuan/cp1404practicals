"""
CP1404/CP5632 Practical 06
Guitars Client Program
Allows user to input guitar details, stores them in a list, and displays them.
"""

from guitar import Guitar


def main():
    """Main function to handle user input and display of guitars."""
    print("My guitars!")

    guitars = []

    while True:
        name = input("Name: ")
        if not name:
            break

        while True:
            try:
                year = int(input("Year: "))
                break
            except ValueError:
                print("Please enter a valid year (integer).")

        while True:
            try:
                cost = float(input("Cost: $"))
                break
            except ValueError:
                print("Please enter a valid cost (number).")

        new_guitar = Guitar(name, year, cost)
        guitars.append(new_guitar)
        print(f"{new_guitar} added.\n")

    if guitars:
        print("\nThese are my guitars:")
        for i, guitar in enumerate(guitars, 1):
            vintage_string = " (vintage)" if guitar.is_vintage() else ""
            print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")
    else:
        print("\nNo guitars added.")


main()