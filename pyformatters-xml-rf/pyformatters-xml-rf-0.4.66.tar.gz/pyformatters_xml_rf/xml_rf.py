from collections import defaultdict, Counter
from pathlib import Path
from typing import Type

import lxml.etree as ET
from Ranger import RangeBucketMap, Range
from fastapi import HTTPException
from pydantic import BaseModel, Field
from pymultirole_plugins.v1.formatter import FormatterBase, FormatterParameters
from pymultirole_plugins.v1.schema import Document, Boundary, Annotation
from starlette.responses import Response


class RFXmlParameters(FormatterParameters):
    boundaries: str = Field("SECTIONS", description="Name of boundaries to consider")
    with_forms: bool = Field(True, description="Add list of all matching forms")
    absolute_uri: bool = Field(True, description="Use absolute or relative URI as identifier")


class RFXmlFormatter(FormatterBase):
    """Groupe RF XML formatter.
    """

    def format(self, document: Document, parameters: FormatterParameters) \
            -> Response:
        """Parse the input document and return a formatted response.

        :param document: An annotated document.
        :param parameters: options of the parser.
        :returns: Response.
        """
        parameters: RFXmlParameters = parameters
        if not document.sourceText:
            raise HTTPException(status_code=400, detail="No source xml text")
        try:
            data = document.sourceText
            encoding = document.properties.get('encoding', "UTF-8") if document.properties else "UTF-8"
            if document.sourceText and document.boundaries and document.annotations:
                if data.lower().startswith("<?xml"):
                    decl, data = data.split("?>", maxsplit=1)
                    decl += "?>"
                root: ET.Element = ET.fromstring(data)
                baseNs = root.nsmap.get(None, None)
                # Ignore all namespaces
                for el in root.iter():
                    if baseNs and el.tag.startswith(f"{{{baseNs}}}"):
                        _, _, el.tag = el.tag.rpartition('}')
                doc_annexes = root.find("DOC_ANNEXES")
                if not doc_annexes:
                    doc_annexes = ET.Element("DOC_ANNEXES")
                    root.append(doc_annexes)
                thesaurus = doc_annexes.find("ANNOTATIONS_SHERPA")
                if not thesaurus:
                    thesaurus = ET.Element("ANNOTATIONS_SHERPA")
                    doc_annexes.insert(0, thesaurus)
                boundaries = {}
                buckets = RangeBucketMap()
                terms = defaultdict(lambda: defaultdict(list))
                for b in document.boundaries.get(parameters.boundaries, []):
                    boundary = Boundary(**b) if isinstance(b, dict) else b
                    r = root.xpath(boundary.name)
                    if len(r) == 1:
                        node = r[0]
                        boundaries[node] = Range.closedOpen(boundary.start, boundary.end)
                        buckets[Range.closedOpen(boundary.start, boundary.end)] = node
                for a in document.annotations:
                    annotation = Annotation(**a) if isinstance(a, dict) else a
                    form = document.text[annotation.start:annotation.end]
                    if buckets.contains(annotation.start) and buckets.contains(annotation.end):
                        zones = buckets[Range.closedOpen(annotation.start, annotation.end)]
                        for zone in zones:
                            for term in annotation.terms:
                                ident = term.identifier if parameters.absolute_uri\
                                    else term.identifier[term.identifier.index("#") + 1:]
                                terms[zone][ident].append(form)

                def left_longest_match(item):
                    r: Range = item[1]
                    return r.lowerEndpoint(), r.upperEndpoint() - r.lowerEndpoint()

                sorted_boundaries = sorted(boundaries.items(), key=left_longest_match, reverse=False)

                for node, r in sorted_boundaries:
                    if node in terms and terms[node]:
                        descripteurs = ET.Element("DESCRIPTEURS_" + node.tag, node.attrib)
                        for ident, forms in terms[node].items():
                            c = Counter(forms)
                            freq = sum(c.values())
                            descripteur = ET.Element("DESCRIPTEUR", Id=ident, Freq=str(freq))
                            if parameters.with_forms:
                                desc_forms = ET.Element("FORMES")
                                for form, ffreq in c.items():
                                    desc_form = ET.Element("FORME", Freq=str(ffreq))
                                    desc_form.text = form
                                    desc_forms.append(desc_form)
                                descripteur.insert(0, desc_forms)
                            descripteurs.append(descripteur)
                        thesaurus.append(descripteurs)

                data = ET.tostring(root, pretty_print=True, encoding=encoding)
            filename = "file.xml"
            if document.properties and "fileName" in document.properties:
                filepath = Path(document.properties['fileName'])
                filename = f"{filepath.stem}.xml"
            resp = Response(content=data, media_type="application/xml")
            resp.headers["Content-Disposition"] = f"attachment; filename={filename}"
            resp.charset = encoding
            return resp
        except BaseException as err:
            raise err

    @classmethod
    def get_model(cls) -> Type[BaseModel]:
        return RFXmlParameters
