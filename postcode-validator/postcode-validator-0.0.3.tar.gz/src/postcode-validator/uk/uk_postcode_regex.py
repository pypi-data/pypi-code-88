import re

postcode_regex = re.compile(r"^([A-Z]{1,2}[0-9][A-Z0-9]?) *([0-9][A-Z]{2})$")
area_regex = re.compile(r"^[A-Z]{1,2}")
district_regex = re.compile(r"[0-9]{1,2}[A-Z]?$")
sector_regex = re.compile(r"^[0-9]")
unit_regex = re.compile(r"[A-Z0-9]{2}$")
