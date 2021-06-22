
from typing import Type, List, cast
from pydantic import BaseModel, Field
from pymultirole_plugins.v1.annotator import AnnotatorParameters, AnnotatorBase
from pymultirole_plugins.v1.schema import Document


class StefanParameters(AnnotatorParameters):
    foo: str = Field("foo", description="Foo")
    bar: float = Field(0.123456789, description="Bar")


class StefanAnnotator(AnnotatorBase):
    """Stefan annotator .
    """
    def annotate(self, documents: List[Document], parameters: AnnotatorParameters) \
            -> List[Document]:
        params: StefanParameters =\
            cast(StefanParameters, parameters)
        documents[0].annotations = [{'start': 0, 'end': 1, 'labelName': params.foo}]
        return documents

    @classmethod
    def get_model(cls) -> Type[BaseModel]:
        return StefanParameters
