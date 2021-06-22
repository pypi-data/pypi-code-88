# Extention of meaning with disambiguation
from pywsd import disambiguate
import nltk
from nltk.tokenize import word_tokenize
# Extention of meaning with disambiguation
def main(sen):
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


if __name__ == '__main__':
    main()
