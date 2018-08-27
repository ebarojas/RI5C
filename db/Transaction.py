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
            db.query("INSERT INTO transactions (txid, block, amount, tx_to, tx_from, age) \
                VALUES (:txid, :block, :amount, :tx_to, :tx_from, :age)", \
                txid=tx['txid'], block=tx['block'], amount=tx['amount'], tx_to=tx['tx_to'], \
                tx_from=tx['tx_from'], age=tx['age'])

        except Exception as error:
            print("Could not create tx", error)

        finally:
            db.close()