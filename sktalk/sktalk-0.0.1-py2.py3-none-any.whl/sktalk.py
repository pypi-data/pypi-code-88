"""Main module."""

import pandas as pd
import regex as re

def clean(df):
## lowercase
  df['utterance'] = df['utterance'].str.lower()
## overlap
  df['utterance'] = [re.sub('\<u .*trans="overlap".*\>\n', "tag_overlap ", str(x)) for x in df['utterance']]
## u open tag
  df['utterance'] = [re.sub('\<u .*\>\n', "", str(x)) for x in df['utterance']]
## u close tag
  df['utterance'] = [re.sub('\<\/u\>\n', "", str(x)) for x in df['utterance']]
## w open tag
  df['utterance'] = [re.sub('\<w class=".*" lemma=".*" pos=".*" usas=".*"\>', "", str(x)) for x in df['utterance']]
## w close tag
  df['utterance'] = [re.sub('\<\/w\>\n', " ", str(x)) for x in df['utterance']]
## laugh tag
  df['utterance'] = [re.sub('\<vocal desc="laugh" \/\>\n', " tag_laugh ", str(x)) for x in df['utterance']]
## sigh tag
  df['utterance'] = [re.sub('\<vocal desc="sigh" \/\>\n', " tag_sigh ", str(x)) for x in df['utterance']]
## gasp tag
  df['utterance'] = [re.sub('\<vocal desc="gasp" \/\>\n', " tag_gasp ", str(x)) for x in df['utterance']]
## nonsense tag
  df['utterance'] = [re.sub('\<vocal desc="nonsense" \/\>\n', " tag_nonsense ", str(x)) for x in df['utterance']]
## whistle tag
  df['utterance'] = [re.sub('\<vocal desc="whistle" \/\>\n', " tag_whistle ", str(x)) for x in df['utterance']]
## sneeze tag
  df['utterance'] = [re.sub('\<vocal desc="sneeze" \/\>\n', " tag_sneeze ", str(x)) for x in df['utterance']]
## cough tag
  df['utterance'] = [re.sub('\<vocal desc="cough" \/\>\n', " tag_cough ", str(x)) for x in df['utterance']]
## yawn tag
  df['utterance'] = [re.sub('\<vocal desc="yawn" \/\>\n', " tag_yawn ", str(x)) for x in df['utterance']]
## misc vocal tag
  df['utterance'] = [re.sub('\<vocal desc=".*" \/\>\n', "", str(x)) for x in df['utterance']]
## singing starts tag
  df['utterance'] = [re.sub('\<shift new="singing" \/\>\n', " tag_startsinging ", str(x)) for x in df['utterance']]
## singing stops tag
  df['utterance'] = [re.sub('\<shift new="normal" \/\>\n', " tag_stopsinging ", str(x)) for x in df['utterance']]
## event full
  #df['utterance'] = [re.sub('\<event desc="', " tag_event", str(x)) for x in df['utterance']]
## event
  df['utterance'] = [re.sub('\<event desc="', " tag_event_", str(x)) for x in df['utterance']]
## foreign starts tag full         
  #df['utterance'] = [re.sub('\<foreign lang="\w\w\w"\>', " tag_inforeign " , str(x)) for x in df['utterance']]
## foreign starts tag 
  df['utterance'] = [re.sub('\<foreign lang="', " tag_inforeign_" , str(x)) for x in df['utterance']]
## foreign stops tag 
  df['utterance'] = [re.sub('\<\/foreign\>\n', " ", str(x)) for x in df['utterance']] #" #endforeign "
## foreign stops tag
  df['utterance'] = [re.sub('--foreignword', " tag_foreignword ", str(x)) for x in df['utterance']] #" #foreignword "
## pause long to short
  df['utterance'] = [re.sub('\<pause dur="long" \/\>', '<pause dur="short" />', str(x)) for x in df['utterance']]
## pause tag
  df['utterance'] = [re.sub('\<pause dur="short" \/\>\n', " tag_pause ", str(x)) for x in df['utterance']]
 ## truncation open tags
  df['utterance'] = [re.sub('\<trunc\>\n', " ", str(x)) for x in df['utterance']]
 ## truncation close tags
  df['utterance'] = [re.sub('\<\/trunc\>\n', " tag_trunc ", str(x)) for x in df['utterance']] #" #trunc "
## unclear tags
  df['utterance'] = [re.sub('\<\/?unclear\>\n', " ", str(x)) for x in df['utterance']]
## unclear words tag
  df['utterance'] = [re.sub('--unclearword', " tag_unclearword ", str(x)) for x in df['utterance']]
