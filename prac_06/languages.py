"""
CP1404/CP5632 Practical 06
Languages Client Program
Demonstrates the use of the ProgrammingLanguage class.
"""

from programming_language import ProgrammingLanguage


def main():
    """Demo test code for ProgrammingLanguage class."""
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    print(python)

    languages = [python, ruby, visual_basic]

    print("\nThe dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)

main()