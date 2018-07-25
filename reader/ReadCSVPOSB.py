# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 21:04:45 2018

@author: AlexL
"""
import pandas as pd
from util import Storage as db
from util import common


def read(filename):
    col_to_del = ['Reference', 'Transaction Ref1', 'Transaction Ref2', 'Transaction Ref3']
    # header_rows = 16
    header_rows = 0

    df = pd.read_csv(filename, index_col=False, skiprows=header_rows, skip_blank_lines=True)

    print(df)
    """ remove redundant information """
    df['Transaction Ref'] = df['Transaction Ref1'].map(str) + ' ' + df['Transaction Ref2'].map(str)
    df.drop(col_to_del, axis=1, inplace=True)
    df = df.fillna('')

    return df


def save_to_db(df, table_name):
    # db.drop_table(table_name)
    # db.create_table(table_name)

    for index in reversed(df.index):
        date = df.loc[index, 'Transaction Date']
        description = df.loc[index, 'Transaction Ref']
        debit = df.loc[index, 'Debit Amount']
        credit = df.loc[index, 'Credit Amount']

        date = common.datetime_transform("POSB", date)

        db.add_transaction(table_name, date, description, debit, credit)

    table = db.display_table(pd, table_name)
    print(table)