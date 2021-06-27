import numpy as np

def generate_vidya_arr(high_array, low_array, moving_average_length = 10):

    valpha = 2/(moving_average_length + 1)

    hl2 = (high_array + low_array)/2

    vud1 = []

    before_val = 0

    for current_hl2 in hl2:
        if current_hl2 > before_val:
            vud1.append(current_hl2 - before_val)
        else:
            vud1.append(0)

        before_val = current_hl2

    vdd1 = []

    for current_hl2 in hl2:
        if current_hl2 < before_val:
            vdd1.append(before_val - current_hl2)
        else:
            vdd1.append(0)

        before_val = current_hl2

    vUD = []

    geriden_gelen_indx = 0

    len_vud1 = len(vud1)

    finished = False

    for j in range(1,9):
        window_sum = 0
        for k in range(0,j):
            window_sum = window_sum + vud1[k]
        vUD.append(window_sum)

    while geriden_gelen_indx < len_vud1:
        window_sum = 0
        for i in range(0,9):
            current_indx = geriden_gelen_indx + i
            if current_indx >= len_vud1:
                finished = True
                break
            window_sum = window_sum + vud1[current_indx]
        vUD.append(window_sum)

        if finished:
            break

        geriden_gelen_indx = geriden_gelen_indx + 1

    vUD_ar = np.asarray(vUD[:-1])

    vDD = []

    geriden_gelen_indx = 0

    len_vdd1 = len(vdd1)

    finished = False

    for j in range(1,9):
        window_sum = 0
        for k in range(0,j):
            window_sum = window_sum + vdd1[k]
        vDD.append(window_sum)

    while geriden_gelen_indx < len_vdd1:
        window_sum = 0
        for i in range(0,9):
            current_indx = geriden_gelen_indx + i
            if current_indx >= len_vdd1:
                finished = True
                break
            window_sum = window_sum + vdd1[current_indx]
        vDD.append(window_sum)

        if finished:
            break

        geriden_gelen_indx = geriden_gelen_indx + 1

    vDD_ar = np.asarray(vDD[:-1])

    vCMO = ((vUD_ar - vDD_ar) / (vUD_ar + vDD_ar))

    hl2_left = hl2[:]

    var_before = 0.0

    var = []

    for i in range(0, len(high_array)):
        var_current = (valpha * abs(vCMO[i])*hl2_left[i]) + (1 - valpha*abs(vCMO[i]))*var_before
        var.append(var_current)
        var_before = var_current

    var_arr = np.asarray(var)

    return var_arr
