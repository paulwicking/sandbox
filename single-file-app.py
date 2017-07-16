"""single-file-app.py: logging in a Single File Application example.

From http://www.patricksoftwareblog.com/python-logging-tutorial/.
"""


class FirstClass(object):
    """FirstClass is a class containing nothing but number counting.
    """
    def __init__(self):
        """Initialize current_number to 0 for instantiated objects.
        """
        self.current_number = 0

    def increment_number(self):
        """Increments current_number by 1.
        """
        self.current_number += 1

    def decrement_number(self):
        """Decrements current_number by 1.
        """
        self.current_number -= 1

    def clear_number(self):
        """Reset current_number to 0.
        """
        self.current_number = 0

number = FirstClass()
number.increment_number()
number.increment_number()
print(f"Current number: { number.current_number }.")
number.clear_number()
print(f"Current number: { number.current_number }.")

