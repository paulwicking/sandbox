from os import path, remove
import logging
import logging.config
import json

from .first_class import FirstClass
from .second_class import SecondClass


#  Delete existing log file
if path.isfile("logs/python_logging.log"):
    remove("logs/python_logging.log")

#  Configure logging based on config file
with open("python_logging_config.json", 'r') as logging_config_file:
    config_dict = json.load(logging_config_file)
logging.config.dictConfig(config_dict)

#  Log that the logger is configured
logger = logging.getLogger(__name__)
logger.info('logger() configuration complete.')
