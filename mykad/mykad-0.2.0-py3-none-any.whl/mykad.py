from .constants import state_dict
from .utils import is_mykad_valid
from datetime import datetime


class MyKad:
    """The base MyKad class.

    :param mykad_num: The MyKad number. This can contain numbers and '-'
    :type mykad_num: str, int
    """
    def __init__(self, mykad_num):
        if (is_mykad_valid(mykad_num)):
            self.mykad_num = mykad_num
        else:
            raise ValueError(f'MyKad number {mykad_num} is not valid')

        # If MyKad is valid we should extract the information out of it
        # YYMMDD-PB-###G
        self.birth_year = self.mykad_num[0:2]
        self.birth_month = self.mykad_num[2:4]
        self.birth_day = self.mykad_num[4:6]
        self.birthplace_code = self.mykad_num[6:8]
        self.special_nrd_num = self.mykad_num[8:11]
        self.gender_code = self.mykad_num[-1]

    def get_unformatted(self):
        """Returns the unformatted MyKad string (i.e. just numbers, without '-')

        :return: The unformatted MyKad number
        :rtype: str
        """
        return self.mykad_num.replace('-', '')

    def get_formatted(self):
        """Returns the formatted MyKad string (with '-')

        :return: The formatted MyKad number
        :rtype: str
        """
        return f'{self.birth_year}{self.birth_month}{self.birth_day}-{self.birthplace_code}-{self.special_nrd_num}{self.gender_code}'

    def get_birth_year(self):
        """Returns the birthyear of the MyKad holder in YY format. For YYYY format, use `get_pretty_birth_year()` instead

        :return: The birth year in YY format
        :rtype: str
        """
        return self.birth_year

    def get_pretty_birth_year(self):
        """Returns the birthyear of the MyKad holder in YYYY format.

        :return: The birth year in YYYY format
        :rtype: str
        """
        # MyKads started being issued in the year 1949
        if int(self.birth_year) >= 49:
            return f'19{self.birth_year}'

        return f'20{self.birth_year}'

    def get_birth_month(self):
        """Returns the birth month of the MyKad holder in MM format. To get the birth month in English, use `get_pretty_birth_month()` instead

        :return The birth month in MM format
        :rtype str
        """
        return self.birth_month

    def get_pretty_birth_month(self):
        """Returns the birth month of the MyKad holder in English.

        :return The birth month in English
        :rtype str
        """
        month_dict = {
            '01': 'January',
            '02': 'February',
            '03': 'March',
            '04': 'April',
            '05': 'May',
            '06': 'June',
            '07': 'July',
            '08': 'August',
            '09': 'September',
            '10': 'October',
            '11': 'November',
            '12': 'December',
        }

        return month_dict[self.birth_month]

    def get_birth_day(self):
        """Returns the day of birth of the MyKad holder in DD format. To get the exact day in English, use `get_pretty_birth_day()` instead.

        :return The day of birth of the MyKad holder in DD format
        :rtype str
        """
        return self.birth_day

    def get_pretty_birth_day(self):
        """Returns the day of birth of the MyKad holder.

        :return The day of birth of the MyKad holder in English
        :rtype str
        """
        return datetime.fromisoformat(f'{self.get_pretty_birth_year()}-{self.get_birth_month()}-{self.get_birth_day()}').strftime('%A')

    def get_birthplace_code(self):
        """Returns the birthplace code of the MyKad holder. To get the birthplace (either a Malaysian state or a country abroad) of the MyKad holder, use `get_birthplace()` instead.

        :return The birthplace code of the MyKad holder
        :rtype str
        """
        return self.birthplace_code

    def get_birthplace(self):
        """Returns the birthplace of the MyKad holder.

        :return The birthplace of the MyKad holder
        :rtype str
        """
        for key, val in state_dict.items():
            if int(self.birthplace_code) in val:
                return key

        return 'Outside Malaysia'

    def is_male(self):
        """Checks if the MyKad holder is a male.

        :return True if male, False otherwise
        :rtype bool
        """
        return int(self.gender_code) % 2 != 0

    def is_female(self):
        """Checks if the MyKad holder is a female.

        :return True if female, False otherwise
        :rtype bool
        """
        return int(self.gender_code) % 2 == 0

    def get_gender_code(self):
        """Returns the gender code of the MyKad holder.

        :return The gender code of the MyKad holder. For a proper "Male" or "Female" string, use `get_gender()` instead
        :rtype str
        """

        return self.gender_code

    def get_gender(self):
        """Returns the gender of the MyKad holder.

        :return Either "Male" or "Female"
        :rtype str
        """

        if self.is_male():
            return "Male"
        else:
            return "Female"
