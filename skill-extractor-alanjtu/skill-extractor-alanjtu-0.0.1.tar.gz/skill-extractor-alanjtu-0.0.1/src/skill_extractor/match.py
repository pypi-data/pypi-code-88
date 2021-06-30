import pandas as pd
import numpy as np
from termcolor import colored
from tqdm import tqdm
from fuzzywuzzy import fuzz
import re
import spacy

nlp = spacy.load('en_core_web_sm')

emsi = pd.read_csv('emsi_skills_full.csv')
emsi_names = emsi.Name.tolist()

noise = ['paid', 'pay', 'time', 'sex', 'orientation', 'work',
        'location', 'job', 'type', 'national', 'origin', 'member', 'equal',
        'opportunit', 'veteran', 'status', 'gender', 'identity', 'health',
        'insurance', 'remote', 'employ', 'retire', 'part-time'
        'bachelor', 'degree', 'authoriz', 'dental', 'vision', 'full-time',
        'year', 'benefit', 'qualifi', 'applicant', 'marital',
        'schedule', 'flexib', 'parent', 'leave', 'interview',
        'hour', 'shift', 'description', 'saving', 'entry', 'level', 'ideal',
        'candidate', 'disabilit', 'relevant', 'school',
        'salary', 'protect', 'prefer', 'supplement',
        'covid', 'corona', 'accommodat', 'contract', 'bonus', 'professional',
        'demonstrat', 'abilit', 'seek', 'current',
        'responsibilit', 'inclusiv', 'race', 'color', 'creed',
        'religio', 'legal', 'sponsor', 'company', 'junior', 'senior',
        'career', 'assist', 'cover', 'fair', 'value', 'diversity',
        'desire', 'related', 'offer', 'duti', 'essential', 'summary', 'other',
         'educat'] # these noise words are just not relevant

exact_noise = ['medical', 'maternity', 'language', 'application', 'software',
               'user', 'cloud', 'bs', 'material', 'able', 'nice', 'programming',
               'st', 'us', 'ba', 'imagine', 'business', 'id', 'use', 'for', 'nyc',
               'digital', 'web', 'industry', 'project', 'system', 'or', 'standard', 'cs',
               'u.s', 'server', 'basic', 'cd', 'quality', 'electrical', 'visual', 'service',
               'deep', 'pto', 'eeo', 'responsibilities', 'note', 'eoe', 'qualifications',
               'usa', 'embedded', 'gpa', 'boot', 'and', 'ip',
               'finance', 'track', 'direct', 'manufacturing', 'hiv', 'llc', 'vp', 'unit',
               'the', 'you', 'requirements', 'experience', 'required', 'what', 'tv', 'open',
               'ceo', 'dna', 'articulate', 'jun', 'to', 'nasdaq', 'product', 'pm', 'pms', '3d',
               'nyse', 'hr', 'food', 'about', 'mechanical', 'tnt', 'model', 'skills', 'do', 'hsa',
               'be', 'is', 'not', 'we', 'gm', 'who', 'bring', 'ivd', 'cnn',
               'are', 'tbs', 'npi', 'will', 'ar', "you'll", 'hbo'] + \
                ['al', 'ak', 'az', 'ar', 'ca', 'co', 'ct', 'dc', 'de', 'fl', 'ga', 'hi',
                 'id', 'il', 'in', 'ia', 'ks', 'ky', 'la', 'me', 'md', 'ma', 'mi', 'mn',
                 'ms', 'mo', 'mt', 'ne', 'nv', 'nh', 'nj', 'nm', 'ny', 'nc', 'nd', 'oh',
                 'ok', 'or', 'pa', 'ri', 'sc', 'sd', 'tn', 'tx',
                 'ut', 'vt', 'va', 'wa', 'wv', 'wi', 'wy'] # state abbreviations
                # these noise-words, in these exact forms, mess up the Emsi matching


#-------SECTION 1: FUNCTIONS USED FOR PRINTING-------

def find_substring(string, substring):
    """Returns locations of all instances of the substring `substring`
    in the larger string `string`."""
    places = []
    cur_pos = 0
    while True:
        cur_pos = string.find(substring, cur_pos)
        if cur_pos == -1:
            return places
        places.append(cur_pos)
        cur_pos += len(substring) # to treat overlapping text, make this += 1


