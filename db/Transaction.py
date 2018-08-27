# Transaction class

from schema.DBManager import DBManager

class Transaction(object):
    """docstring for Transaction"""
    def __init__(self):
        super(Transaction, self).__init__()
        # self.txid = txid
        
    def __str__ (self):
        return "txid(txid='%s')" % self.txid

    def create(self, tx):
        resulf = False
        db = None

        try:
            db = DBManager()
            db = db.get_db()
            db.query("INSERT INTO transactions (txid, block, amount, tx_to, tx_from, age\
                ) VALUES(tx['txid'], tx['block'], tx['amount'], tx['tx_to'], tx['tx_from'], tx['age'])")

        except Exception as error:
            print("Could not create tx", error)

        finally:
            db.close()