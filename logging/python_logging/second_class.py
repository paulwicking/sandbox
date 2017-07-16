"""A second class for package level logging example.

From http://www.patricksoftwareblog.com/python-logging-tutorial/
"""
import logging


class SecondClass(object):
    """This class causes log entries for "system".
    """

    def __init__(self):
        """system is disabled by default.
        """
        self.enabled = False
        self.logger = logging.getLogger(__name__)

    def enable_system(self):
        """Enable the system.
        """
        self.enabled = True
        self.logger.warning('Enabling system.')
        self.logger.info('Still enabling system.')

    def disable_system(self):
        """Disable the system.
        """
        self.enabled = False
        self.logger.warning('Disabling system.')
        self.logger.info('Still disabling system.')
