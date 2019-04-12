from reader.readcsvocbc import ReadCsvOcbc
from reader.readcsvposb import ReadCsvPosb


class BankStatement:

    def __init__(self, str_bank_name, f_csv_file_path):
        self.str_bank_name = str_bank_name
        self.f_csv_file_path = f_csv_file_path
        self.reader = None
        self.writer = None

    def get_bank_statement(self):
        if self.str_bank_name is "OCBC":
            self.reader = ReadCsvOcbc()
        elif self.str_bank_name is "POSB":
            self.reader = ReadCsvPosb()

        if self.reader is not None:
            return self.reader.read(self.f_csv_file_path)
