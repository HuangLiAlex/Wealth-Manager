# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 21:04:45 2018

@author: AlexL
"""
import pandas as pd


class ReadCsvPosb:
    col_to_del = ['Reference', 'Transaction Ref1', 'Transaction Ref2', 'Transaction Ref3']
    HEADER_ROWS = 1

    def read(self, csv_file_path):
        # col name must follow title sequence in csv file
        col_names = ["Transaction Date", "Reference", "Debit Amount", "Credit Amount", "Transaction Ref1",
                     'Transaction Ref2', 'Transaction Ref3']

        df = pd.read_csv(csv_file_path,
                         index_col=False,
                         skiprows=self.HEADER_ROWS,
                         names=col_names)

        # remove blank lines
        df.dropna(how='all', inplace=True)
        df = df.fillna('')

        # Combine col
        df['Transaction Ref'] = df['Reference'].map(str) + ' ' + \
                                df['Transaction Ref1'].map(str) + ' ' + \
                                df['Transaction Ref2'].map(str)

        # Remove col
        df.drop(self.col_to_del, axis=1, inplace=True)
        # df = df.fillna('')

        # Rename col: follow original sequence
        # ['Transaction Date', 'Debit Amount', 'Credit Amount', 'Transaction Ref']
        df.columns = ["Date", "Dr", "Cr", "Description"]
        # df.index.name = "id"

        # Re-index col
        column_titles = ["Date", "Description", "Dr", "Cr"]
        df = df.reindex(columns=column_titles)

        # Change date format
        df["Date"] = pd.to_datetime(df["Date"], format="%d-%b-%y")

        # Sort order by Date
        df = df.sort_values(by="Date")
        df = df.reset_index(drop=True)

        # Add Category col
        df["Category"] = "Uncategorised"

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


