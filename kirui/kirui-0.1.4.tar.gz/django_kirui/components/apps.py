import json
from io import StringIO

from samon.elements import BaseElement
from samon.render import RenderedElement


class KrApp(BaseElement):
    def to_xml(self, io: StringIO, indent: int, rendered_element: RenderedElement):
        with rendered_element.frame(io, indent):
            print('<script type="text/javascript">', file=io, end='')
            print(f"let ${self.xml_attrs['id']}_data = ", file=io, end='')
            data = rendered_element.to_json()
            json.dump(data, io)
            print('</script>', file=io)