def find_many(text, string_list):
    """Returns a dictionary where the keys are the locations as tuples
    (start_pos, end_pos) and the values are the elements in `string_list`.
    This essentially runs `find_substring` for every element in `string_list`
    and creates a dictionary out of it. Kind of a dumb function."""
    loc_dict = {}
    for string in string_list:
        places = find_substring(text, string)
        for loc in places:
            loc_dict[(loc, loc+len(string))] = string
            # using tuples as keys allows different-grammed names starting at the same location to be distinct entries
    return loc_dict


colors = ['red', 'blue', 'green']

def colored_print(text, loc_dict):
    """Will color all strings in the dict `words`
    if they appear in the document. A very ugly function but
    it's not easy to print colored text in Python interface!"""
    loc_dict = dict(sorted(loc_dict.items()))
    final_string = ''
    cur_pos = 0
    for idx, key in enumerate(loc_dict):
        if key[0] >= cur_pos:
            final_string += text[cur_pos:key[0]] # append all text that comes before the word
            # if this word's length extends into the next word!
            if (idx < len(loc_dict) - 1) and (key[1] > list(loc_dict)[idx+1][0]): # edited
                final_string += colored(text[key[0]:list(loc_dict)[idx+1][0]], colors[loc_dict[key].count(' ')])
                cur_pos = list(loc_dict)[idx+1][0]
            else:
                final_string += colored(text[key[0]:key[1]], colors[loc_dict[key].count(' ')])
                cur_pos = key[1]
    final_string += text[cur_pos:]
    print(final_string)


# -------SECTION 2: FUNCTIONS USED FOR SKILL EXTRACTION-------

end_punct = '.,:;!?()'

def discretize_single(text):
    """Returns a list of all individual words in the document,
    removing stop words and other irrelevant dust. Use this function
    only for 1-gram matching."""
    singles = text.split('\n')
    singles = '. '.join(singles)
    singles = singles.split('/')
    singles = ', '.join(singles)
    singles = singles.split(' ')
    singles = [word.rstrip(end_punct).lstrip(end_punct[1:]) for word in singles] # avoid getting rid of period in .NET
    singles = [word for word in singles if word == 'C' or (len(word)>1 and (word[0].isupper() or word[1].isupper()))]
    # chooses just the capitalized words that are longer than one letter, or the programming language C
    singles_final = []
    for word in singles:
        if (nlp(word)[0].is_stop and not word.isupper()) or any(elem in word.lower() for elem in noise) \
          or any(elem == word.lower() for elem in exact_noise):
            pass
        else:
        # chooses non-stop and all-caps words
            singles_final.append(word)
    return list(set(singles_final)) # don't want repeats!!


def discretize_multi(text):
    """Returns a list of all individual words in the document,
    without removing any words. Use this function only for multi-gram
    matching, i.e. n-gram matching where n >= 2."""
    singles = text.split('\n')
    singles = '. '.join(singles)
    singles = singles.split('/')
    singles = ', '.join(singles)
    singles = singles.split(' ')
    singles = [word.lower() for word in singles if len(word)>1 or word.isalpha()]
    return singles


def glue(singles, gram_size):
    """Takes in a list of single words and returns a list of n-grams,
    where n = gram_size, having taken out those with punctuation marks
    in the middle."""
    glued = []
    if gram_size == 2:
        for i in range(len(singles)-1):
            if (singles[i][-1] not in end_punct) and (singles[i+1][0] not in end_punct):
                glued.append(singles[i].strip(end_punct) + ' ' + singles[i+1].strip(end_punct))
        return glued
    elif gram_size == 3:
        for i in range(len(singles)-2):
            if (singles[i][-1] not in end_punct) and (singles[i+1][0] not in end_punct) and \
              (singles[i+1][-1] not in end_punct) and (singles[i+2][0] not in end_punct):
                glued.append(singles[i].strip(end_punct) + ' ' + singles[i+1].strip(end_punct)
                             + ' ' + singles[i+2].strip(end_punct))
        return glued
    else:
        raise NameError('Gram size not supported.')


def remove_stop(glued):
    """Removes n-grams, where n >= 2, for which an outer word is a
    stop word (is, the, etc.) or which contains a noise word."""
    no_stop = []
    for string in glued:
        text = nlp(string)
        stops = [token.is_stop for token in text]
        if not stops[0] and not stops[-1] and not any(elem in string for elem in noise):
            no_stop.append(string)
    return no_stop


