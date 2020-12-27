import inspect
import logging
import os
from datetime import datetime

import pytest

from src.commons import constants
from src.utilities.XLUtil import XLUtil


@pytest.mark.usefixtures('setup')
class TestBase(object):

    @staticmethod
    def get_user():
        file_path = constants.USERS_FILE_PATH
        return XLUtil(file_path, 'users').read_data_of_random_row()

    @staticmethod
    def logger():
        LOGFILE_PATH = os.path.join(constants.ROOT_DIR, '..', 'logs',
                                    f'{datetime.now().strftime("%Y-%m-%d")}.log')
        loggerName = inspect.stack()[1][3]
        myLogger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler(LOGFILE_PATH)
        formatter = logging.Formatter('%(asctime)s : %(levelname)s : %(filename)s : %(name)s : %(message)s')
        fileHandler.setFormatter(formatter)
        myLogger.handlers.clear()
        myLogger.addHandler(fileHandler)
        myLogger.setLevel(logging.DEBUG)
        return myLogger


if __name__ == '__main__':
    log = TestBase().logger()
    log.info('Info')
    log.debug('debug')
