# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 21:04:45 2018

@author: AlexL
"""
import pandas as pd
import Storage as db

""" define constants """
col_to_del = ['Value date']
HEADER_ROWS = 5
list_del_idx = []


""" define variables """
file = 'csv\TransactionHistory_2.csv'

""" read csv file """
df = pd.read_csv(file, index_col=False, skiprows=HEADER_ROWS)

""" remove redundant information """
df.drop(col_to_del, axis=1, inplace=True)
df = df.fillna('')

""" combine description """
for index, row in df.iterrows():
    if row['Transaction date']  is '':
        df.iloc[index-1]['Description'] += ' ' + row['Description']
        list_del_idx.append(index)
        
df.drop(labels=list_del_idx, axis=0, inplace=True)

df.columns = ["Date", "Description", "Dr", "Cr"]
df.index.name = "id"
""" output to excel file """
#print(df)
#df.to_csv('csv\output.csv')

""" save into database """
db.drop_table("Journal")
db.create_table("Journal")
db.add_transaction("Journal",               \
                   0,                       \
                   df.loc[0,'Date'],        \
                   df.loc[0,'Description'], \
                   df.loc[0,'Dr'],          \
                   df.loc[0,'Cr'])

#db.add_transaction("Journal", "20180401", "dummy_txn", 10, None)
table = db.display_table(pd, "Journal")
print (table)