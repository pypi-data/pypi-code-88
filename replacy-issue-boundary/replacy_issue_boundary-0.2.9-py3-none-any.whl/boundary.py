from typing import List

from spacy.tokens import Span


class ReplacyPipelineOrderError(RuntimeError):
    pass


class ESpan(Span):
    @staticmethod
    def create_instance(span: Span):
        espan = ESpan(span.doc, span.start, span.end, span.label, span.vector, span.vector_norm, span.kb_id)
        espan.start_character = espan.start_char
        espan.end_character = espan.end_char
        espan.fixed_text = espan.text
        espan.original_text = espan.text
        if Span.has_extension("suggestions"):
            espan.original_suggestions = span._.suggestions
            espan.is_deletion = len(span._.suggestions) and span._.suggestions[0] == ""
        else:
            espan.original_suggestions = []
            espan.is_deletion = False
        return espan

    def __getattribute__(self, item):
        if item == 'start_char' and hasattr(self, 'start_character'):
            return self.start_character
        elif item == 'end_char' and hasattr(self, 'end_character'):
            return self.end_character
        elif item == 'text' and hasattr(self, 'fixed_text'):
            return self.fixed_text
        else:
            return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        if key == 'start_char':
            self.start_character = value
            self.fixed_text = self.doc.text[self.start_character:self.end_character]
        elif key == 'end_char':
            self.end_character = value
            self.fixed_text = self.doc.text[self.start_character:self.end_character]
        else:
            object.__setattr__(self, key, value)


class IssueBoundary:
    def __init__(self, name="IssueBoundary"):
        self.name = name

    @staticmethod
    def _would_cause_lowercase_first_letter(span: Span) -> bool:
        return (
                span.start_char == 0
                and len(span._.suggestions) > 0
                and span._.suggestions[0] == ""
        )

    @staticmethod
    def _would_cause_double_space(span: Span) -> bool:
        return (
                span.start_char > 0
                and span.end_char < len(span.doc.text)
                and len(span._.suggestions) > 0
                and span.doc.text[span.start_char - 1] == " "
                and span.doc.text[span.end_char] == " "
                and span._.suggestions[0] in ["", ","]
        )

    @staticmethod
    def _would_cause_space_at_start(span: Span) -> bool:
        return (
                span.start_char == 0
                and span.end_char < len(span.doc.text)
                and span.doc.text[span.end_char] == ' '
                and len(span._.suggestions) > 0
                and span._.suggestions[0] == ""
        )

    @staticmethod
    def _would_cause_double_comma(span: Span) -> bool:
        return (
                (
                        (
                                span.start_char > 0
                                and span.doc.text[span.start_char - 1] == ","
                        )
                        or
                        (
                                span.start_char > 1
                                and span.doc.text[span.start_char - 1] == " "
                                and span.doc.text[span.start_char - 2] == ","
                        )
                )
                and (span.end_char < len(span.doc.text) and span.doc.text[span.end_char] == ",")
                and len(span._.suggestions) > 0
                and span._.suggestions[0] == ""
        )

    @staticmethod
    def _would_cause_comma_start(span: Span) -> bool:
        return (
                span.start_char == 0
                and span.end_char < len(span.doc.text)
                and span.doc.text[span.end_char] == ","
                and len(span._.suggestions) > 0
                and span._.suggestions[0] == ""
        )

    @staticmethod
    def _is_comma_replacement_that_could_be_deletion(span: Span) -> bool:
        return (
                (span.text[0] == "," or span.text[-1] == ",")
                and len(span._.suggestions) > 0
                and span._.suggestions[0] == ","
        )

    @staticmethod
    def _comma_replacement_to_deletion(span: Span):
        """
        rather than suggest replacing 'some long string,' with ',', it looks nicer in the front end
        if we replace 'some long string' with '' - because the empty string is a magic replacement
        this attempts to figure out how to move the span boundaries to make this happen
        """
        first_char = span.doc.text[span.start_char]
        second_char = span.doc.text[span.start_char + 1]
        second_to_last_char = span.doc.text[span.end_char - 2]
        last_char = span.doc.text[span.end_char - 1]
        if first_char == ",":
            span.start_char += 1
        elif first_char == " " and second_char == ",":
            span.start_char += 2
        elif second_to_last_char == "," and last_char == " ":
            span.end_char -= 2
        elif last_char == ",":
            span.end_char -= 1
        span._.suggestions.remove(",")
        if "" not in span._.suggestions:
            span._.suggestions.insert(0, "")
        return span

    @staticmethod
    def _would_cause_parenthesis_space(span: Span) -> bool:
        return (
                span.start_char > 0
                and span.end_char < len(span.doc.text)
                and len(span._.suggestions) > 0
                and span.doc.text[span.start_char - 1] == "("
                and span.doc.text[span.end_char] == " "
                and span._.suggestions[0] in [""]
        )

    @staticmethod
    def _would_cause_space_parenthesis(span: Span) -> bool:
        return (
                span.start_char > 0
                and span.end_char < len(span.doc.text)
                and len(span._.suggestions) > 0
                and span.doc.text[span.start_char - 1] == " "
                and span.doc.text[span.end_char] == ")"
                and span._.suggestions[0] in [""]
        )

    @staticmethod
    def _sanity_check(span: Span) -> Span:
        if span[0].is_sent_start or span.doc.text[span.start_char - 1] == "(":
            # the language model gets confused and sometimes thinks
            # that it makes sense to start a sentence (or a parenthetical) with a comma
            # don't allow this
            if "," in span._.suggestions:
                span._.suggestions.remove(",")
                # now maybe so suggestions are left,
                # so add DELETE operation (i.e. suggest replacement with "")
                if not len(span._.suggestions):
                    span._.suggestions.append("")
        return span

    @staticmethod
    def _drop_comma_when_empty_top(span: Span) -> Span:
        if len(span._.suggestions) > 0 and span._.suggestions[0] == "" and "," in span._.suggestions:
            span._.suggestions.remove(",")
        return span

    def __call__(self, spans: List[Span]) -> List[Span]:
        result = []
        for span in spans:
            span = ESpan.create_instance(span)

            span = IssueBoundary._sanity_check(span)

            if IssueBoundary._would_cause_double_comma(span):
                span.end_char += 1

            if IssueBoundary._would_cause_comma_start(span):
                span.end_char += 1

            if IssueBoundary._would_cause_double_space(span):
                # double space issue, extending issue back one character
                span.start_char -= 1
            elif IssueBoundary._would_cause_space_at_start(span):
                # space at start, extending issue forward one character
                span.end_char += 1

            if IssueBoundary._would_cause_lowercase_first_letter(span):
                # casing issue, extending issue forward one word and uppercasing that word
                doc_text_without_issue = span.doc.text[span.end_char:]
                first_space_index = doc_text_without_issue.find(' ')
                replacement = doc_text_without_issue[0:first_space_index]
                span.end_char += first_space_index
                span._.suggestions = [replacement[0].upper() + replacement[1:]]

            # order matters, must come after _would_cause_lowercase_first_letter
            if IssueBoundary._is_comma_replacement_that_could_be_deletion(span):
                span = IssueBoundary._comma_replacement_to_deletion(span)

            # fix parentheses
            if self._would_cause_parenthesis_space(span):
                span.end_char += 1
            if self._would_cause_space_parenthesis(span):
                span.start_char -= 1

            # only "" or "," can ever be right; so drop comma suggestion, when first one is empty
            span = IssueBoundary._drop_comma_when_empty_top(span)

            result.append(span)

        return sorted(result, key=lambda span: span.start)
