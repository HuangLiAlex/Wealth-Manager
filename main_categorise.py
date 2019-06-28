import csv
import os
import numpy as np
from tkinter import Tk
from tkinter.filedialog import askopenfilename

from reader.readParsedCsv import ReadParsedCsv
from writer.writecsv import WriteCsv

'''
    status:
    open categorized csv into dataframe
    categorize transactions with the same categorize
    manually created sample monthly report in  D:\git\Wealth-Manager\csv\working\wip\finalised_OCBC_Jan.csv
    
    TODO:
    calculate sub amount in each category
    
    write csv file by category in income statement format
    
    calculate total amount and write in monthly report format 
    
    future:
    with pop up GUI to do categorization
    gen report by one click
    
'''
if __name__ == '__main__':

    # Tk().withdraw()
    # show an "Open" dialog box and return the path to the selected file
    # file_path = askopenfilename(initialdir="D:\git\Wealth-Manager\csv/")

    file_path = "D:\git\Wealth-Manager\csv\working\wip\cated_POSB_Jan.csv"
    if file_path is "":
        exit("No CSV file is chosen!")

    # Get filename
    idx = file_path.rfind("/") + 1
    file_dir = file_path[0: idx]
    file_name = file_path[idx:]
    print("file_name = " + file_name)

    df = ReadParsedCsv.read(file_path)
    print("Data frame loading completed")

    category_list = []

    for category in df["Category"]:
        if category not in category_list:
            category_list.append(category)

    output_filename = file_path[:-4] + "_sorted2.csv"

    with open(output_filename, "w") as csv_file:
        for category in category_list:
            df_temp = df.loc[df["Category"] == category]

            # if Cr side is not empty
            if not df_temp["Cr"].replace(' ', np.nan).isnull().any():
                df_temp.to_csv(output_filename, mode='a', header=False)

        for category in category_list:
            df_temp = df.loc[df["Category"] == category]

            # if Dr side is not empty
            if not df_temp["Dr"].replace(' ', np.nan).isnull().any():
                df_temp.to_csv(output_filename, mode='a', header=False)

    csv_file.close()

    # Revenue
    # df_cat_salary       = df.loc[df["Category"] == "Salary"]
    # df_cat_transfer_in  = df.loc[df["Category"] == "Transfer In"]
    # df_cat_other_rev    = df.loc[df["Category"] == "Other Income"]

    # Fixed Expenses
    # df_cat_cpf          = df.loc[df["Category"] == "CPF"]
    # df_cat_loan         = df.loc[df["Category"] == "Loan"]
    # df_cat_rental       = df.loc[df["Category"] == "Rental"]
    # df_cat_installment  = df.loc[df["Category"] == "Installment"]
    # df_cat_tax          = df.loc[df["Category"] == "Tax"]
    # df_cat_insurance    = df.loc[df["Category"] == "Insurance"]
    # df_cat_nuss         = df.loc[df["Category"] == "NUSS"]

    # Transfer and Remit
    # df_cat_transfer_out = df.loc[df["Category"] == "Transfer Out"]
    # df_cat_remit        = df.loc[df["Category"] == "Remit"]

    # Floating Expenses
    # df_cat_utility      = df.loc[df["Category"] == "Utility"]
    # df_cat_Telecom      = df.loc[df["Category"] == "Telecom"]
    # df_cat_meal         = df.loc[df["Category"] == "Meal"]
    # df_cat_transportation = df.loc[df["Category"] == "Transportation"]
    # df_cat_entertainment = df.loc[df["Category"] == "Entertainment"]
    # df_cat_miscellaneous = df.loc[df["Category"] == "Miscellaneous"]
    # df_cat_other_exp     = df.loc[df["Category"] == "Other Expense"]

    # output_name = "parsed_" + file_name
    # output_dir = file_dir

    # Create target Directory if don't exist
    # if not os.path.exists(output_dir):
    #     os.mkdir(output_dir)
    #     print("Directory ", output_dir, " Created ")
    #
    # print("Parsed file is saved into ", output_dir + output_name)
    # writer.write(df, output_dir + output_name)



