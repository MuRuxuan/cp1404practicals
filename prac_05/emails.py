"""
Map email addresses to usernames with format validation.
Validate email contains "@", extract default name from email (before "@", split by "."),
and allow user to override the default name.
"""
def main():
    """Coordinate email input, validation, name mapping, and result display."""
    email_to_names = {}
    while True:
        email = input("Email: ").strip()
        if not email:
            break
        if not is_valid_email(email):
            print("Invalid email format. Must contain '@'.")
            continue
        default_name = extract_name_from_email(email)
        confirmation = input(f"Is your name {default_name}? (Y/n) ").strip().lower()
        if confirmation != '' and confirmation != 'y':
            name = input("Name: ").strip()
            while not name:
                print("Name cannot be empty.")
                name = input("Name: ").strip()
        else:
            name = default_name
        email_to_names[email] = name
    print("\nEmail to Name Mapping:")
    for email, name in email_to_names.items():
        print(f"{name} ({email})")

def extract_name_from_email(email):
    """Extract default name from email (e.g., "john.doe@example.com" → "John Doe")."""
    local_part = email.split('@')[0]
    name_parts = local_part.split('.')
    return ' '.join(part.title() for part in name_parts)

def is_valid_email(email):
    """Check if email contains "@" (basic format validation)."""
    return '@' in email and email.strip() != ''

main()