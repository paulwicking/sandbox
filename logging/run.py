"""Module runner.
"""
from python_logging import FirstClass, SecondClass


MY_NUMBER = FirstClass()
MY_NUMBER.increment_number()
MY_NUMBER.increment_number()
print(f'Current number: { MY_NUMBER.current_number }')
MY_NUMBER.clear_number()
print(f'Current number: { MY_NUMBER.current_number }')

SYSTEM = SecondClass()
SYSTEM.enable_system()
SYSTEM.disable_system()
print(f'Current system configuration: { SYSTEM.enabled }')