## anon name tag
  df['utterance'] = [re.sub('(--anonnamef)|(--anonnamem)|(--anonnamen)', " tag_name ", str(x)) for x in df['utterance']]
## anon place tag
  df['utterance'] = [re.sub('--anonplace', " tag_place ", str(x)) for x in df['utterance']]
## anon address tag
  df['utterance'] = [re.sub('--anonaddress', " tag_address ", str(x)) for x in df['utterance']]
## anon misc personal info tag
  df['utterance'] = [re.sub('--anonmiscpersonalinfo', " tag_personalinfo ", str(x)) for x in df['utterance']]
## anon date of birth tag
  df['utterance'] = [re.sub('--anondateofbirth', " tag_dateofbirth ", str(x)) for x in df['utterance']]
## anon email tag
  df['utterance'] = [re.sub('--anonemail', " tag_email", str(x)) for x in df['utterance']]
## anon financial details tag
  df['utterance'] = [re.sub('--anonfinancialdetails', " tag_financial ", str(x)) for x in df['utterance']]
## anon social media name tag
  df['utterance'] = [re.sub('--anonsocialmedianame', " tag_socialmedianame ", str(x)) for x in df['utterance']]
## anon telephone number tag
  df['utterance'] = [re.sub('--anontelephonenumber', " tag_phonenumber ", str(x)) for x in df['utterance']]
## anon other tags
  df['utterance'] = [re.sub('--anon\w*\b', " tag_anon ", str(x)) for x in df['utterance']]
## clean mess
  df['utterance'] = [re.sub('"+ \/\>', " ", str(x)) for x in df['utterance']] #event closer
  df['utterance'] = [re.sub('"+\>', " ", str(x)) for x in df['utterance']] #foreign tag start closer
  df['utterance'] = [re.sub('\n', " ", str(x)) for x in df['utterance']]
## clean extra spaces
  df['utterance'] = [re.sub(' {2,}', " ", str(x)) for x in df['utterance']]
  df['utterance'] = [re.sub('^ ', "", str(x)) for x in df['utterance']]
  df['utterance'] = [re.sub(' $', "", str(x)) for x in df['utterance']]
## rejoin contractions  
  df['utterance'] = [re.sub(" n't", "n't", str(x)) for x in df['utterance']]
  df['utterance'] = [re.sub(" 's", "'s", str(x)) for x in df['utterance']]
  df['utterance'] = [re.sub(" 'll", "'ll", str(x)) for x in df['utterance']]
  df['utterance'] = [re.sub(" 've", "'ve", str(x)) for x in df['utterance']]
  df['utterance'] = [re.sub(" 're", "'re", str(x)) for x in df['utterance']]
  df['utterance'] = [re.sub(" 'm", "'m", str(x)) for x in df['utterance']]
  df['utterance'] = [re.sub(" 'd", "'d", str(x)) for x in df['utterance']]
  df['utterance'] = [re.sub("\bd' ", "d'", str(x)) for x in df['utterance']]
  df['utterance'] = [re.sub(" n ", "n", str(x)) for x in df['utterance']]
  df['utterance'] = [re.sub("- ", " ", str(x)) for x in df['utterance']]
  df['utterance'] = [re.sub("\bgon na\b", "gonna", str(x)) for x in df['utterance']]
  df['utterance'] = [re.sub(" \?", "?", str(x)) for x in df['utterance']]
  return df

################################################################################
## 2. clean tags from already clean utterances in SBNC

def no_tag(df):
  df['utterance'] = [re.sub(r'tag_\w+', "", str(x)) for x in df['utterance']]
  df['utterance'] = [re.sub(r' {2,}', " ", str(x)) for x in df['utterance']]
  df['utterance'] = [re.sub(r' \?', "?", str(x)) for x in df['utterance']]
  df['utterance'] = [re.sub(r'\?{2,}', "?", str(x)) for x in df['utterance']] #
  df['utterance'] = [re.sub(r'^ ', "", str(x)) for x in df['utterance']]
  df['utterance'] = [re.sub(r' $', "", str(x)) for x in df['utterance']]
  df['utterance'] = [re.sub(r'^\?$', "", str(x)) for x in df['utterance']]
  df['utterance'] = [re.sub(r'^\s*$', "", str(x)) for x in df['utterance']]
  df['utterance'].replace('', np.nan, inplace=True)
  df.dropna(axis=0, inplace=True)
  df.reset_index(drop=True, inplace=True)
  return df

################################################################################
## 3. add punctuation

def add_punctuation(df):
  df['utterance'] = [re.sub("(?<!\?)$", ".", str(x)) for x in df['utterance']]
  return df
