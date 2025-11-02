# CP1404 Practical 06 Reflection

## 1. What did you learn about classes in this practical?
In this practical, I learned how to design and implement classes that encapsulate both data (attributes) and behavior (methods) — a core concept of object-oriented programming. Key takeaways include:
- How to define a class with an `__init__` constructor to initialize attributes (including setting default values)
- The importance of the `__str__` method for creating human-readable string representations of objects
- How to create methods that use an object's internal state (e.g., `is_vintage()` using `get_age()` in the Guitar class) instead of relying on external data
- How to use class instances in collections (like lists) and iterate over them, which simplifies managing multiple related objects

## 2. What was the most challenging part of this practical?
The most challenging part was ensuring the string formatting in both the `__str__` methods and the client programs (e.g., `guitars.py`) matched the required style — especially aligning text and formatting currency with commas and decimal places. For example, in `guitars.py`, I had to experiment with format specifiers like `:>20` (right-aligned with width 20) and `:10,.2f` (fixed decimal places with commas) to replicate the sample output. Another small challenge was handling edge cases in input validation (e.g., ensuring users enter valid integers for years), which required adding try-except blocks.

## 3. How did you overcome the challenges?
To overcome the formatting challenges, I referred to Python's string formatting documentation and tested small snippets of code in isolation (e.g., testing `f"{guitar.name:>20}"` with different guitar names to check alignment). For input validation, I used while loops with try-except blocks to repeatedly prompt the user until they entered valid data — this ensured the program didn't crash from invalid inputs. I also found that testing methods incrementally (e.g., testing `get_age()` before `is_vintage()` in `guitar_test.py`) helped catch errors early and made debugging easier.

## 4. What would you do differently next time?
Next time, I would:
- Start by writing more detailed test cases before implementing class methods (e.g., testing edge cases like a guitar from the current year or a programming language with unknown typing)
- Add more comments to complex methods (e.g., explaining the logic of `drive()` in the Car class, which calculates actual distance driven based on fuel) to improve readability
- Experiment with additional class features, like class variables (beyond `CURRENT_YEAR` in Guitar) or inheritance, to deepen my understanding of OOP

## 5. How does this practical relate to real-world programming?
This practical directly relates to real-world programming because classes are used to model real-world objects and concepts (e.g., cars, guitars, programming languages) in software. For example:
- A car rental app might use a `Car` class to track each vehicle's fuel, mileage, and name
- A music store inventory system could use a `Guitar` class to manage product details like name, year, and cost
- The `ProgrammingLanguage` class demonstrates how to model abstract concepts (like programming languages) with specific attributes and behaviors, which is common in tools that analyze or compare software technologies

By learning to create reusable, well-structured classes, I'm building skills that apply to developing modular, maintainable software — a key requirement in professional programming.