class WriteCsv:

    def write(self, df, filename):
        if df is not None:
            df.to_csv(filename)