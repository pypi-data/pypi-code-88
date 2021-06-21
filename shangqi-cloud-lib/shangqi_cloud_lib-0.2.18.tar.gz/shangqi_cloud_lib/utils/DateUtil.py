import datetime


def strDate(date_type="datetime", delta=0):
    curr_date = datetime.datetime.now()
    delta_x_map = {
        "day": 1,
        "month": 30,
        "year": 365,
    }
    if delta != 0:
        delta = int(delta * delta_x_map.get(date_type, 1))
        curr_date = curr_date + datetime.timedelta(delta)
    if date_type == "day":
        result = curr_date.strftime("%Y-%m-%d")
    elif date_type == "month":
        result = curr_date.strftime("%Y-%m")
    elif date_type == "year":
        result = curr_date.strftime("%Y")
    else:
        result = curr_date.strftime("%Y-%m-%d %H:%M:%S")
    return result
