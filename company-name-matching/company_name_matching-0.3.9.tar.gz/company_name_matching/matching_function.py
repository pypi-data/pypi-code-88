import pandas as pd
import numpy as np
import os
import csv
import json

from fuzzywuzzy import fuzz
import Levenshtein
from enum import IntFlag, IntEnum
import unicodedata, unittest
import importlib.resources as pkg_resources


class MatchingResult:
    def __init__(self, score=0):
        self.score = score


class MatcherMixin:

    def match(self, lhs, rhs, original_lhs, original_rhs, **parameters):
        new_lhs, new_rhs = self.normalize(lhs, rhs, original_lhs, original_rhs, **parameters)
        return self.compare(new_lhs, new_rhs, original_lhs, original_rhs, **parameters), new_lhs, new_rhs

    def compare(self, lhs, rhs, original_lhs, original_rhs, **parameters):
        return None

    def normalize(self, lhs, rhs, original_lhs, original_rhs, **parameters):
        return lhs, rhs


class ComparerMixin(MatcherMixin):

    def compare(self, lhs, rhs, original_lhs, original_rhs, **parameters):
        return self.compare(lhs, rhs, original_lhs, original_rhs, **parameters), lhs, rhs


class NormalizerMixin(MatcherMixin):

    def normalize(self, lhs, rhs, original_lhs, original_rhs, **parameters):
        return self.normalize(lhs, rhs, original_lhs, original_rhs, **parameters)


class TokenCategoryComparer(ComparerMixin):
    '''If some abbreviations are remaining'''
    def compare(self, lhs, rhs, original_lhs, original_rhs, **parameters):
        abbreviations_lhs = lhs[0]
        company_words_lhs = lhs[1]
        abbreviations_rhs = rhs[0]
        company_words_rhs = rhs[1]

        number_of_entity_words = len(abbreviations_lhs) + len(company_words_lhs) + len(abbreviations_rhs) + len(
                                                                                                    company_words_rhs)

class OtherWordsComparer(ComparerMixin):

    def compare(self, lhs, rhs, original_lhs, original_rhs, **parameters):
        typographies_in_raw=40
        ratio = fuzz.token_sort_ratio(str(lhs), str(rhs))
        return MatchingResult(ratio)


class LevenshteinComparer(ComparerMixin):

    def compare(self, lhs, rhs, original_lhs, original_rhs, **parameters):
        edit = Levenshtein.distance(lhs, rhs)

        if edit <= parameters.get("maximal_typographies_in_raw", 1):
            ratio = self.__ratio_distance(edit, lhs, rhs)
            if edit == 0 and len(lhs) == len(rhs):
                return MatchingResult(ratio)
            else:
                return MatchingResult(ratio)

    def __ratio_distance(self, edit_score, lhs, rhs):
        if edit_score == 0:
            return 100
        else:
            len_sum = len(lhs) + len(rhs)
            return int(((len_sum - edit_score) / len_sum) * 100)


class ElfType(IntEnum):
    '''first column of the elf_company dataset'''
    Abbreviation = 0,
    LocalName = 1, # = company word
    TransliteratedAbbreviation = 2,
    TransliteratedLocalName = 3,
    Unknown = 5


class Elf:
    def __init__(self):
        content = pkg_resources.open_text('company_name_matching', 'elf_company.csv')
        self.__elf_database = self.__read_from_csv(content)

    def get(self, elf_type, token, country='AA'):
        country_mapping = self.__elf_database[country]
        if country_mapping[elf_type] is None:
            return None
        else:
            return country_mapping[elf_type].get(token)

    def __read_from_csv(self, content):
        elf_database = {}
        spamreader = csv.reader(content, delimiter=',', quotechar='"', strict=True)
        for tokens in spamreader:

            country = tokens[0]
            elf_type = ElfType(int(tokens[1]))
            word = tokens[2]
            elfs = set(tokens[3].split(';'))

            country_mapping = elf_database.get(country, None)
            if country_mapping is None:
                word_mapping = {}
                word_mapping[word] = elfs
                country_mapping = [None for _ in range(4)]
                country_mapping[elf_type] = word_mapping
            else:
                word_mapping = country_mapping[elf_type]
                if word_mapping is not None:
                    word_mapping[word] = elfs
                else:
                    word_mapping = { word: elfs }
                country_mapping[elf_type] = word_mapping

            elf_database[country] = country_mapping
        return elf_database


