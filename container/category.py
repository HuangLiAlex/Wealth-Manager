class Category:
    name = ""
    df = None
    sum = 0

    def category(self, name, df):
        self.name = name
        self.df = df
        self.sum = self.compute_sum()

    def compute_sum(self):
        if self.df is not None:
            if not self.df["Dr"].isnull().any():
                return self.df["Dr"].astype(int).sum()
            else:
                return self.df["Cr"].astype(int).sum()
