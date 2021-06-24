class LeaderboardConstants:
    ladder_ids = [      \
        4, 5, 6, 7, 51,  \
        8, 9, 10, 11, 52, \
        12, 13, 14, 15, 53,\
        16, 17, 18, 19, 54, \
        20, 21, 22, 23, 24, 25]

    ladder_names = [\
        "OST1", "SOV1", "OKW1", "USF1", "UKF1",\
        "OST2", "SOV2", "OKW2", "USF2", "UKF2",\
        "OST3", "SOV3", "OKW3", "USF3", "UKF3",\
        "OST4", "SOV4", "OKW4", "USF4", "UKF4",\
        "AX2", "AL2", "AX3", "AL3", "AX4", "AL4"]

    ladder_ids_4s_solo = [16, 17, 18, 19, 54]
    ladder_ids_team = [20, 21, 22, 23, 24, 25]

    id_to_ladder_name = dict(zip(ladder_ids, ladder_names))
    ladder_name_to_id = dict(zip(ladder_names, ladder_ids))