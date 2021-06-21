import re
import uk.uk_postcode_regex as reg
from Exceptions.exceptions import ValidationError


class UKPostcode:
    """Validates & Formats the given postcode to standard UK Postcode"""
    outward_code = None
    inward_code = None

    def __init__(self, postcode):

        self.__format(postcode)

    def __format(self, postcode):
        postcode = f"{postcode}".upper()
        validation_status = reg.postcode_regex.match(postcode)
        if not validation_status:
            raise ValidationError("Postcode is invalid")
        else:
            self.outward_code, self.inward_code = validation_status.groups()

    @property
    def postcode(self):
        """Valid & formatted postcode"""
        return f"{self.outward_code} {self.inward_code}"

    @property
    def area(self):
        """Gives the area details from the postcode"""
        return re.search(reg.area_regex, self.outward_code).group()

    @property
    def district(self):
        """Gives the district details from the postcode"""
        return re.search(reg.district_regex, self.outward_code).group()

    @property
    def sector(self):
        """Gives the sector details from the postcode"""
        return re.search(reg.sector_regex, self.inward_code).group()

    @property
    def unit(self):
        """Gives the unit details from the postcode"""
        return re.search(reg.unit_regex, self.inward_code).group()
