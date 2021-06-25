from .utils import is_mykad_valid, get_birthplace
from datetime import datetime


class MyKad:
    """The base MyKad class.

    :param mykad_num: The MyKad number. This can contain numbers and '-'
    :type mykad_num: str, int
    """
    def __init__(self, mykad_num):
        if (is_mykad_valid(mykad_num)):
            self.mykad_num = mykad_num.replace('-', '')
        else:
            raise ValueError(f'MyKad number {mykad_num} is not valid')

    def __str__(self):
        return f'{self.get_formatted()}'

    @property
    def birthdate_yymmdd(self):
        return self.mykad_num[0:6]

    @property
    def birthplace_code(self):
        return self.mykad_num[6:8]

    @property
    def special_nrd_num(self):
        return self.mykad_num[8:11]

    @property
    def gender_code(self):
        return self.mykad_num[11]

    @property
    def birthdate(self):
        """Returns the datetime instance corresponding to this
        MyKad holder.

        :return: The datetime instance
        :rtype: datetime
        """
        birthdate = datetime.strptime(self.birthdate_yymmdd, "%y%m%d")

        # Make sure dates past current time are 19xx and not 20xx.
        # This is mostly due to the limitations of ISO 8601:2000
        # where a date '570620' in YYMMDD format could be initialised
        # as 20th June 2057 rather than 20th June 1957.
        # I don't see any workaround to this unless the Malaysian
        # gov switches to a YYYYMMDD format.
        if birthdate.year > datetime.now().year:
            # Reconstruct datetime instance with a different year (i.e. 19xx instead of 20xx)
            birthdate = datetime(year=int('19' + str(birthdate.year)[2:4]), month=birthdate.month, day=birthdate.day)

        return birthdate

    @property
    def birth_year(self):
        return self.birthdate.year

    @property
    def birth_month(self):
        return self.birthdate.month

    @property
    def day_of_birth(self):
        return self.birthdate.day

    @property
    def birthplace(self):
        return get_birthplace(self.birthplace_code)

    @property
    def gender(self):
        if self.is_male():
            return "Male"
        else:
            return "Female"

    def get_unformatted(self):
        """Returns the unformatted MyKad string (i.e. just numbers, without '-')

        :return: The unformatted MyKad number
        :rtype: str
        """
        return self.mykad_num

    def get_formatted(self):
        """Returns the formatted MyKad string (with '-')
                :return: The formatted MyKad number
        :rtype: str
        """
        return f'{self.birthdate.strftime("%y%m%d")}-{self.birthplace_code}-{self.special_nrd_num}{self.gender_code}'

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
