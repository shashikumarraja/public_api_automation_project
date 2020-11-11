"""
Create custom logger to be used in Test
"""

import logging
import os
from abc import ABCMeta
from src import global_logs_dir

ABC = ABCMeta('ABC', (object,), {'__slots__': ()}) 

class CustomLogger(ABC):
    __logger = None
        
    @staticmethod
    def getLogger(name):

        if CustomLogger.__logger is not None:
            return CustomLogger.__logger

        #logs dir to be created under the project dir
        logs_path = global_logs_dir

        # Create log directory if it does not exist
        if not os.path.exists(logs_path):
            os.mkdir(logs_path)

        # Let's create a root logger now and clear any old handlers if already
        # available
        logger = logging.getLogger(name)
        logger.setLevel(logging.DEBUG)

        if logger.handlers:
            for handler in logger.handlers[:]:
                logger.removeHandler(handler)

        # Set formatter for logging
        format_pattern = '%(asctime)s:%(levelname)s:%(filename)s:%(lineno)d:%(message)s'
        formatter = logging.Formatter(format_pattern)

        # Set INFO or above log handler
        info_handler = logging.FileHandler('{0}/info.log'.format(logs_path))
        info_handler.setLevel(logging.INFO)
        info_handler.setFormatter(formatter)

        # Set DEBUG or above log handler
        debug_handler = logging.FileHandler('{0}/debug.log'.format(logs_path))
        debug_handler.setLevel(logging.DEBUG)
        debug_handler.setFormatter(formatter)

        # Set ERROR or above log handler
        error_handler = logging.FileHandler('{0}/error.log'.format(logs_path))
        error_handler.setLevel(logging.ERROR)
        error_handler.setFormatter(formatter)

        # set console log Handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        console_handler.setFormatter(formatter)

        logger.addHandler(info_handler)
        logger.addHandler(debug_handler)
        logger.addHandler(error_handler)
        logger.addHandler(console_handler)

        # Disable verbosity for the unecessary loggers
        urllib3_logger = logging.getLogger('urllib3')
        urllib3_logger.setLevel(logging.ERROR)

        CustomLogger.__logger = logger
        return CustomLogger.__logger
