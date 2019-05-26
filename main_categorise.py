from tkinter import Tk
from tkinter.filedialog import askopenfilename

from container.bankStatement import BankStatement
from reader.readParsedCsv import ReadParsedCsv
from writer.writecsv import WriteCsv
from util.common import combine

if __name__ == '__main__':

    Tk().withdraw()
    # show an "Open" dialog box and return the path to the selected file
    filename = askopenfilename(initialdir="D:\git\Wealth-Manager\csv/")

    if filename is "":
        exit("No CSV file is chosen!")

    writer = WriteCsv()

    # df_parsed = ReadParsedCsv.read("csv\output_posb.csv")
    # writer.write(df_parsed, "csv\output_parsed.csv")

    # df_combined = combine(df_ocbc, df_posb)
    # writer.write(df_combined, "csv\output_combined.csv")

    ######
    # manipulating transactions
    # manually add transaction categories

    # read manipulated csv file
    # save into monthly statement for summarising


