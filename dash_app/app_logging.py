import logging
import datetime
import os


def initialize_logger(output_dir, name):
    """
    Logger for the experiments. Log in console and saved file
    :param name: name of logger
    :param output_dir: where to save the log file
    """
    # logger
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    FILE_SUFFIX_DATE_FORMAT = "%Y%m%d%H%M%S"
    timestamp = datetime.datetime.now().strftime(FILE_SUFFIX_DATE_FORMAT)

    # create console handler and set level to info
    handler = logging.StreamHandler()
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter("'%(asctime)s %(levelname)s %(message)s'")
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    # create error file handler and set level to error
    error_file_name = timestamp + "_error.log"
    handler = logging.FileHandler(os.path.join(output_dir, 'error', error_file_name), "w",
                                  encoding=None, delay="true")
    handler.setLevel(logging.ERROR)
    formatter = logging.Formatter("'%(asctime)s %(levelname)s %(message)s'")
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    # create debug file handler and set level to debug
    all_file_name = timestamp + "_all.log"
    handler = logging.FileHandler(os.path.join(output_dir, 'info', all_file_name), "w")
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter("'%(asctime)s %(levelname)s %(message)s'")
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    return logger



