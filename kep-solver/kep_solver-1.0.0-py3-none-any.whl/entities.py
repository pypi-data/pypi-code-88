"""This module contains entities (such as Donors, Recipients) within a KEP, as
well as the encapsulating Instance objects
"""

from collections.abc import ValuesView
from enum import Enum
from typing import Optional


class BloodGroup(Enum):
    """The blood group of a participant in a KEP."""
    O = 0  # noqa: E741
    A = 1
    B = 2
    AB = 3

    def __str__(self):
        return _BG_TO_STR[self]


_BLOODGROUPS = {"O": BloodGroup.O,
                "A": BloodGroup.A,
                "B": BloodGroup.B,
                "AB": BloodGroup.AB}

_BG_TO_STR = {BloodGroup.O: "O",
              BloodGroup.A: "A",
              BloodGroup.B: "B",
              BloodGroup.AB: "AB"}


def parseBloodGroup(bloodGroupText: str) -> BloodGroup:
    """Given a blood group as text, return the corresponding BloodGroup object.

    :param bloodGroupText: the text
    :type bloodGroupText: str
    :return: the BloodGroup
    :rtype: BloodGroup
    """
    if bloodGroupText not in _BLOODGROUPS:
        raise Exception(f"Unknown blood group: {bloodGroupText}")
    return _BLOODGROUPS[bloodGroupText]


class Recipient:
    """A recipient in a KEP instance.
    """
    def __init__(self, id: str):
        self._id: str = id
        self._age: Optional[int] = None
        self._cPRA: Optional[float] = None
        self._bloodGroup: Optional[BloodGroup] = None
        self._donors: list['Donor'] = []

    def __str__(self):
        return f"R{self._id}"

    def longstr(self):
        """A longer string representation.

        :return: a string representation
        :rtype: str
        """
        return f"Recipient {self._id}"

    def __hash__(self):
        return hash(f"R{self._id}")

    @property
    def id(self) -> str:
        """Return the ID of this recipient.

        :return: the ID of this recipient
        :rtype: str
        """
        return self._id

    @property
    def age(self) -> int:
        """The age of this recipient.

        :param age: the age of the recipient
        :type age: int
        :return: the age of the recipient
        :rtype: int
        """
        if self._age is None:
            raise Exception(f"Age of {str(self)} not known")
        return self._age

    @age.setter
    def age(self, age: int) -> None:
        if self._age is not None:
            raise Exception(f"Trying to change age of {str(self)}")
        self._age = age

    @property
    def cPRA(self) -> float:
        """The cPRA of this recipient.

        :param cPRA: the cPRA of the recipient
        :type cPRA: float
        :return cPRA: the cPRA of the recipient
        :rtype cPRA: float
        """
        if self._cPRA is None:
            raise Exception(f"cPRA of {str(self)} not known")
        return self._cPRA

    @cPRA.setter
    def cPRA(self, cPRA: float) -> None:
        if self._cPRA is not None:
            raise Exception(f"Trying to change cPRA of {str(self)}")
        self._cPRA = cPRA

    @property
    def bloodGroup(self) -> BloodGroup:
        """The blood group of this recipient.

        :param bloodGroup: the blood group of the recipient
        :type BloodGroup: str
        :return: the blood group of the recipient
        :rtype: BloodGroup
        """
        if self._bloodGroup is None:
            raise Exception(f"bloodGroup of {str(self)} not known")
        return self._bloodGroup

    @bloodGroup.setter
    def bloodGroup(self, bloodGroup: str) -> None:
        if self._bloodGroup is not None:
            raise Exception(f"Trying to change bloodGroup of {str(self)}")
        self._bloodGroup = parseBloodGroup(bloodGroup)

    def addDonor(self, donor: 'Donor') -> None:
        """Add a paired donor for this recipient.

        :param donor: The donor to add
        :type donor: Donor
        """
        self._donors.append(donor)

    def donors(self) -> list['Donor']:
        """The list of donors paired with this recipient

        :return: the list of donors
        :rtype: list[Donor]
        """
        return self._donors


