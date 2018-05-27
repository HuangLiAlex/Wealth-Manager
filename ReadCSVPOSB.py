# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 21:04:45 2018

@author: AlexL
"""
import pandas as pd

""" define constants """
col_to_del = ['Reference', 'Transaction Ref1', 'Transaction Ref2','Transaction Ref3']
HEADER_ROWS = 16

""" define variables """

file = r'csv\posb_2.csv'

""" read csv file """
df = pd.read_csv(file, index_col=False, skiprows=HEADER_ROWS, skip_blank_lines=True)

""" remove redundant information """
df['Transaction Ref'] = df['Transaction Ref1'].map(str) + ' ' + df['Transaction Ref2'].map(str)
df.drop(col_to_del, axis=1, inplace=True)
df = df.fillna('')


print(df)