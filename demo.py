from us_visa.logger import logging
from us_visa.exception import USVisaException
import sys

## Create a custom logger
#logging.info("Welcome to our custom logger")



## Create a custom exception
try:
    a=2/0
except Exception as e:
    raise USVisaException("Bro, Error occurred", sys, error_detail=e)
