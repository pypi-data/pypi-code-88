import io
from enum import Enum
from pathlib import Path
from typing import Type

import pandas as pd
from pydantic import BaseModel, Field
from pymultirole_plugins.v1.formatter import FormatterBase, FormatterParameters
from pymultirole_plugins.v1.schema import Document
from starlette.responses import Response


class OutputFormat(str, Enum):
    xlsx = 'xlsx'
    csv = 'csv'


class TabularParameters(FormatterParameters):
    format: OutputFormat = Field(OutputFormat.xlsx, description="Output format")


class TabularFormatter(FormatterBase):
    """Tabular formatter.
    """

    def format(self, document: Document, parameters: FormatterParameters) \
            -> Response:
        """Parse the input document and return a formatted response.

        :param document: An annotated document.
        :param options: options of the parser.
        :returns: Response.
        """
        parameters: TabularParameters = parameters
        try:
            resp: Response = None
            df: pd.DataFrame = None
            records = []
            if document.annotations:
                for a in document.annotations:
                    record = a if isinstance(a, dict) else a.dict()
                    record['text'] = document.text[record['start']:record['end']]
                    props = record.pop('properties', None)
                    if props:
                        for prop, val in props.items():
                            record[f"properties.{prop}"] = str(val)
                    terms = record.pop('terms', None)
                    if terms:
                        for i, term in enumerate(terms):
                            for key, val in term.items():
                                record[f"terms.{i}.{key}"] = str(val)
                    records.append(record)
            # if document.categories:
            #     for c in document.categories:
            #         record = c if isinstance(c, dict) else c.dict()
            #         props = record.pop('properties', None)
            #         if props:
            #             for prop, val in props.items():
            #                 record[f"properties.{prop}"] = str(val)
            #         records.append(record)
            df = pd.DataFrame.from_records(records)
            filename = f"file.{parameters.format.value}"
            if document.properties and "fileName" in document.properties:
                filepath = Path(document.properties['fileName'])
                filename = f"{filepath.stem}.{parameters.format.value}"
            if parameters.format == OutputFormat.xlsx:
                bio = io.BytesIO()
                df.to_excel(bio)
                resp = Response(content=bio.getvalue(),
                                media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
                resp.headers["Content-Disposition"] = f"attachment; filename={filename}"
            elif parameters.format == OutputFormat.csv:
                sio = io.StringIO()
                df.to_csv(sio, index=False)
                resp = Response(content=sio.getvalue(),
                                media_type="text/csv")
                resp.headers["Content-Disposition"] = f"attachment; filename={filename}"
            return resp
        except BaseException as err:
            raise err

    @classmethod
    def get_model(cls) -> Type[BaseModel]:
        return TabularParameters
