"""Description of a metabolite."""


class Metabolite:
    """Describes the properties of a metabolite relevant for the estimation of Gibbs
    free energies.

    Parameters
    ----------
    key : str
        The identifier of the metabolite.
    compartment : str, optional
        The identifier of the compartment, by default 'c'.
    nH : int, optional
        Number of hydrogen atoms in the metabolite, by default 0.
    z : int, optional
        Charge of the metabolite, by default 0.
    """

    def __init__(
        self,
        key: str,
        compartment: str = 'c',
        nH: int = 0,
        z: int = 0
    ):
        self._key = key
        self._compartment = compartment
        self._nH = nH
        self._z = z

    @property
    def key(self) -> str:
        """Gets the key of the metabolite."""
        return self._key

    @key.setter
    def key(self, value: str):
        """Sets the key of the metabolite."""
        self._key = value

    @property
    def compartment(self) -> str:
        """Gets the compartment ID of the metabolite."""
        return self._compartment

    @compartment.setter
    def compartment(self, value: str):
        """Sets the compartment ID of the metabolite."""
        self._compartment = value

    @property
    def nH(self) -> int:
        """Gets the number of hydrogen atoms in the metabolite."""
        return self._nH

    @nH.setter
    def nH(self, value: int):
        """Sets the number of hydrogen atoms in the metabolite."""
        self._nH = value

    @property
    def z(self) -> int:
        """Gets the charge of the metabolite."""
        return self._z

    @z.setter
    def z(self, value: int):
        """Sets the charge of the metabolite."""
        self._z = value
