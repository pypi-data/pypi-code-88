# Extention of meaning with disambiguation
from pywsd import disambiguate
import nltk
from nltk.tokenize import word_tokenize
# Extention of meaning with disambiguation
# Extention of meaning with disambiguation
from pywsd import disambiguate
import nltk
from nltk.tokenize import word_tokenize
nltk.download('wordnet')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
# Extention of meaning with disambiguation
def sense(sen):
    allWords=disambiguate(sen)
#     print(allWords)
    new_sen=[]
    for x in allWords:
        if x[0]=='fuck':
            for l in x[1].lemmas():
                if l.name() == 'fuck' or l.name() == 'fucking' or l.name() == 'screw' or l.name() == 'screwing' or l.name() == 'ass' or l.name() == 'nooky' or l.name() == 'nookie' or l.name() == 'piece_of_ass'  or l.name() == 'roll_in_the_hay' or l.name() == 'shag' or l.name() == 'shtup' or l.name() == 'sleep_together' or l.name() == 'roll_in_the_hay' or l.name() == 'make_out'  or l.name() == 'sleep_with' or l.name() == 'get_laid' or l.name() == 'have_sex'  or l.name() == 'be_intimate' or l.name() == 'have_intercourse'  or l.name() == 'screw' or l.name() == 'fuck' or l.name() == 'jazz' or l.name() == 'eff' or l.name() == 'hump' or l.name() == 'lie_with' or l.name() == 'bed'  or l.name() == 'bang'  or l.name() == 'bonk':
                    ns=sen.replace(x[0], l.name())
                    ns=ns.lower()
                    new_sen.append(ns.replace('_', ' '))
        elif x[0]=='love':
            for l in x[1].lemmas():
                if l.name()=='love' or l.name()=='passion' or l.name()=='beloved' or l.name()=='dearest' or l.name()=='honey' or l.name()=='know' or l.name()=='love_life' or l.name()=='have_a_go_at_it' or l.name()=='get_it_on':
                    ns=sen.replace(x[0], l.name())
                    ns=ns.lower()
                    new_sen.append(ns.replace('_', ' '))
        else:
            try: 
                for l in x[1].lemmas():
                        ns=sen.replace(x[0], l.name())
                        ns=ns.lower()
                        new_sen.append(ns.replace('_', ' '))
            except:
                ns=sen.lower()
                new_sen.append(ns.replace('_', ' '))
        new_sen = list(dict.fromkeys(new_sen))
    return new_sen


# Extention of memaning with pos tag
def pos(sen):
    allWords=disambiguate(sen)
    new_sen=[]
    for x in allWords:
        if x[0]=='fuck':
            for l in x[1].lemmas():
                if l.name() == 'fuck' or l.name() == 'fucking' or l.name() == 'screw' or l.name() == 'screwing' or l.name() == 'ass' or l.name() == 'nooky' or l.name() == 'nookie' or l.name() == 'piece_of_ass'  or l.name() == 'roll_in_the_hay' or l.name() == 'shag' or l.name() == 'shtup' or l.name() == 'sleep_together' or l.name() == 'roll_in_the_hay' or l.name() == 'make_out'  or l.name() == 'sleep_with' or l.name() == 'get_laid' or l.name() == 'have_sex'  or l.name() == 'be_intimate' or l.name() == 'have_intercourse'  or l.name() == 'screw' or l.name() == 'fuck' or l.name() == 'jazz' or l.name() == 'eff' or l.name() == 'hump' or l.name() == 'lie_with' or l.name() == 'bed'  or l.name() == 'bang'  or l.name() == 'bonk':
                    ns=sen.replace(x[0], l.name())
                    ns=ns.lower()
                    new_sen.append(ns.replace('_', ' '))
        elif x[0]=='love':
            for l in x[1].lemmas():
                if l.name()=='love' or l.name()=='passion' or l.name()=='beloved' or l.name()=='dearest' or l.name()=='honey' or l.name()=='know' or l.name()=='love_life' or l.name()=='have_a_go_at_it' or l.name()=='get_it_on':
                    ns=sen.replace(x[0], l.name())
                    ns=ns.lower()
                    new_sen.append(ns.replace('_', ' '))
        else:
            try: 
                pos=x[1].pos()
                for syn in wn.synsets(x[0]):
                    if syn.pos()==pos:
                        for l in syn.lemmas():
                            ns=sen.replace(x[0], l.name())
                            ns=ns.lower()
                            new_sen.append(ns.replace('_', ' '))

            except:
                ns=sen.lower()
                new_sen.append(ns.replace('_', ' '))
    new_sen = list(dict.fromkeys(new_sen))
    return new_sen

# Extention of memaning with all words
def synonym(sen):
    text = word_tokenize(sen)
    allWords=nltk.pos_tag(text)
    new_sen=[]
    for x in allWords:
        if x[0]=='fuck':
            synonyms = wn.synsets(x[0])
            for syn in synonyms:
                for l in syn.lemmas():
                    if l.name() == 'fuck' or l.name() == 'fucking' or l.name() == 'screw' or l.name() == 'screwing' or l.name() == 'ass' or l.name() == 'nooky' or l.name() == 'nookie' or l.name() == 'piece_of_ass'  or l.name() == 'roll_in_the_hay' or l.name() == 'shag' or l.name() == 'shtup' or l.name() == 'sleep_together' or l.name() == 'roll_in_the_hay' or l.name() == 'make_out'  or l.name() == 'sleep_with' or l.name() == 'get_laid' or l.name() == 'have_sex'  or l.name() == 'be_intimate' or l.name() == 'have_intercourse'  or l.name() == 'screw' or l.name() == 'fuck' or l.name() == 'jazz' or l.name() == 'eff' or l.name() == 'hump' or l.name() == 'lie_with' or l.name() == 'bed'  or l.name() == 'bang'  or l.name() == 'bonk':
                        ns=sen.replace(x[0], l.name())
                        ns=ns.lower()
                        new_sen.append(ns.replace('_', ' '))
                        
        elif x[0]=='love':
            synonyms = wn.synsets(x[0])
            for l in syn.lemmas():
                for syn in synonyms:
                    for l in syn.lemmas():
                        if l.name()=='love' or l.name()=='passion' or l.name()=='beloved' or l.name()=='dearest' or l.name()=='honey' or l.name()=='know' or l.name()=='love_life' or l.name()=='have_a_go_at_it' or l.name()=='get_it_on':
                            ns=sen.replace(x[0], l.name())
                            ns=ns.lower()
                            new_sen.append(ns.replace('_', ' '))  

        try: 
            synonyms = wn.synsets(x[0])
            for syn in synonyms:
#                 print(syn)
#                 print(syn.lemmas())
                for l in syn.lemmas():
                    ns=sen.replace(x[0], l.name())
                    ns=ns.lower()
                    new_sen.append(ns.replace('_', ' '))
        except:
            ns=sen.lower()
            new_sen.append(ns.replace('_', ' '))
    new_sen = list(dict.fromkeys(new_sen))
    return new_sen