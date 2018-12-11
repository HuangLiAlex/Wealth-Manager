from data.bankstatement import BankStatement
from writer.writecsv import WriteCsv

if __name__ == '__main__':
    writer = WriteCsv()

    bs = BankStatement("OCBC", "csv\TransactionHistory_2.csv")

    df = bs.getBankStatement()

    writer.write(df, "csv\output_ocbc.csv")

    bs = BankStatement("POSB", "csv\posb_2.csv")

    df = bs.getBankStatement()

    writer.write(df, "csv\output_posb.csv")