class Donor:
    """A donor (directed or non-directed) in an instance.
    """
    def __init__(self, id: str):
        """Construct a Donor object. These are assumed to be non-directed, this
        can be changed with the NDD instance variable.
        :param id: An identifier for this donor.
        """
        self._id: str = id
        self._recip: Optional[Recipient] = None
        self.NDD: bool = False
        self._age: Optional[float] = None
        self._bloodGroup: Optional[BloodGroup] = None
        self._outgoingTransplants: list['Transplant'] = []

    def __eq__(self, other):
        # Compare only on ID as an instance can only have one donor of each ID.
        return self.id == other.id

    def __str__(self):
        if self.NDD:
            return f"NDD{self._id}"
        return f"D{self._id}"

    def longstr(self):
        """A longer string representation.
        :return: a string representation
        :rtype: str
        """
        if self.NDD:
            return f"Non-directed donor {self._id}"
        return f"Donor {self._id}"

    def __hash__(self):
        return hash(f"D{self._id}")

    @property
    def id(self) -> str:
        """Return the ID of this donor.
        :return: the ID
        """
        return self._id

    @property
    def age(self) -> float:
        """Return the age of the donor (in years), fractions allowed.
        :rtype: float
        :return: the age of the donor
        """
        if self._age is None:
            raise Exception(f"Age of donor {self.id} not known")
        return self._age

    @age.setter
    def age(self, age: float) -> None:
        """Set the age of this donor in years, fractions allowed.
        :param age: The age of this donor
        :type age: float
        """
        if self._age is not None:
            raise Exception(f"Trying to change age of donor {self.id}")
        self._age = age

    @property
    def bloodGroup(self) -> BloodGroup:
        if self._bloodGroup is None:
            raise Exception(f"bloodGroup of {str(self)} not known")
        return self._bloodGroup

    @bloodGroup.setter
    def bloodGroup(self, bloodGroup: str) -> None:
        if self._bloodGroup is not None:
            raise Exception(f"Trying to change bloodGroup of {str(self)}")
        self._bloodGroup = parseBloodGroup(bloodGroup)

    @property
    def recipient(self) -> Recipient:
        """Return the recipient paired with this donor.
        :return: the recipient
        :rtype: Recipient
        """
        if self.NDD:
            raise Exception("Tried to get recipient of a non-directed donor.")
        if not self._recip:
            raise Exception("Donor is directed but has no recipient.")
        return self._recip

    @recipient.setter
    def recipient(self, new_recip: Recipient) -> None:
        """Set the recipient paired with this donor.
        :param new_recip: the paired recipient
        :type new_recip: Recipient
        """
        if self._recip is not None:
            raise Exception("Tried to set a second recipient on a donor")
        if self.NDD:
            raise Exception("Tried to set recipient of a non-directed donor.")
        self._recip = new_recip

    def addTransplant(self, transplant: 'Transplant') -> None:
        """Add a potential transplant from this donor.
        :param transplant: the transplant object
        :type transplant: Transplant
        """
        self._outgoingTransplants.append(transplant)

    def transplants(self) -> list['Transplant']:
        """Return the list of transplants associated with this Donor.
        :return: A list of transplants
        :rtype: list[Transplant]
        """
        return self._outgoingTransplants


class Transplant:
    """A potential transplant."""
    def __init__(self, donor: Donor, recipient: Recipient, weight: float):
        self._donor: Donor = donor
        self._recipient: Recipient = recipient
        self._weight: float = weight

    def __str__(self):
        """Return a string representation of this transplant."""
        return f"Transplant({self.donor.id},{self.recipient.id},{self.weight})"

    @property
    def donor(self) -> Donor:
        return self._donor

    @property
    def recipient(self) -> Recipient:
        return self._recipient

    @property
    def weight(self) -> float:
        return self._weight


class Instance:
    """A KEP instance."""
    def __init__(self) -> None:
        """Create a new KEP instance."""
        self._donors: dict[str, Donor] = {}
        self._recips: dict[str, Recipient] = {}
        self._transplants: list[Transplant] = []

    def addDonor(self, donor: Donor) -> None:
        """Add a donor to the instance.
        :param donor: The Donor being added
        """
        if donor.id in self._donors:
            raise Exception(f"Trying to replace Donor {donor.id} in instance")
        self._donors[donor.id] = donor

    def recipient(self, id: str, create: bool = True) -> Recipient:
        """Get a recipient from the instance by ID. If the recipient does not
        exist, create one with no details.
        :param id: the ID of the recipient
        :type id: str
        :param create: If True, will create recipient if it doesn't exist. If
        False, and the recipient does not exist, will raise an exception.
        :type create: bool
        :return: the recipient
        :rtype: Recipient
        """
        if id in self._recips:
            return self._recips[id]
        if not create:
            raise Exception(f"Recipient with ID \"{id}\" not found")
        recip = Recipient(id)
        self._recips[id] = recip
        return recip

    def recipients(self) -> ValuesView[Recipient]:
        """Return a list of all recipients.
        :return: a list of recipients
        """
        return self._recips.values()

    def addTransplant(self, transplant: Transplant) -> None:
        """Add a potential transplant to this instance.
        :param transplant: The transplant
        :type transplant: Transplant
        """
        self._transplants.append(transplant)
        transplant.donor.addTransplant(transplant)

    def donors(self) -> ValuesView[Donor]:
        """Return a generator object that can iterate through donors in a
        list-like fashion. Note that this list cannot itself be modified.
        :return: a list of donors
        """
        return self._donors.values()

    def donor(self, id: str) -> Donor:
        """Return a donor by ID:
        :param id: a donor ID
        :type id: str
        :rtype: Donor
        :return: the donor
        """
        return self._donors[id]

    def transplants(self) -> list[Transplant]:
        return self._transplants
