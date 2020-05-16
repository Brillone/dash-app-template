# base
from db_handler.mssql.mssql_read import MSSQLTableReader

# internal
from settings import env_variables


class Reader:

    def __init__(self, writer_config, logger, env_mode):
        self.writer_config = writer_config()

        self._env_mode = env_mode

        self._logger = logger

    def read_data(self, **kwargs):
        self._logger.info('Reader - start read data')

        top = None
        table = None

        if self._env_mode in ['Development']:
            top = 'constant_val'

        self._logger.info('Reader - finished read data')

        return table
