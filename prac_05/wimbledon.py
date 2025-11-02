"""
wimbledon
Estimate: 35 minutes
Actual:   40 minutes
"""
import csv

INDEX_FOR_CHAMPION = 1
INDEX_FOR_COUNTRY = 2
FILENAME = "wimbledon.csv"

def main():
    """Main function to coordinate data extraction and display."""
    data = read_csv_file(FILENAME)
    champions, countries = process_data(data)
    display_results(champions, countries)


def read_csv_file(filename):
    """Read CSV file using csv module for robust parsing, skip header."""
    try:
        with open(filename, "r", encoding="utf-8-sig") as file:
            reader = csv.reader(file)
            next(reader)
            return list(reader)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        exit(1)
    except Exception as e:
        print(f"Error reading file: {str(e)}")
        exit(1)


def process_data(data):
    """Process raw data to count champions and collect countries."""
    champion_wins = {}
    countries = set()

    for row in data:
        champion = row[INDEX_FOR_CHAMPION]
        country = row[INDEX_FOR_COUNTRY]

        countries.add(country)

        champion_wins[champion] = champion_wins.get(champion, 0) + 1

    sorted_countries = sorted(countries)
    return champion_wins, sorted_countries


def display_results(champions, countries):
    """Display champions with their win counts and sorted countries."""
    print("Wimbledon Champions:")
    for champion, wins in champions.items():
        print(f"{champion}: {wins} win(s)")

    print(f"\nThese {len(countries)} countries have won Wimbledon:")
    print(", ".join(countries))

main()