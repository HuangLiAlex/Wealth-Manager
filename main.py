from container.bankStatement import BankStatement
from writer.writecsv import WriteCsv
from util.common import combine

if __name__ == '__main__':
    writer = WriteCsv()

    bs = BankStatement("OCBC", "csv\ocbc\ocbc_12_17.csv")

    df_ocbc = bs.get_bank_statement()

    # writer.write(df1, "csv\output_ocbc.csv")

    bs = BankStatement("POSB", "csv\posb\posb_12_17.csv")

    df_posb = bs.get_bank_statement()

    # writer.write(df2, "csv\output_posb.csv")

    df_combined = combine(df_ocbc, df_posb)

    writer.write(df_combined, "csv\output_combined.csv")

    # manipulating transactions
    # manually add transaction categories

    # read manipulated csv file
    # save into monthly statement for summarising


