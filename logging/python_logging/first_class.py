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
        self.logger = logging.getLogger(__name__)


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
