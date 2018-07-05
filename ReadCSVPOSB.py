# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 21:04:45 2018

@author: AlexL
"""
import pandas as pd
import Storage as db
from util import common


""" define constants """
col_to_del = ['Reference', 'Transaction Ref1', 'Transaction Ref2', 'Transaction Ref3']
HEADER_ROWS = 16

""" define variables """
file = r'csv\posb_2.csv'

""" read csv file """
df = pd.read_csv(file, index_col=False, skiprows=HEADER_ROWS, skip_blank_lines=True)

""" remove redundant information """
df['Transaction Ref'] = df['Transaction Ref1'].map(str) + ' ' + df['Transaction Ref2'].map(str)
df.drop(col_to_del, axis=1, inplace=True)
df = df.fillna('')

""" output to excel file """
# print(df)
# df.to_csv('csv\output_posb.csv')

""" save into database """
table_name = "Journal"

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


