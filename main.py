from reader.ReaderFactory import ReaderFactory
from util import Storage as db
import pandas as pd
import sys

# get a file name as input
files = sys.argv[1:]

# call reader to read the file and save into database
for filename in files:
    df = None
    filename = "csv/" + filename

    oReaderFactory = ReaderFactory()

    if "OCBC" in filename:
        oReader = oReaderFactory.get_reader("OCBC")
        df = oReader.read(filename)

    elif "POSB" in filename:
        oReader = oReaderFactory.get_reader("POSB")
        df = oReader.read(filename)

    table_name = "Journal"

    db.drop_table(table_name)
    db.create_table(table_name)

    for index in reversed(df.index):
        date = df.loc[index, 'Date']
        description = df.loc[index, 'Description']
        debit = df.loc[index, 'Dr']
        credit = df.loc[index, 'Cr']

        # date = common.datetime_transform("OCBC", date)

        db.add_transaction(table_name, date, description, debit, credit)

    table = db.display_table(pd, table_name)

    table.to_csv('output\out.csv')
