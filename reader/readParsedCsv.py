# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 21:04:45 2018

@author: AlexL
"""
import pandas as pd


class ReadParsedCsv:

    @staticmethod
    def read(csv_file_path):
        column_names = ["Date", "Description", "Dr", "Cr", "Category"]
        df = pd.read_csv(csv_file_path, names=column_names, skiprows=1)

        # df = df.fillna('')

        # df.columns = ["id", "Date", "Description", "Dr", "Cr", "Category"]
        # df.index.name = "id"

        # df["Date"] = pd.to_datetime(df["Date"], format="%d-%b-%y")

        return df


