from reader import CSV_Reader
from util import Storage as db
from util import common
import pandas as pd

# get a file name as input
files = ["csv\OCBC_APR.csv", "csv\POSB_APR.csv"]

# call reader to read the file and save into database
for filename in files:
    df = None

    if "OCBC" in filename:
        df = CSV_Reader.read_ocbc(filename)

    if "POSB" in filename:
        df = CSV_Reader.read_posb(filename)

    table_name = "Journal"

    # db.drop_table(table_name)
    db.create_table(table_name)

    for index in reversed(df.index):
        date = df.loc[index, 'Date']
        description = df.loc[index, 'Description']
        debit = df.loc[index, 'Dr']
        credit = df.loc[index, 'Cr']

        date = common.datetime_transform("OCBC", date)

        db.add_transaction(table_name, date, description, debit, credit)

    table = db.display_table(pd, table_name)
    print(table)
