from reader.readcsvocbc import ReadCsvOcbc
from reader.readcsvposb import ReadCsvPosb


class BankStatement:

    def __init__(self, bank, csvFilePath):
        self.bank = bank
        self.csvFilePath = csvFilePath
        self.reader = None
        self.writer = None

    def getBankStatement(self):
        if self.bank is "OCBC":
            self.reader = ReadCsvOcbc()
        elif self.bank is "POSB":
            self.reader = ReadCsvPosb()

        if self.reader is not None:
            return self.reader.read(self.csvFilePath)
