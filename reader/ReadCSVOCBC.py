# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 21:04:45 2018

@author: AlexL
"""
import pandas as pd
from util import Storage as db
from util import common


def read(filename):
    """ define constants """
    col_to_del = ['Value date']
    HEADER_ROWS = 5
    list_del_idx = []

    """ read csv file """
    df = pd.read_csv(filename, index_col=False, skiprows=HEADER_ROWS)

    """ remove redundant information """
    df.drop(col_to_del, axis=1, inplace=True)
    df = df.fillna('')

    """ combine description """
    for index, row in df.iterrows():
        if row['Transaction date'] is '':
            df.iloc[index-1]['Description'] += ' ' + row['Description']
            list_del_idx.append(index)

    df.drop(labels=list_del_idx, axis=0, inplace=True)

    df.columns = ["Date", "Description", "Dr", "Cr"]
    df.index.name = "id"

    return df

    """ output to excel file """
    # print(df)
    # df.to_csv('csv\output_ocbc.csv')

    """ save into database """
    # table_name = "Journal"
    #
    # db.drop_table(table_name)
    # db.create_table(table_name)
    #
    # for index in reversed(df.index):
    #     date = df.loc[index, 'Date']
    #     description = df.loc[index, 'Description']
    #     debit = df.loc[index, 'Dr']
    #     credit = df.loc[index, 'Cr']
    #
    #     date = common.datetime_transform("OCBC", date)
    #
    #     db.add_transaction(table_name, date, description, debit, credit)
    #
    # table = db.display_table(pd, table_name)
    # print(table)


