import pytest 
from libary import calculateDaysLate,calculateFine
#testing data
assert calculateDaysLate("01/11/26","03/11/26") == 2 