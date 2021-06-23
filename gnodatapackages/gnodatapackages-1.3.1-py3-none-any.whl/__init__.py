from .gno_gen_stopwords import gno_generalstopwords
from .gno_gen_stopwords import gno_generalstopwords_cn
from .gno_name_stopwords import gno_inpersonname_remove
from .gno_name_stopwords import gno_honorifics_remove
from .gno_coname_stopwords import gno_inconame_stopwords
# the above have been replaced by the below. but not sure if any other codes are using the above. 

from .gno_stopwords import gno_generalstopwords, gno_generalstopwords_cn, gno_inpersonname_remove, gno_honorifics_remove, gno_inconame_stopwords
from .gno_stopwordcleaning import Remove_stopwords, Replace_CoStopwords

from .gno_uploadfile_clean import load_files
from .gno_checkLang_ft import gno_predictLang
# from .gno_checkLang_ftfull import gno_predictLang_full


def joke():
    return (u'simi lan test test.')