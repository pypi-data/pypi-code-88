from pydantic import BaseModel
from typing import List, Dict


class OutputStruct(BaseModel):
    """
    Data class for output kafka topic.
    Note that the output topic name is created seperately from the app_name and version.
    ...

    Attributes
    ----------
    mode: streaming output mode, one of "append", "complete", "update"
    processing_time: optional time to wait to aggregate inputs before writing
    """

    mode: str
    processing_time: str = "0"


class TableStruct(BaseModel):
    """
    Data class for cassandra table.
    ...

    Attributes
    ----------
    primary_keys: list of keys that define the primary key in the cassandra table
    output_schema: list of dictionaries with name and type attributes describing the table's schema
    """

    primary_keys: List[str]
    output_schema: List[Dict[str, str]]  # name: "field1", type: "string"


class FileStruct(BaseModel):
    """
    Data class for reading data from files/gcs.
    ...

    Attributes
    ----------
    max_file_age: how far back to go to retrieve data
    """

    max_file_age: str


class InputStruct(BaseModel):
    """
    Data class for incoming kafka topics.
    ...

    Attributes
    ----------
    topic: incoming kafka topic
    topic_schema: list of dictionaries with name and type attributes describing the kafka topic's schema
    sample: optional list of possible kafka topic payloads (used for running unit tests)
    """

    topic: str
    topic_schema: List[Dict[str, str]]  # name: "field1", type: "string"
    sample: List[dict] = []  # not all need a sample


class KafkaStruct(BaseModel):
    """
    Data class for connecting to kafka
    ...

    Attributes
    ----------
    brokers: comma seperated string of brokers
    """

    brokers: str
    confluent_api_key: str
    confluent_secret: str


class FirestoreOutputStruct(BaseModel):
    """
    Data class for writing to cassandra
    ...

    Attributes
    ----------
    firestore_collection_name: firestore collection
    project_id: gcp project
    code_version: code version
    """

    firestore_collection_name: str
    project_id: str
    # schema_version: str
    code_version: str
