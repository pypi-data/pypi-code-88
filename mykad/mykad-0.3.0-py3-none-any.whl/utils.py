from .constants import abbreviation_dict, state_dict


def is_mykad_valid(mykad_num):
    """Checks if a MyKad number is valid.

    :return: True if MyKad is valid, False otherwise
    :rtype: bool
    """

    # Since this is meant to be a generic utility function, we accept both str and int
    if type(mykad_num) != str and type(mykad_num) != int:
        return False

    mykad_num = str(mykad_num)

    if '-' in mykad_num:
        mykad_num = mykad_num.replace('-', '')

    # MyKad should be correct length
    if len(mykad_num) != 12:
        return False

    # MyKad should only contain decimals
    if not mykad_num.isdecimal():
        return False

    # Check if PB (place of birth) code is valid
    try:
        get_birthplace(mykad_num[6:8])
    except ValueError:
        return False

    return True

def get_birthplace(birthplace_code):
    """Returns the birthplace of the MyKad holder.

    :return The birthplace code of the MyKad holder (i.e. 'BP' in YYMMDD-BP-###G)
    :rtype str, int
    """
    if (int(birthplace_code) == 0 or
        int(birthplace_code) == 17 or
        int(birthplace_code) == 18 or
        int(birthplace_code) == 19 or
        int(birthplace_code) == 20 or
        int(birthplace_code) == 69 or
        int(birthplace_code) == 70 or
        int(birthplace_code) == 73 or
        int(birthplace_code) == 80 or
        int(birthplace_code) == 81 or
        int(birthplace_code) == 94 or
        int(birthplace_code) == 95 or
        int(birthplace_code) == 96 or
        int(birthplace_code) == 97):
        raise ValueError(f'code {birthplace_code} is an invalid birthplace code')

    for key, val in state_dict.items():
        if int(birthplace_code) in val:
            return key

    return 'Outside Malaysia'

def get_state_abbreviation(state):
    """Gets the state abbreviation.

    :param state: The name of the state. This can be lower or upper-case
    :type state: str

    :return: State abbreviation (i.e. SGR, KUL, etc.)
    :rtype: str
    """
    for key, val in abbreviation_dict.items():
        # Make it lowercase to better generalise it
        if state.lower() == key.lower():
            return val

    raise ValueError(f'unknown state {state}')
