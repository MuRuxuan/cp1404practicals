"""
Emails
Estimate: 30 minutes
Actual: 25 minutes
"""

def extract_name_from_email(email):
    """Extract the name part from the email"""
    parts = email.split('@')[0].split('.')

    name = ' '.join(part.title() for part in parts)
    return name

email_to_name = {}

while True:
    email = input("Email: ")
    if not email:
        break

    name = extract_name_from_email(email)

    confirmation = input(f"Is your name {name}? (Y/n) ").strip().lower()

    if confirmation != '' and confirmation != 'y':
        name = input("Name: ")

    email_to_name[email] = name


for email, name in email_to_name.items():
    print(f"{name} ({email})")