class UnicodeNormalizer(NormalizerMixin):

    def normalize(self, lhs, rhs, original_lhs, original_rhs, **parameters):
        normalized_lhs = self.__normalize(lhs)
        normalized_rhs = self.__normalize(rhs)
        return normalized_lhs, normalized_rhs

    def __normalize(self, input_str):
        nfkd_form = unicodedata.normalize('NFKD', input_str.casefold())
        return u"".join([c for c in nfkd_form if not unicodedata.combining(c)])


class TokenCategoryNormalizer(NormalizerMixin):

    def normalize(self, lhs, rhs, original_lhs, original_rhs, **parameters):
        new_lhs = self.__categorize_tokens(lhs, **parameters)
        new_rhs = self.__categorize_tokens(rhs, **parameters)
        return new_lhs, new_rhs

    def __categorize_tokens(self, tokens, **parameters):
        abbreviations = {} # abbreviations: ltd, ...
        company_words = {} # corporation, limited, ...
        others = [] # if no abbreviation and no company words

        elf = parameters["ELF"]
        transliterate_function = parameters.get("transliterate", None)

        for token in tokens:
            category, elfs = self.__categorize_token(token, parameters)
            if category == ElfType.Abbreviation or category == ElfType.TransliteratedAbbreviation:
                abbreviations[token] = elfs
            elif category == ElfType.LocalName or category == ElfType.TransliteratedLocalName:
                company_words[token] = elfs
            else:
                if transliterate_function is not None:
                    transliteration = transliterate_function(token)

            others.append(token)
        return abbreviations, company_words, others

    def __categorize_token(self, token, parameters):

        elf = parameters["ELF"]
        transliterate_function = parameters.get("transliterate", None)

        abbreviations_elfs = elf.get(ElfType.Abbreviation, token)
        local_names_elfs = elf.get(ElfType.LocalName, token)

        if abbreviations_elfs is None and local_names_elfs is None:
            if transliterate_function is None:
                return ElfType.Unknown, None
            
            transliterated_token = transliterate_function(token)
            transliterated_abbreviations_elfs = elf.get(ElfType.TransliteratedAbbreviation, transliterated_token)
            transliterated_local_names_elfs = elf.get(ElfType.TransliteratedLocalName, transliterated_token)
            if transliterated_abbreviations_elfs is None and transliterated_local_names_elfs is None:
                return ElfType.Unknown, None
            elif transliterated_abbreviations_elfs is None and transliterated_local_names_elfs is not None:
                return ElfType.LocalName, transliterated_local_names_elfs
            elif transliterated_abbreviations_elfs is not None and transliterated_local_names_elfs is None:
                return ElfType.Abbreviation, transliterated_abbreviations_elfs
            else:
                if len(transliterated_abbreviations_elfs) > len(transliterated_local_names_elfs):
                    return ElfType.Abbreviation, transliterated_abbreviations_elfs
                else:
                    return ElfType.LocalName, transliterated_local_names_elfs
            
        elif abbreviations_elfs is None and local_names_elfs is not None:
            return ElfType.LocalName, local_names_elfs
        elif abbreviations_elfs is not None and local_names_elfs is None:
            return ElfType.Abbreviation, abbreviations_elfs
        else:
            if len(abbreviations_elfs) > len(local_names_elfs):
                return ElfType.Abbreviation, abbreviations_elfs
            else:
                return ElfType.LocalName, local_names_elfs


class StripNormalizer(NormalizerMixin):

    def normalize(self, lhs, rhs, original_lhs, original_rhs, **parameters):
        return lhs.strip(), rhs.strip()


