import os
from tkinter import Tk
from tkinter.filedialog import askopenfilename

from container.bankStatement import BankStatement
from writer.writecsv import WriteCsv

if __name__ == '__main__':

    Tk().withdraw()
    # show an "Open" dialog box and return the path to the selected file
    file_path = askopenfilename(initialdir="D:\git\Wealth-Manager\csv/")

    if file_path is "":
        exit("No CSV file is chosen!")

    idx = file_path.rfind("/") + 1
    # print(idx)

    file_dir = file_path[0 : idx]
    # print("file_dir=" + file_dir)

    file_name = file_path[idx:]
    print("file_name = " + file_name)

    bank_source = ""
    if "OCBC" in file_name.upper():
        bank_source = "OCBC"
    elif "POSB" in file_path.upper():
        bank_source = "POSB"
    else:
        exit("Please place bank name in file name.")

    writer = WriteCsv()

    bs = BankStatement(bank_source, file_path)
    df = bs.get_bank_statement()
    print("Data frame loading completed")

    output_name = "output_" + file_name
    output_dir = file_dir + "wip/"

    # Create target Directory if don't exist
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)
        print("Directory ", output_dir, " Created ")

    print("Parsed file is saved into ", output_dir, output_name)
    writer.write(df, output_dir + output_name)



