# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 21:04:45 2018

@author: AlexL
"""
import pandas as pd


class ReadCsvOcbc:

    col_to_del = ['Value date']
    HEADER_ROWS = 5
    list_del_idx = []

    # file = 'csv\TransactionHistory_2.csv'

    def read(self, sCsvFilePath):
        df = pd.read_csv(sCsvFilePath, index_col=False, skiprows=self.HEADER_ROWS)

        """ remove redundant information """
        df.drop(self.col_to_del, axis=1, inplace=True)
        df = df.fillna('')

        """ combine description """
        for index, row in df.iterrows():
            if row['Transaction date'] is '':
                df.iloc[index-1]['Description'] += ' ' + row['Description']
                self.list_del_idx.append(index)
        
        df.drop(labels=self.list_del_idx, axis=0, inplace=True)

        df.columns = ["Date", "Description", "Dr", "Cr"]
        df.index.name = "id"

        df["Date"] = pd.to_datetime(df["Date"], format="%d/%m/%Y")
        # df["Date"] = df["Date"].dt.strftime("%d/%m/%Y")

        df["Source"] = "OCBC"
        df["Category"] = "Uncategorised"

        return df

        # """ save into data """
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


