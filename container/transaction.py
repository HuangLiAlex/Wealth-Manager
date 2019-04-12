class Transaction(object):

    def __init__(self, n_id, dt_date, str_txn_name, str_txn_type, n_amount ):
        self.n_id = n_id
        self.dt_date = dt_date
        self.str_txn_name = str_txn_name
        self.str_txn_type = str_txn_type
        self.n_amount = n_amount

