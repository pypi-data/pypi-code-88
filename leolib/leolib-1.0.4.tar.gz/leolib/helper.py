import re

from .api import User
import datetime


def get_day(days: int = 0):
    """
    返回的日期格式 %Y-%m-%d
    :param days: 距离今天的天数
    :return: 格式 %Y-%m-%d
    """
    return (datetime.datetime.now() + datetime.timedelta(days=days)).strftime("%Y-%m-%d")


def get_time(str_time=None, fix=True):
    """
    获取分钟时间
    :param fix: 获取以30分钟为分度的分钟时间
    :param str_time: 格式 %H:%M 范围: 7:30 - 22:30
    :return: int: 分钟
    """
    if str_time is None:
        str_time = datetime.datetime.now().strftime("%H:%M")
        fix = False
    if len(str(str_time).split(":")) == 1:
        hour = datetime.datetime.now().hour + int(str_time)
        minute = datetime.datetime.now().minute
    else:
        hour = int(str_time.split(":")[0])
        minute = int((int(str_time.split(":")[1]) // 30)
                     * 30) if fix else int(str_time.split(":")[1])
    return minute + hour * 60


def get_seat_id(user: User, loc: str):
    """
    通过座位地址获取seatId
    :param user:
    :param loc:
    :return:
    """
    pattern = r'(.*馆)(\d)层(.*[$|\D])(\d*)号'
    res = re.match(pattern, loc)
    room_info = user.get_room()
    for building in room_info["data"]["buildings"]:
        if building[1] == res.group(1):
            for room in room_info["data"]["rooms"]:
                if str(room[1]) == res.group(3) and room[2] == building[0] and str(room[3]) == res.group(2):
                    room_id = room[0]
                    layout_info = user.get_room_status(room_id, date=get_day())
                    for seat in layout_info["data"]["layout"].values():
                        if str(seat.get("name")) == str(res[4]):
                            return seat["id"]


def reservation(user: User):
    """
    获取精确的预约情况
    :param user:
    :return:
    """
    data = user.get_history()
    res = {
        "status": "success",
        "data": {
            "reservations": []
        }
    }
    try:
        for _reservation in data["data"]["reservations"]:
            if _reservation["stat"] == "RESERVE":
                res["data"]["reservations"].append(_reservation)
    finally:
        return res
