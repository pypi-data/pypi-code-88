# 总大小
from __future__ import annotations
# total = 121
# # 每一块的大小
# step = 20
# # 分多块
# parts = [(start, min(start+step, total)) for start in range(0, total, step)]

# print(parts)

# # # 看最后那一部分的最后一个数字是否等于总大小，不等于就新加一块
# if parts[-1][-1] != total:
#     start = step*len(parts)
#     end = total
#     parts.append((start, total))
# print(parts)


def split(start: int, end: int, step: int) -> list[tuple[int, int]]:
    '''
    将指定区间的数切割为多个区间

    Parameters
    ----------
    start :起始位置
    end : 终止位置
    step : 区间长度

    Return
    ------
    区间元组构成的列表
    '''
    # 分多块
    parts = [(start, min(start+step, end))
             for start in range(0, end, step)]
    # 看最后那一部分的最后一个数字是否等于总大小，不等于就新加一块
    if parts[-1][-1] != end:
        start = step*len(parts)
        parts.append((start, end))
    return parts


if "__main__" == __name__:
    # 起始位置
    start = 1
    # 终止位置
    total = 102
    # 区间长度
    step = 20
    parts = split(start, total, step)
    print(parts)
