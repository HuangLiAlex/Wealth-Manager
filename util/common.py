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
