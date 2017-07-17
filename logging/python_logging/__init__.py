"""Logging example module. Provides basic logging capabilities for packages.

From http://www.patricksoftwareblog.com/python-logging-tutorial/
"""

from os import path, remove
import logging
import logging.config
import json

from .first_class import FirstClass
from .second_class import SecondClass

PACKAGE_DIRECTORY = path.dirname(path.abspath(__file__))
LOG_FILE = PACKAGE_DIRECTORY + r"/../logs/python_logging.log"


#  Delete existing log file
if path.isfile(LOG_FILE):
    remove(LOG_FILE)


#  Configure logging based on config file
with open(PACKAGE_DIRECTORY + "/../config/python_logging_config.json", 'r') as logging_config_file:
    config_dict = json.load(logging_config_file)
logging.config.dictConfig(config_dict)
#logging.basicConfig(filename=LOG_FILE)

#  Log that the logger is configured
logger = logging.getLogger(__name__)
logger.info('logger() configuration complete.')
