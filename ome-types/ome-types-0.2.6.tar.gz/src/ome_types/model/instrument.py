from typing import Any, Dict, List, Optional, Union

from pydantic import Field, validator

from ome_types._base_type import OMEType

from .annotation_ref import AnnotationRef
from .arc import Arc
from .detector import Detector
from .dichroic import Dichroic
from .filament import Filament
from .filter import Filter
from .filter_set import FilterSet
from .generic_excitation_source import GenericExcitationSource
from .laser import Laser
from .light_emitting_diode import LightEmittingDiode
from .light_source import LightSource
from .microscope import Microscope
from .objective import Objective
from .simple_types import InstrumentID

_light_source_types: Dict[str, type] = {
    "laser": Laser,
    "arc": Arc,
    "filament": Filament,
    "light_emitting_diode": LightEmittingDiode,
    "generic_excitation_source": GenericExcitationSource,
}


class Instrument(OMEType):
    """This element describes the instrument used to capture the Image.

    It is primarily a container for manufacturer's model and catalog numbers for
    the Microscope, LightSource, Detector, Objective and Filters components. The
    Objective element contains the additional elements LensNA and Magnification.
    The Filters element can be composed either of separate excitation, emission
    filters and a dichroic mirror or a single filter set. Within the Image itself,
    a reference is made to this one Filter element. There may be multiple light
    sources, detectors, objectives and filters on a microscope. Each of these has
    their own ID attribute, which can be referred to from Channel. It is
    understood that the light path configuration can be different for each
    channel, but cannot be different for each timepoint or each plane of an XYZ
    stack.

    Parameters
    ----------
    id : InstrumentID
    annotation_ref : AnnotationRef, optional
    detectors : Detector, optional
    dichroics : Dichroic, optional
    filter_sets : FilterSet, optional
    filters : Filter, optional
    light_source_group : List[LightSource], optional
    microscope : Microscope, optional
    objectives : Objective, optional
    """

    id: InstrumentID
    annotation_ref: List[AnnotationRef] = Field(default_factory=list)
    detectors: List[Detector] = Field(default_factory=list)
    dichroics: List[Dichroic] = Field(default_factory=list)
    filter_sets: List[FilterSet] = Field(default_factory=list)
    filters: List[Filter] = Field(default_factory=list)
    light_source_group: List[LightSource] = Field(default_factory=list)
    microscope: Optional[Microscope] = None
    objectives: List[Objective] = Field(default_factory=list)

    @validator("light_source_group", pre=True, each_item=True)
    def validate_light_source_group(
        cls, value: Union[LightSource, Dict[Any, Any]]
    ) -> LightSource:
        if isinstance(value, LightSource):
            return value
        elif isinstance(value, dict):
            try:
                _type = value.pop("_type")
            except KeyError:
                raise ValueError("dict initialization requires _type") from None
            try:
                light_source_cls = _light_source_types[_type]
            except KeyError:
                raise ValueError(f"unknown LightSource type '{_type}'") from None
            return light_source_cls(**value)
        else:
            raise ValueError("invalid type for light_source_group values")
