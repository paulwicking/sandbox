"""Module runner.
"""
from python_logging.first_class import FirstClass


number = FirstClass()
number.increment_number()
number.increment_number()
print(f'Current number: { number.current_number }')
number.clear_number()
print(f'Current number: { number.current_number }')

