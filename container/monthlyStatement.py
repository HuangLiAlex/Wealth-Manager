class MonthlyStatement(object):

    def __init__(self, str_bank_name, dt_month_year, df_txn):
        self.str_bank_name = str_bank_name
        self.dt_month_year = dt_month_year
        self.df_txn = df_txn

