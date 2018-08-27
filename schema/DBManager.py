# Database manager

from settings import DATABASE_URL
import records

class DBManager(object):
    """docstring for DBManager"""
    def __init__(self):
        super(DBManager, self).__init__()
        self.db = records.Database(DATABASE_URL)
        # self.model = self.db


    def create_tx_table(self):
        self.db.query('CREATE TABLE transactions (id SERIAL PRIMARY KEY, \
            txid text, \
            block text, \
            amount text, \
            tx_to text, \
            tx_from text, \
            age text\
        )')

    def drop_table(self, table):
        db.query("DROP TABLE 'table' CASCADE")

    def get_db(self):
        return self.db

    def close(self):
        self.db.close()
