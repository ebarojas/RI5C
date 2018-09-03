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
            # This line doesn't work - need to input the text.
            # This needs binding with object and rest of shite
            db.query("INSERT INTO transactions (txid, block, value, tx_to, tx_from, timestamp) \
                VALUES (:txid, :block, :value, :tx_to, :tx_from, :timestamp)", \
                txid=tx['txid'], block=tx['block'], value=tx['value'], tx_to=tx['tx_to'], \
                tx_from=tx['tx_from'], timestamp=tx['timestamp'])

        except Exception as error:
            print("Could not create tx", error)

        finally:
            db.close()