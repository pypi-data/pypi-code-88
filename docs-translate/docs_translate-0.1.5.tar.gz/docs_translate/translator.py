from translators import apis  # type: ignore

from langdetect import detect  # type: ignore
from langdetect.lang_detect_exception import LangDetectException  # type: ignore

from docs_translate import const
from docs_translate.exceptions import UnknownServiceError

from docs_translate.google_v2 import is_detected


def get_translator_by_service_name(service_name: str):
    translator_class = const.TRANSLATOR_BY_SERVICE_NAME.get(service_name)
    if translator_class is None:
        raise UnknownServiceError(service_name)
    return translator_class


def is_untranslated_paragraph(service_name: str, line: str, source_lang: object) -> bool:
    """
    Call the language detect function of each translate API
    :rtype: bool
    """
    if service_name == const.TRANSLATION_SERVICE_GOOGLE_V2:
        return is_detected(line, source_lang)
    else:
        end_words = int(len(source_lang)/4)
        try:
            return detect(line) == source_lang or detect(line) == source_lang[-end_words:]
        except LangDetectException:
            return False
