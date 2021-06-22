from pangeamt_nlp.processor.base.validator_base import ValidatorBase
from pangeamt_nlp.seg import Seg
import re


class NoLinesWithUKDatesVal(ValidatorBase):
    NAME = "no_lines_with_uk_dates_val"

    DESCRIPTION_TRAINING = """
            Filter English with UK dates
        """

    DESCRIPTION_DECODING = """
            Validators do not apply to decoding.
        """

    def __init__(self, src_lang: str, tgt_lang: str, only_english=False) -> None:
        super().__init__(src_lang, tgt_lang)
        self.only_english=only_english

    def validate(self, seg: Seg) -> bool:
        if  self.only_english and  (self.src_lang == 'en' or self.tgt_lang == 'en'):
                if self.src_lang == 'en':
                        UK_dates = re.findall(r"([0-3]{0,1}[0-9]){1}(((th|nd|rd)?( of)?[\s]?)|(-))(?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sept(?:ember)?|Sep(?:tember)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)((,?\s?)|(-))?(([0-9]{4})|([0-9]{2}))?", seg.src)
                else:
                        UK_dates = re.findall(r"([0-3]{0,1}[0-9]){1}(((th|nd|rd)?( of)?[\s]?)|(-))(?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sept(?:ember)?|Sep(?:tember)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)((,?\s?)|(-))?(([0-9]{4})|([0-9]{2}))?", seg.tgt)

        if len(UK_dates) > 0:
            return False
        return True
