# Database manager

from settings import DATABASE_URL
import records

class DBManager(object):
    """docstring for DBManager"""
    def __init__(self):
        super(DBManager, self).__init__()
        self.db = records.Database(DATABASE_URL)
        # self.model = self.db

    # TODO: Need to change age to timestamp and amount to value - this code is not very DRY.
    def create_tx_table(self):
        self.db.query('CREATE TABLE transactions (id SERIAL PRIMARY KEY, \
            txid text, \
            block text, \
            value text, \
            tx_to text, \
            tx_from text, \
            timestamp text\
        )')

    def drop_table(self, table):
        # THIS doesn't work [WIP], can't escape string adequately
        self.db.query("DROP TABLE :table CASCADE", table=table)

    def get_db(self):
        return self.db

    def close(self):
        self.db.close()
