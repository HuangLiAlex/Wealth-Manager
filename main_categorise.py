import os
from tkinter import Tk
from tkinter.filedialog import askopenfilename

from reader.readParsedCsv import ReadParsedCsv
from writer.writecsv import WriteCsv

if __name__ == '__main__':

    Tk().withdraw()
    # show an "Open" dialog box and return the path to the selected file
    file_path = askopenfilename(initialdir="D:\git\Wealth-Manager\csv/")

    if file_path is "":
        exit("No CSV file is chosen!")

    writer = WriteCsv()

    idx = file_path.rfind("/") + 1
    # print(idx)

    file_dir = file_path[0: idx]
    # print("file_dir=" + file_dir)

    file_name = file_path[idx:]
    print("file_name = " + file_name)

    df = ReadParsedCsv.read(file_path)
    print("Data frame loading completed")

    # Revenue
    df_cat_salary       = df.loc[df["Category"] == "Salary"]
    df_cat_transfer_in  = df.loc[df["Category"] == "Transfer In"]
    df_cat_other_rev    = df.loc[df["Category"] == "Other Income"]

    # Fixed Expenses
    df_cat_cpf          = df.loc[df["Category"] == "CPF"]
    df_cat_loan         = df.loc[df["Category"] == "Loan"]
    df_cat_rental       = df.loc[df["Category"] == "Rental"]
    df_cat_installment  = df.loc[df["Category"] == "Installment"]
    df_cat_tax          = df.loc[df["Category"] == "Tax"]
    df_cat_insurance    = df.loc[df["Category"] == "Insurance"]
    df_cat_nuss         = df.loc[df["Category"] == "NUSS"]

    # Transfer and Remit
    df_cat_transfer_out = df.loc[df["Category"] == "Transfer Out"]
    df_cat_remit        = df.loc[df["Category"] == "Remit"]

    # Floating Expenses
    df_cat_utility      = df.loc[df["Category"] == "Utility"]
    df_cat_Telecom      = df.loc[df["Category"] == "Telecom"]
    df_cat_meal         = df.loc[df["Category"] == "Meal"]
    df_cat_transportation = df.loc[df["Category"] == "Transportation"]
    df_cat_entertainment = df.loc[df["Category"] == "Entertainment"]
    df_cat_miscellaneous = df.loc[df["Category"] == "Miscellaneous"]
    df_cat_other_exp     = df.loc[df["Category"] == "Other Expense"]

    output_name = "parsed_" + file_name
    output_dir = file_dir

    # Create target Directory if don't exist
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)
        print("Directory ", output_dir, " Created ")

    print("Parsed file is saved into ", output_dir, output_name)
    writer.write(df, output_dir + output_name)



