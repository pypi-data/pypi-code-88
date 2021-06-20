def S2020_2021(semaine):
    """
    Number of the week

    Parameters
    ----------
    :param semaine: A specific week ("2020-S45")
    :type semaine: str


    Returns
    -------
    :return: number of the week

    :Examples:
    >>> S200_2021("2020-S35")
    """
    return int(semaine[3])*53+int(semaine[6:8])


def W2020_2021(number):
    """
    The week  of the year

    Parameters
    ----------
    :param number: A specific number
    :type number: int


    Returns
    -------
    :return: week of the year

    :Examples:

    >>> W200_2021("2020-S35")

    """
    if (number == 53):
        return "202"+str(number//54)+f"-S{number:02}"
    return "202"+str(number//54)+f"-S{number%53:02}"
