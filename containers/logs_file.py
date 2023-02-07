import os
import time
import logging

# store time date for error messages
def date_time():
    dt = time.strftime('[%d.%m.%Y %I:%M:%S%p]').lower()
    return dt

# config logs filename
def set_custom_log_info(filename):
    logging.basicConfig(filename=filename, level=logging.INFO)
    
    
# through the logs info into file
def report_info(e:Exception):
    try: e = str(e)
    except: e = 'Bad type'
    logging.exception(date_time()+e, exc_info=False)
    
    
# create log folder is not exists
def create_log_file(dname):
    if not os.path.exists(dname):
        os.makedirs(dname)


create_log_file('log')
log_file = 'log/errors.log' # store logs info
set_custom_log_info(log_file)