"""single-file-app.py: logging in a Single File Application example.

From http://www.patricksoftwareblog.com/python-logging-tutorial/.
"""
import logging


class FirstClass(object):
    """FirstClass is a class containing logged number counting.
    """

    def __init__(self):
        """Initialize current_number to 0 for instantiated objects.
        """
        self.current_number = 0

        #  Create the Logger
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)

        #  Create handler for logging to file
        logger_handler = logging.FileHandler('python_logging.log')
        logger_handler.setLevel(logging.INFO)

        #  Create formatter for formatting log messages
        logger_formatter = logging.Formatter(fmt='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        #  Add formatter to handler
        logger_handler.setFormatter(logger_formatter)

        #  Add Handler to Logger
        self.logger.addHandler(logger_handler)
        self.logger.info('logger() configuration complete.')

    def increment_number(self):
        """Increments current_number by 1.
        """
        self.current_number += 1
        self.logger.warning('Incrementing number.')
        self.logger.info('Still incrementing number.')

    def decrement_number(self):
        """Decrements current_number by 1.
        """
        self.current_number -= 1

    def clear_number(self):
        """Reset current_number to 0.
        """
        self.current_number = 0
        self.logger.warning('Clearing number.')
        self.logger.info('Still clearing number.')

number = FirstClass()
number.increment_number()
number.increment_number()
print(f"Current number: { number.current_number }.")
number.clear_number()
print(f"Current number: { number.current_number }.")