class SplitNormalizer(NormalizerMixin):

    def normalize(self, lhs, rhs, original_lhs, original_rhs, **parameters):
        return lhs.split(), rhs.split()


class OtherWordsAbbreviationNormalizer(NormalizerMixin):

    def __init__(self, abbreviations):
        self.abbreviations = abbreviations

    def normalize(self, lhs, rhs, original_lhs, original_rhs, **parameters):
        original_length = len(lhs)
        lhs_to_remove = set()
        rhs_to_remove = set()
        considered_lhs = [False for _ in range(len(lhs))]
        considered_rhs = [False for _ in range(len(rhs))]
        for index, l in enumerate(lhs):
            others = self.abbreviations.get(l, None)
            if others is not None:
                for other in others:
                    if other in rhs:
                        pos = rhs.index(other)
                        if pos != -1 and considered_rhs[pos] == False:
                            considered_lhs[index] = True
                            considered_rhs[pos] = True
                            lhs_to_remove.add(l)
                            rhs_to_remove.add(other)

        for index, l in enumerate(rhs):
            if not considered_rhs[index]:
                others = self.abbreviations.get(l, None)
                if others is not None:
                    for other in others:
                        if other in lhs:
                            pos = lhs.index(other)
                            if pos != -1 and considered_lhs[pos] == False:
                                considered_lhs[index] = True
                                considered_rhs[pos] = True
                                lhs_to_remove.add(l)
                                rhs_to_remove.add(other)

        for to_remove in lhs_to_remove:
            lhs.remove(to_remove)
        for to_remove in rhs_to_remove:
            rhs.remove(to_remove)
        return lhs, rhs


class MisplacedCharacterNormalizer(NormalizerMixin):

    def normalize(self, lhs, rhs, original_lhs, original_rhs, **parameters):
        normalized_lhs = self.__normalize(lhs)
        normalized_rhs = self.__normalize(rhs)
        return normalized_lhs, normalized_rhs

    def __normalize(self, input_str):
        final = []
        tokens = input_str.split()
        for token in tokens:
            if '.' in token:
                parts = token.split('.')
                # If there are more than 2 dots, it's likely to be initials.
                if len(parts) == 2:
                    final.append(parts[0])
                    final.append(parts[1])
                else:
                    final.append(token.replace('.', ''))
            elif '&' in token and token != '&':
                parts = token.split('&')
                # If there are more than 2 parts, I don't know what it can be oO.
                if len(parts) == 2:
                    final.append(parts[0])
                    final.append('&')
                    final.append(parts[1])
                else:
                    final.append(token.replace('&', ''))
            else:
                final.append(token)
        return u' '.join(final)



class KeepOtherWordsNormalizer(NormalizerMixin):

    def normalize(self, lhs, rhs, original_lhs, original_rhs, **parameters):
        normalized_lhs = lhs[2]
        normalized_rhs = rhs[2]
        lhs_all_abrv = lhs[0].copy()
        lhs_all_abrv.update(lhs[1])
        rhs_all_abrv = rhs[0].copy()
        rhs_all_abrv.update(rhs[1])
        for elements_lhs in lhs_all_abrv.values():
            for element_lhs in elements_lhs:
                if element_lhs == "TY0P":
                    lhs_remove = [k for k, v in lhs_all_abrv.items() if element_lhs in v]
                    if len(lhs_remove) > 0:
                        normalized_lhs.remove(lhs_remove[0])
                for elements_rhs in rhs_all_abrv.values():
                    if element_lhs in elements_rhs:
                        lhs_element_lhs_to_remove = [k for k, v in lhs_all_abrv.items() if element_lhs in v]
                        if len(lhs_element_lhs_to_remove) > 0:
                            if lhs_element_lhs_to_remove[0] in normalized_lhs:
                                normalized_lhs.remove(lhs_element_lhs_to_remove[0])
                        rhs_element_lhs_to_remove = [k for k, v in rhs_all_abrv.items() if element_lhs in v]
                        if len(rhs_element_lhs_to_remove) > 0:
                            if rhs_element_lhs_to_remove[0] in normalized_rhs:
                                normalized_rhs.remove(rhs_element_lhs_to_remove[0])
        for elements_rhs in rhs_all_abrv.values():
            for element_rhs in elements_rhs:        
                if element_rhs == "TY0P":
                    rhs_remove = [k for k, v in rhs_all_abrv.items() if element_rhs in v]
                    if len(rhs_remove) > 0:
                        normalized_rhs.remove(rhs_remove[0])
        return normalized_lhs, normalized_rhs