def match_single(text):
    single_list = discretize_single(text)
    matched = []
    for word in tqdm(single_list):
        for name in emsi_names:
            # 1st test: remove parentheses and try
            no_par = re.sub("\(.*?\)", "", name).strip() # removes all text within parentheses
            if fuzz.ratio(word.lower(), no_par.lower()) == 100:
                if len(matched) == 0 or name not in np.array(matched)[:,1]:
                    # if we don't yet have the Emsi skill
                    matched.append((word, name, 200.)) # how to set confidence score for single words?
                break
        if len(matched) == 0 or word not in np.array(matched)[:,0]:
            for name in emsi_names:
                # 3rd test: take only the stuff in the parentheses (in case abbreviation is in there)
                if name.find("(") >= 0:
                    in_par = name[name.find("(")+1:name.find(")")]
                    if any(i.isupper() for i in in_par[1:]) and word.lower() == in_par.lower():
                        # don't want to catch "Quality" in parentheses, for example
                        if len(matched) == 0 or name not in np.array(matched)[:,1]:
                            matched.append((word, name, 190.))
                        break
        # 4th test: take all-caps no matter what
        if (len(matched) == 0 or word not in np.array(matched)[:,0]) and word.strip("’'s").isupper():
            matched.append((word, '', 165.))
    return matched


def match_multi(text):
    pair_list = remove_stop(glue(discretize_multi(text), 2))
    trio_list = remove_stop(glue(discretize_multi(text), 3))
    matched = []
    for pair in tqdm(pair_list):
        candidates = {}
        for name in emsi_names:
            Ratio = fuzz.ratio(pair.lower(), name.lower())
            if Ratio >= 65:
                P_Ratio = fuzz.partial_ratio(pair.lower(), name.lower())
                if Ratio + P_Ratio >= 175 or P_Ratio >= 95:
                    candidates[name] = Ratio + P_Ratio + P_Ratio/1000. # last term is to break ties
        if len(candidates) > 0:
            best_match = sorted(candidates, key=candidates.get, reverse=True)[0]
            if len(matched) == 0 or best_match not in np.array(matched)[:,1]:
                # if we don't yet have the Emsi skill
                matched.append((pair, best_match, candidates[best_match]))
            else:
                # choose whichever one has a higher score
                old_tuple = matched[list(np.array(matched)[:,1]).index(best_match)]
                if candidates[best_match] > old_tuple[2]:
                    matched.remove(old_tuple)
                    matched.append((pair, best_match, candidates[best_match]))
    for trio in tqdm(trio_list):
        candidates = {}
        for name in emsi_names:
            Ratio = fuzz.ratio(trio.lower(), name.lower())
            if Ratio >= 70:
                P_Ratio = fuzz.partial_ratio(trio.lower(), name.lower())
                if Ratio + P_Ratio >= 180 or P_Ratio >= 95:
                    candidates[name] = Ratio + P_Ratio + P_Ratio/1000.
        if len(candidates) > 0:
            best_match = sorted(candidates, key=candidates.get, reverse=True)[0]
            if len(matched) == 0 or best_match not in np.array(matched)[:,1]:
                # if we don't yet have the Emsi skill
                matched.append((trio, best_match, candidates[best_match]))
            else:
                # choose whichever one has a higher score
                old_tuple = matched[list(np.array(matched)[:,1]).index(best_match)]
                if candidates[best_match] > old_tuple[2]:
                    matched.remove(old_tuple)
                    matched.append((trio, best_match, candidates[best_match]))
    return matched # this return is lowercase


#-------SECTION 3: COMBINING THE TWO-------

def tag_extract(text):
    """Returns a set of all skills that were found in the text.
    In other words, does everything."""
    text_lower = text.lower() + '  ' # add extra space at end to prevent overflow string indexing
    found_multi = match_multi(text)
    found_single = match_single(text)
    locs_multi = find_many(text_lower, np.array(found_multi)[:,0])
    locs_single = find_many(text + '  ', np.array(found_single)[:,0])
    locs_combined = dict(sorted(({**locs_single, **locs_multi}).items()))
    colored_print(text, locs_combined)
    return pd.DataFrame(np.array(found_multi + found_single), columns=['Text', 'Emsi', 'Score']).sort_values(by=['Score'],
                                                                                    ascending=False, ignore_index=True)
