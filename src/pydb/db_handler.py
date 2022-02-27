import sqlite3 as sl
from pydb.logging.json_logger import get_logger
import os
class DBHandler:
    def __init__(self):
        self._logger = get_logger('INFO')

    def create_database(self, name):
        if not os.path.exists('/tmp/databases'):
            self._logger.info('Folder for databases does not exists.')
            os.mkdir('/tmp/databases')
            self._logger.info('Created database folder.')
        self._logger.info(f'Connecting to DB {name}')
        con = sl.connect(f'/tmp/databases/{name}.db')
        return con



if __name__ == "__main__":
    db = DBHandler()
    db.create_database('test')