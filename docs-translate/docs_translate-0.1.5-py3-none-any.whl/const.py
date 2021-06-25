from translators import bing, deepl, google, yandex  # type: ignore
from docs_translate.google_v2 import google_v2

TRANSLATION_SERVICE_YANDEX = 'Yandex'
TRANSLATION_SERVICE_GOOGLE = 'Google'
TRANSLATION_SERVICE_BING = 'Bing'
TRANSLATION_SERVICE_DEEPL = 'Deepl'
TRANSLATION_SERVICE_GOOGLE_V2 = 'Google_v2'

TRANSLATOR_BY_SERVICE_NAME = {
    TRANSLATION_SERVICE_YANDEX: yandex,
    TRANSLATION_SERVICE_GOOGLE: google,
    TRANSLATION_SERVICE_BING: bing,
    TRANSLATION_SERVICE_DEEPL: deepl,
    TRANSLATION_SERVICE_GOOGLE_V2: google_v2
}
