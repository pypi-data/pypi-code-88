def generate_number(area_code=None):
    """
    Generates a random phone number
    """
    from random import randint
    NPA = str(randint(201, 999))
    NXX = str(randint(2, 9)) + str(randint(00, 99))
    XXXX = str(randint(0000, 9999))

    if area_code is None:
        phone = NPA + "-" + NXX + "-" + XXXX
    else:
        phone = str(area_code) + "-" + NXX + "-" + XXXX

    return phone
