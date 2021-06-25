# %%
import typing
import time
import os
import logging
import requests
import json
from typing import Any, Optional, List, Type, Text, Dict

# %%
from rasa.nlu.components import Component
from rasa.nlu.config import RasaNLUModelConfig
from rasa.nlu.training_data import Message, TrainingData
import rasa.utils.endpoints as endpoints_utils
from rasa.constants import DOCS_URL_COMPONENTS
from rasa.nlu.constants import ENTITIES
from rasa.nlu.config import RasaNLUModelConfig
from rasa.nlu.extractors.extractor import EntityExtractor
from rasa.nlu.model import Metadata
from rasa.nlu.training_data import Message
from rasa.utils.common import raise_warning

# %%
logger = logging.getLogger(__name__)


# %%
def extract_value(match: Dict[Text, Any]) -> Dict[Text, Any]:
    if match["value"].get("type") == "interval":
        value = {
            "to": match["value"].get("to", {}).get("value"),
            "from": match["value"].get("from", {}).get("value"),
        }
    else:
        value = match["value"].get("value")

    return value


# %%
def convert_duckling_format_to_rasa(
    matches: List[Dict[Text, Any]]
) -> List[Dict[Text, Any]]:
    extracted = []

    for match in matches:
        value = extract_value(match)
        entity = {
            "start": match["start"],
            "end": match["end"],
            "text": match.get("body", match.get("text", None)),
            "value": value,
            "confidence": 1.0,
            "additional_info": match["value"],
            "entity": match["dim"],
        }

        extracted.append(entity)

    return extracted


# %%
class SofieHTTPExtractor(EntityExtractor):
    """A pre-trained entity extractor component"""

    # Which components are required by this component.
    # Listed components should appear before the component itself in the pipeline.
    @classmethod
    def required_components(cls) -> List[Type[Component]]:
        """Specify which components need to be present in the pipeline."""

        return []
    
    @staticmethod
    def _reference_time_from_message(message: Message) -> int:
        if message.time is not None:
            try:
                return int(message.time) * 1000
            except ValueError as e:
                logging.warning(
                    "Could not parse timestamp {}. Instead "
                    "current UTC time will be passed to "
                    "duckling. Error: {}".format(message.time, e)
                )
        # fallbacks to current time, multiplied by 1000 because duckling
        # requires the reftime in miliseconds
        return int(time.time()) * 1000

    # Defines the default configuration parameters of a component
    # these values can be overwritten in the pipeline configuration
    # of the model. The component should choose sensible defaults
    # and should be able to create reasonable results with the defaults.
    defaults = {
        # by default all dimensions recognized by duckling are returned
        # dimensions can be configured to contain an array of strings
        # with the names of the dimensions to filter for
        "dimensions": None,
        # http url of the running duckling server
        "url": None,
        # locale - if not set, we will use the language of the model
        "locale": None,
        # timezone like Europe/Istanbul
        # if not set the default timezone of Duckling is going to be used
        "timezone": None,
        # Timeout for receiving response from http url of the running duckling server
        # if not set the default timeout of duckling http url is set to 3 seconds.
        "timeout": 3,
    }

    # Defines what language(s) this component can handle.
    # This attribute is designed for instance method: `can_handle_language`.
    # Default value is None which means it can handle all languages.
    # This is an important feature for backwards compatibility of components.
    language_list = ["tr", "en"]

    def __init__(
        self, 
        component_config: Optional[Dict[Text, Any]] = None, 
        language: Optional[Text] = None
    ) -> None:
        super().__init__(component_config)
        self.language = language

    def train(
            self,
            training_data: TrainingData,
            config: Optional[RasaNLUModelConfig] = None,
            **kwargs: Any,
    ) -> None:
        """Train this component.

        This is the components chance to train itself provided
        with the training data. The component can rely on
        any context attribute to be present, that gets created
        by a call to :meth:`components.Component.pipeline_init`
        of ANY component and
        on any context attributes created by a call to
        :meth:`components.Component.train`
        of components previous to this one."""
        pass

    
    def _locale(self) -> Optional[Text]:
        if not self.component_config.get("locale"):
            # this is king of a quick fix to generate a proper locale
            # works most of the time
            language = self.language or ""
            locale_fix = "{}_{}".format(language, language.upper())
            self.component_config["locale"] = locale_fix
        return self.component_config.get("locale")

    def _payload(self, text: Text, reference_time: int) -> Dict[Text, Any]:
        dimensions = self.component_config["dimensions"]
        return {
            "text": text,
            "locale": self._locale(),
            "tz": self.component_config.get("timezone"),
            "dims": json.dumps(dimensions),
            "reftime": reference_time,
        }

    def _url(self) -> Optional[Text]:
        """Return url of the duckling service. Environment var will override."""
        if os.environ.get("RASA_DUCKLING_HTTP_URL"):
            return os.environ["RASA_DUCKLING_HTTP_URL"]

        return "http://localhost:8000"

    def _duckling_parse(self, text: Text, reference_time: int) -> List[Dict[Text, Any]]:
        """Sends the request to the duckling server and parses the result.
        Args:
            text: Text for duckling server to parse.
            reference_time: Reference time in milliseconds.
        Returns:
            JSON response from duckling server with parse data.
        """
        parse_url = self._url() + "/parse"
        try:
            payload = self._payload(text, reference_time)
            headers = {
                "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
            }
            response = requests.post(
                parse_url,
                data=payload,
                headers=headers,
                timeout=self.component_config.get("timeout"),
            )
            if response.status_code == 200:
                return response.json()
            else:
                logger.error(
                    f"Failed to get a proper response from remote "
                    f"duckling at '{parse_url}. Status Code: {response.status_code}. Response: {response.text}"
                )
                return []
        except (
            requests.exceptions.ConnectionError,
            requests.exceptions.ReadTimeout,
        ) as e:
            logger.error(
                "Failed to connect to duckling http server. Make sure "
                "the duckling server is running/healthy/not stale and the proper host "
                "and port are set in the configuration. More "
                "information on how to run the server can be found on "
                "github: "
                "https://github.com/facebook/duckling#quickstart "
                "Error: {}".format(e)
            )
            return []

    def process(self, message: Message, **kwargs: Any) -> None:

        if self._url() is not None:
            reference_time = self._reference_time_from_message(message)
            matches = self._duckling_parse(message.text, reference_time)
            all_extracted = convert_duckling_format_to_rasa(matches)
            dimensions = self.component_config["dimensions"]
            extracted = SofieHTTPExtractor.filter_irrelevant_entities(
                all_extracted, dimensions
            )
        else:
            extracted = []
            raise_warning(
                "Duckling HTTP component in pipeline, but no "
                "`url` configuration in the config "
                "file nor is `RASA_DUCKLING_HTTP_URL` "
                "set as an environment variable. No entities will be extracted!",
                docs=DOCS_URL_COMPONENTS + "#sofiehttpextractor",
            )

        extracted = self.add_extractor_name(extracted)
        message.set(ENTITIES, message.get(ENTITIES, []) + extracted, add_to_output=True)

    def persist(self, file_name: Text, model_dir: Text) -> Optional[Dict[Text, Any]]:
        """Persist this component to disk for future loading."""
        pass

    @classmethod
    def load(
        cls,
        meta: Dict[Text, Any],
        model_dir: Text = None,
        model_metadata: Optional[Metadata] = None,
        cached_component: Optional["SofieHTTPExtractor"] = None,
        **kwargs: Any,
    ) -> "SofieHTTPExtractor":

        language = model_metadata.get("language") if model_metadata else None
        return cls(meta, language)