class CommonAbbreviationNormalizer(NormalizerMixin):
    '''delete abbreviaitons with common tags (between the left & right words'''
    def normalize(self, lhs, rhs, original_lhs, original_rhs, **parameters):
        abbreviations_lhs = lhs[0]
        abbreviations_rhs = rhs[0]
        abbreviations_lhs_to_remove = []
        abbreviations_rhs_to_remove = []
        considered = [False for _ in range(len(rhs))]
        for abbreviation_lhs, elfs_lhs in abbreviations_lhs.items():
            for index, (abbreviation_rhs, elfs_rhs) in enumerate(abbreviations_rhs.items()):
                if not considered[index]:
                    if len(elfs_lhs.intersection(elfs_rhs)) > 0:
                        abbreviations_lhs_to_remove.append(abbreviation_lhs)
                        abbreviations_rhs_to_remove.append(abbreviation_rhs)
                        considered[index] = True
                        break
        for abbreviation_to_remove in abbreviations_lhs_to_remove:
            del abbreviations_lhs[abbreviation_to_remove]
        for abbreviation_to_remove in abbreviations_rhs_to_remove:
            del abbreviations_rhs[abbreviation_to_remove]
        return lhs, rhs


class CharacterNormalizer(NormalizerMixin):

    def __init__(self, meaningless_characters):
        super()
        self.meaningless_characters = meaningless_characters

    def normalize(self, lhs, rhs, original_lhs, original_rhs, **parameters):
        normalized_lhs = self.__normalize(lhs)
        normalized_rhs = self.__normalize(rhs)
        return normalized_lhs, normalized_rhs

    def __normalize(self, input_str, **parameters):
        without_dot = parameters.get("meaningless_characters", self.meaningless_characters)
        return self.__remove(input_str, without_dot)


    def __remove(self, input_str, characters):
        for character in characters:
            input_str = input_str.replace(character, '')

        return input_str


class AndNormalizer(NormalizerMixin):

    def __init__(self, and_words):
        self.and_words = and_words

    def normalize(self, lhs, rhs, original_lhs, original_rhs, **parameters):
        return self.__remove_ands(lhs, rhs)

    def __remove_ands(self, lhs, rhs):
        if not ('&' in lhs or '&' in rhs):
            return lhs, rhs

        if '&' in lhs:
            rhs = list(filter(lambda x: x not in self.and_words, rhs))
            lhs = filter(lambda x: x != '&', lhs)
        if '&' in rhs:
            lhs = filter(lambda x: x not in self.and_words, lhs)
            rhs = filter(lambda x: x != '&', rhs)
        return list(lhs), list(rhs)


