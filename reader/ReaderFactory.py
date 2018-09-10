from reader.Reader import *


class ReaderFactory:
    @staticmethod
    def get_reader(type):
        if type == "OCBC":
            return OCBCReader()
        if type == "POSB":
            return POSBReader()
        assert 0, "invalid reader type: " + type