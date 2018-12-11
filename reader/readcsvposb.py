# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 21:04:45 2018

@author: AlexL
"""
import pandas as pd


class ReadCsvPosb:

    col_to_del = ['Reference', 'Transaction Ref1', 'Transaction Ref2', 'Transaction Ref3']
    HEADER_ROWS = 16

    # file = r'csv\posb_2.csv'

    def read(self, sCsvFilePath):
        df = pd.read_csv(sCsvFilePath, index_col=False, skiprows=self.HEADER_ROWS, skip_blank_lines=True)

        """ remove redundant information """
        df['Transaction Ref'] = df['Transaction Ref1'].map(str) + ' ' + df['Transaction Ref2'].map(str)
        df.drop(self.col_to_del, axis=1, inplace=True)
        df = df.fillna('')

        df.columns = ["Date", "Dr", "Cr", "Description"]
        df.index.name = "id"

        columnsTitles=["Date", "Description", "Dr", "Cr"]
        df = df.reindex(columns=columnsTitles)

        df["Date"] = pd.to_datetime(df["Date"], format="%d %b %Y")
        df["Date"] = df["Date"].dt.strftime("%d/%m/%Y")

        return df

        # """ save into data """
        # table_name = "Journal"

        # db.drop_table(table_name)
        # db.create_table(table_name)

        # for index in reversed(df.index):
        #     date = df.loc[index, 'Transaction Date']
        #     description = df.loc[index, 'Transaction Ref']
        #     debit = df.loc[index, 'Debit Amount']
        #     credit = df.loc[index, 'Credit Amount']
        #
        #     date = common.datetime_transform("POSB", date)
        #
        #     db.add_transaction(table_name, date, description, debit, credit)
        #
        # table = db.display_table(pd, table_name)

        # print(table)