class AbbreviationLegalFormNormalizer(NormalizerMixin):
    '''Delete the matches between company words and abbreviations:
    take the (left abbreviations, right company words),
    (left company words, right abbreviations) and look if there is
    an intersection between tags, if association: delete them'''
    def normalize(self, lhs, rhs, original_lhs, original_rhs, **parameters):
        abbreviations_lhs = lhs[0]
        company_words_lhs = lhs[1]
        abbreviations_rhs = rhs[0]
        company_words_rhs = rhs[1]

        original_length = len(abbreviations_lhs) + len(company_words_rhs) + len(abbreviations_rhs) + len(
                                                                                                    company_words_lhs)
        self.__remove_abbreviations_of_company_words(abbreviations_lhs, company_words_rhs)
        self.__remove_abbreviations_of_company_words(abbreviations_rhs, company_words_lhs)

        remaining_length = len(abbreviations_lhs) + len(company_words_rhs) + len(abbreviations_rhs) + len(
                                                                                                    company_words_lhs)
        return lhs, rhs

    def __remove_abbreviations_of_company_words(self, abbreviations, company_words):
        abbreviations_to_remove = set()
        company_words_to_remove = set()
        considered = [False for _ in range(len(company_words))]
        for abbreviation, abbreviation_elfs in abbreviations.items():
            for index, (company_word, company_elfs) in enumerate(company_words.items()):
                if not considered[index]:
                    if len(abbreviation_elfs.intersection(company_elfs)) > 0:
                        abbreviations_to_remove.add(abbreviation)
                        company_words_to_remove.add(company_word)
                        considered[index] = True

        for abbreviation_to_remove in abbreviations_to_remove:
            del abbreviations[abbreviation_to_remove]
        for company_word_to_remove in company_words_to_remove:
            del company_words[company_word_to_remove]

        return abbreviations, company_words


class Pipeline:

    def __init__(self, steps):
        self.steps = steps

    def match(self, lhs, rhs, original_lhs, original_rhs, **parameters):
        for i in range(len(self.steps)):
            result, lhs, rhs = self.steps[i].match(lhs, rhs, original_lhs, original_rhs, **parameters)
            if result is not None:
                return result, lhs, rhs

    def __len__(self):
        return len(self.steps)

def make_pipeline(*steps):
    return Pipeline(steps)


class DefaultMatching:   

    def __init__(self, default_parameters=None):
        if default_parameters is None:
            self.default_parameters = MatchingParameters.default()
        else:
            self.default_parameters = default_parameters

        handle_company_words = make_pipeline(
            SplitNormalizer(), # split words
            TokenCategoryNormalizer(), # associate each word to a word from the elf dataset
            #AbbreviationLegalFormNormalizer(), 
            CommonAbbreviationNormalizer(),
            TokenCategoryComparer(),
            KeepOtherWordsNormalizer(), 
            AndNormalizer(self.default_parameters.and_words),
            OtherWordsAbbreviationNormalizer(self.default_parameters.abbreviations),
            OtherWordsComparer()
        )

        self.__pipeline = make_pipeline(
            UnicodeNormalizer(), 
            CharacterNormalizer(self.default_parameters.meaningless_characters_without_dot), 
            MisplacedCharacterNormalizer(),
            handle_company_words
        )

    def match(self, lhs, rhs, **parameters):
        default_parameters = vars(self.default_parameters)
        default_parameters.update(parameters)
        return self.__pipeline.match(lhs, rhs, lhs, rhs, **default_parameters)[0]



class MatchingParameters:
    __MEANINGLESS_CHARACTERS = ['.', ',', '/', '\\', '\'', '(', ')', '’', '-']

    def __init__(self, typographies_in_raw=1, entity_words_unmatched=2, common_words_unmatched=1, maximal_initialism=5, \
                                    remove_common_abbreviations=True, meaningless_characters=__MEANINGLESS_CHARACTERS):
        self.ELF = Elf()
        self.maximal_typographies_in_raw = typographies_in_raw
        self.maximal_entity_words_unmatched = entity_words_unmatched
        self.maximal_common_words_unmatched = common_words_unmatched
        self.maximal_initialism = maximal_initialism
        self.remove_common_abbreviations = remove_common_abbreviations
        self.meaningless_characters = meaningless_characters
        if '.' in meaningless_characters:
            copy = meaningless_characters[:]
            copy.remove('.')
            self.meaningless_characters_without_dot = copy
        else:
            self.meaningless_characters_without_dot = meaningless_characters
        self.transliterate = None
        self.and_words = ['and', 'und', 'et']
        self.abbreviations = json.load(pkg_resources.open_text('company_name_matching', 'abbreviations.json'))
        #self.abbreviations = json.load(open('data/abbreviations.json'))

    @staticmethod
    def default():
        return MatchingParameters()