# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 21:04:45 2018

@author: AlexL
"""
import pandas as pd


class ReaderInterface:
    def read(self): pass


class OCBCReader(ReaderInterface):

    @staticmethod
    def read(filename):
        """ define constants """
        col_to_del = ['Value date']
        header_rows = 5
        list_del_idx = []

        """ read csv file """
        df = pd.read_csv(filename, index_col=False, skiprows=header_rows, skip_blank_lines=True)

        """ remove redundant information """
        df.drop(col_to_del, axis=1, inplace=True)
        df = df.fillna('')

        """ combine description """
        for index, row in df.iterrows():
            if row['Transaction date'] is '':
                df.iloc[index-1]['Description'] += ' ' + row['Description']
                list_del_idx.append(index)

        """ remove redundant information """
        df.drop(labels=list_del_idx, axis=0, inplace=True)

        """ rename columns """
        df.columns = ["Date", "Description", "Dr", "Cr"]
        df.index.name = "id"

        return df


class POSBReader(ReaderInterface):

    @staticmethod
    def read(filename):
        """ define constants """
        col_to_del = ['Reference', 'Transaction Ref1', 'Transaction Ref2', 'Transaction Ref3']
        header_rows = 6

        """ read csv file """
        df = pd.read_csv(filename, index_col=False, skiprows=header_rows, skip_blank_lines=True)

        """ combine description """
        df['Transaction Ref'] = df['Transaction Ref1'].map(str) + ' ' + df['Transaction Ref2'].map(str)

        """ remove redundant information """
        df.drop(df.columns[7], axis=1, inplace=True)    # remove the unnamed col
        df.drop(col_to_del, axis=1, inplace=True)
        df = df.dropna(subset=['Transaction Date'])
        df = df.fillna('')

        """ rename columns """
        df.columns = ["Date", "Dr", "Cr", "Description"]
        df.index.name = "id"

        return df
