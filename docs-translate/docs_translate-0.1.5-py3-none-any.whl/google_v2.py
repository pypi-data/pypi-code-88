from google.cloud import translate_v2 as translate
from google.cloud.translate_v2 import Client
from html import unescape  # >= Python 3.5


class SingletonInstance:
    _instance = None

    @classmethod
    def _get_instance(cls):
        return cls._instance

    @classmethod
    def instance(cls, *args, **kargs):
        cls._instance = cls(*args, **kargs)
        cls.instance = cls._get_instance
        return cls._instance


class _GoogleV2(object):
    _translate_client = None

    @classmethod
    def _get_translate_client(cls) -> Client:
        if not cls._translate_client:
            cls._translate_client = translate.Client()
        return cls._translate_client

    @classmethod
    def translate_v2(cls, src: str, from_language="ko", to_language="en", model="nmt"):
        return unescape(
            cls._get_translate_client().translate(src, target_language=to_language, source_language=from_language,
                                                  model=model)["translatedText"])

    @classmethod
    def is_detected(cls, src, from_language):
        return True if cls._get_translate_client().detect_language(src)['language'] == from_language else False


class GoogleV2(_GoogleV2, SingletonInstance):
    pass


instance = GoogleV2.instance()
google_v2 = instance.translate_v2
is_detected = instance.is_detected
