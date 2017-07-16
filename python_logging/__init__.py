from os import path, remove
import logging
import logging.config

from .first_class import FirstClass
from .second_class import SecondClass

#  Delete existing log file
if path.isfile("logs/python_logging.log"):
    remove("logs/python_logging.log")

#  Create the Logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

#  Create handler for logging to file
logger_handler = logging.FileHandler('logs/python_logging.log')
logger_handler.setLevel(logging.INFO)

#  Create formatter for formatting log messages
logger_formatter = logging.Formatter(
    fmt='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

#  Add formatter to handler
logger_handler.setFormatter(logger_formatter)

#  Add Handler to Logger
logger.addHandler(logger_handler)
logger.info('logger() configuration complete.')
