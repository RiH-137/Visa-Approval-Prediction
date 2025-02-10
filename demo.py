# from us_visa.logger import logging
# from us_visa.exception import USVisaException
# import sys
from us_visa.pipline.training_pipeline import TrainPipeline
## Create a custom logger
#logging.info("Welcome to our custom logger")



## Create a custom exception
# try:
#     a=2/0
# except Exception as e:
#     raise USVisaException("Bro, Error occurred", sys, error_detail=e)


## Create a custom pipeline 
obj=TrainPipeline()
obj.run_pipeline()