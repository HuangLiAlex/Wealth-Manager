import pandas as pd
from datetime import datetime as dt


def datetime_transform(src_name, str_datetime):
    date = None

    if src_name is "OCBC":
        date = dt.strptime(str_datetime, "%d/%m/%Y").date()

    elif src_name is "POSB":
        date = dt.strptime(str_datetime, "%d %b %Y").date()

    else:
        print("Error: invalid source name in datetime_transform")

    return date.strftime("%d %b %Y")


def combine(df_ocbc, df_posb):
    combine_frames = [df_ocbc, df_posb]

    df_combine = pd.concat(combine_frames)

    df_combine.sort_values(by=["Date"], ascending=True, inplace=True)

    df_combine.reset_index(drop=True, inplace=True)

    return df_combine
