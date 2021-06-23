"""Parsing and identification of metabolites."""

from enum import Enum, auto

from .metabolite import Metabolite


class CompartmentConvention(Enum):
    """The convention used to define the compartment of a metabolite.
    """
    UNDERSCORE = auto()
    """The metabolite ID ends with "_<compartment_ID>" (e.g. g6p_c).
    """


class Namespace(Enum):
    """The namespace in which metabolite identifiers are defined.
    """
    UNSPECIFIED = auto()
    """The namespace is not specified. In most cases PTA can find the metabolite
    in eQuilbrator even if the namespace is not specified. However, this is not
    guaranteed and it is recommended to always specify a namespace.
    """
    BIGG = auto()
    """Assume that metabolite identifiers belong to the BiGG namespace.
    """


class MetaboliteInterpreter:
    """
    An interpreter used to transform metabolite IDs to compound identifiers that can be
    understood by eQuilibrator and compartment identifiers.

    Parameters
    ----------
    compartment_convention : CompartmentConvention, optional
        Naming convention used to specify metabolite and compartment identifiers, by
        default CompartmentConvention.UNDERSCORE.
    namespace : Namespace, optional
        Namespace in which the metabolite identifiers are defined, by default
        Namespace.BIGG.
    """

    def __init__(
        self,
        compartment_convention: CompartmentConvention =
            CompartmentConvention.UNDERSCORE,
        namespace: Namespace = Namespace.BIGG
    ):
        self.compartment_convention = compartment_convention
        self.namespace = namespace

    def read(
        self,
        metabolite_name: str
    ) -> Metabolite:
        """Parses a metabolite from a string, reading its identifier and
        compartment. 

        Parameters
        ----------
        metabolite_name : str
            The identifier of a metabolite.

        Returns
        -------
        Metabolite
            Object describing the parsed metabolite. Note that only the identifier and
            compartment are set, the remaining fields (such as the charge) have to be
            specified manually.

        Raises
        ------
        Exception
            If the naming convention or namespace of the metabolite are not supported.
        """

        metabolite_id = ''
        compartment = ''

        if self.compartment_convention == CompartmentConvention.UNDERSCORE:
            (metabolite_id, compartment) = metabolite_name.rsplit('_', 1)
        else:
            raise Exception(f'Unsupported compartment convention: '
                            f'{self.compartment_convention}')

        if self.namespace == Namespace.UNSPECIFIED:
            pass
        elif self.namespace == Namespace.BIGG:
            metabolite_id = 'bigg.metabolite:' + metabolite_id
        else:
            raise Exception(f'Unsupported namespace: {self.namespace}')

        return Metabolite(metabolite_id, compartment)

    @property
    def compartment_convention(self) -> CompartmentConvention:
        """Gets the convention used to specify compartments."""
        return self._compartment_convention

    @compartment_convention.setter
    def compartment_convention(self, value: CompartmentConvention):
        """Sets the convention used to specify compartments."""
        self._compartment_convention = value

    @property
    def namespace(self) -> Namespace:
        """Gets the namespace of the metabolite names."""
        return self._namespace

    @namespace.setter
    def namespace(self, value: Namespace):
        """Sets the namespace of the metabolite names."""
        self._namespace = value
