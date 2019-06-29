import csv

import numpy as np


class Report:

    def gen_report(self, df, output_filename):

        cr_category_list = []
        dr_category_list = []

        for category in df["Category"]:

            if category not in cr_category_list and category not in dr_category_list:
                df_category = df.loc[df["Category"] == category]
                if self.is_crdit(df_category):
                    cr_category_list.append(category)
                else:
                    dr_category_list.append(category)

        print("cr_category_list")
        print(cr_category_list)
        print("dr_category_list")
        print(dr_category_list)


        # with open(output_filename, "w") as csv_file:
        #     for category in category_list:
        #         df_category = df.loc[df["Category"] == category]
        #
        #         # if Cr side is not empty
        #         if self.is_crdit(df_category):
        #             df_category.to_csv(output_filename, mode='a', header=False)
        #
        #     for category in category_list:
        #         df_category = df.loc[df["Category"] == category]
        #
        #         # if Dr side is not empty
        #         if not self.is_crdit(df_category):
        #             df_category.to_csv(output_filename, mode='a', header=False)
        #
        # csv_file.close()

    def is_crdit(self, df_category):
        return not df_category["Cr"].replace(' ', np.nan).isnull().any()
