from polyglot.text import Text 
import spacy
from spacytextblob.spacytextblob import SpacyTextBlob
import string
import collections
from sklearn.preprocessing import StandardScaler
import pickle




pos_family = {
    'noun' : ['NOUN'],
    'pron' : ['PRON'],
    'verb' : ['VERB'],
    'adj' :  ['ADJ'],
    'adv' : ['ADV'],
    'others' : ['X']
}

# function to check and get the part of speech tag count of a words in a given sentence
def check_pos_tag(x, flag):
    cnt = 0
    try:
        wiki = Text(x)
        for tup in wiki.pos_tags:
            ppo = list(tup)[1]
            if ppo in pos_family[flag]:
                cnt += 1
    except:
        pass
    return cnt

import spacy




def german_fake(df,attribute_name,model_name):
    import de_core_news_sm
    ner = de_core_news_sm.load()
    nlp = de_core_news_sm.load()
    spacy_text_blob = SpacyTextBlob()
    nlp.add_pipe(spacy_text_blob)
    df['word_count'] = df[attribute_name].apply(lambda x: len(x.split()))
    df['char_count'] = df[attribute_name].apply(len)
    df['word_density'] = df['char_count'] / (df['word_count']+1)
    df['punctuation_count'] = df[attribute_name].apply(lambda x: len("".join(_ for _ in x if _ in string.punctuation))) 
    df['title_word_count'] = df[attribute_name].apply(lambda x: len([wrd for wrd in x.split() if wrd.istitle()]))
    df['upper_case_word_count'] = df[attribute_name].apply(lambda x: len([wrd for wrd in x.split() if wrd.isupper()]))
    df['noun_count'] = df[attribute_name].apply(lambda x: check_pos_tag(x, 'noun'))
    df['verb_count'] = df[attribute_name].apply(lambda x: check_pos_tag(x, 'verb'))
    df['adj_count'] = df[attribute_name].apply(lambda x: check_pos_tag(x, 'adj'))
    df['pron_count'] = df[attribute_name].apply(lambda x: check_pos_tag(x, 'pron'))
    df['adv_count'] = df[attribute_name].apply(lambda x: check_pos_tag(x, 'adv'))
    df['other_POS'] = df[attribute_name].apply(lambda x: check_pos_tag(x, 'others'))
    df["sentiment"] = df[attribute_name].apply(lambda x:nlp(x)._.sentiment.polarity)

        ## tag text and exctract tags into a list
    df["tags"] = df[attribute_name].apply(lambda x: [(tag.text, tag.label_) 
                                    for tag in ner(x).ents] )
    ## utils function to count the element of a list
    def utils_lst_count(lst):
        dic_counter = collections.Counter()
        for x in lst:
            dic_counter[x] += 1
        dic_counter = collections.OrderedDict( 
                         sorted(dic_counter.items(), 
                         key=lambda x: x[1], reverse=True))
        lst_count = [ {key:value} for key,value in dic_counter.items() ]
        return lst_count

    ## count tags
    df["tags"] = df["tags"].apply(lambda x: utils_lst_count(x))
    ## utils function create new column for each tag category
    def utils_ner_features(lst_dics_tuples, tag):
        if len(lst_dics_tuples) > 0:
            tag_type = []
            for dic_tuples in lst_dics_tuples:
                for tuple in dic_tuples:
                    type, n = tuple[1], dic_tuples[tuple]
                    tag_type = tag_type + [type]*n
                    dic_counter = collections.Counter()
                    for x in tag_type:
                        dic_counter[x] += 1
            return dic_counter[tag]
        else:
            return 0
    
    ## extract features
    tags_set = []
    for lst in df["tags"].tolist():
         for dic in lst:
            for k in dic.keys():
                tags_set.append(k[1])
    tags_set = list(set(tags_set))
    for feature in tags_set:
         df["tags_"+feature] = df["tags"].apply(lambda x: 
                                 utils_ner_features(x, feature))
    
    #print(tags_set)
    x={'PER','MISC','ORG','LOC'}
    
    x.difference_update(tags_set) 
    for i in x:
      df["tags_"+i]=0

    df.drop([attribute_name,'punctuation_count','tags'],axis=1,inplace=True)

    from sklearn.preprocessing import StandardScaler

    scaler = StandardScaler()
    scaler = scaler.fit(df)
    x_train_scaled = scaler.transform(df)


    !wget https://github.com/soumayan/fake-news-spreader/blob/main/german/german_model_'$model_name'.sav?raw=true 
    loaded_model = pickle.load(open('./german_model_'+model_name+'.sav?raw=true', 'rb'))
    predicted_value = loaded_model.predict(x_train_scaled)
    '''
    if predicted_value[0]==0:
      print('true')
    else:
      print('fake')
    '''
    df['news_output']=predicted_value
    



def french_fake(df,attribute_name,model_name):
    import fr_core_news_sm
    ner = fr_core_news_sm.load()
    nlp = fr_core_news_sm.load()
    spacy_text_blob = SpacyTextBlob()
    nlp.add_pipe(spacy_text_blob)
    df['word_count'] = df[attribute_name].apply(lambda x: len(x.split()))
    df['char_count'] = df[attribute_name].apply(len)
    df['word_density'] = df['char_count'] / (df['word_count']+1)
    df['punctuation_count'] = df[attribute_name].apply(lambda x: len("".join(_ for _ in x if _ in string.punctuation))) 
    df['title_word_count'] = df[attribute_name].apply(lambda x: len([wrd for wrd in x.split() if wrd.istitle()]))
    df['upper_case_word_count'] = df[attribute_name].apply(lambda x: len([wrd for wrd in x.split() if wrd.isupper()]))
    df['noun_count'] = df[attribute_name].apply(lambda x: check_pos_tag(x, 'noun'))
    df['verb_count'] = df[attribute_name].apply(lambda x: check_pos_tag(x, 'verb'))
    df['adj_count'] = df[attribute_name].apply(lambda x: check_pos_tag(x, 'adj'))
    df['pron_count'] = df[attribute_name].apply(lambda x: check_pos_tag(x, 'pron'))
    df['adv_count'] = df[attribute_name].apply(lambda x: check_pos_tag(x, 'adv'))
    df['other_POS'] = df[attribute_name].apply(lambda x: check_pos_tag(x, 'others'))
    df["sentiment"] = df[attribute_name].apply(lambda x:nlp(x)._.sentiment.polarity)

        ## tag text and exctract tags into a list
    df["tags"] = df[attribute_name].apply(lambda x: [(tag.text, tag.label_) 
                                    for tag in ner(x).ents] )
    ## utils function to count the element of a list
    def utils_lst_count(lst):
        dic_counter = collections.Counter()
        for x in lst:
            dic_counter[x] += 1
        dic_counter = collections.OrderedDict( 
                         sorted(dic_counter.items(), 
                         key=lambda x: x[1], reverse=True))
        lst_count = [ {key:value} for key,value in dic_counter.items() ]
        return lst_count

    ## count tags
    df["tags"] = df["tags"].apply(lambda x: utils_lst_count(x))
    ## utils function create new column for each tag category
    def utils_ner_features(lst_dics_tuples, tag):
        if len(lst_dics_tuples) > 0:
            tag_type = []
            for dic_tuples in lst_dics_tuples:
                for tuple in dic_tuples:
                    type, n = tuple[1], dic_tuples[tuple]
                    tag_type = tag_type + [type]*n
                    dic_counter = collections.Counter()
                    for x in tag_type:
                        dic_counter[x] += 1
            return dic_counter[tag]
        else:
            return 0
    
    ## extract features
    tags_set = []
    for lst in df["tags"].tolist():
         for dic in lst:
            for k in dic.keys():
                tags_set.append(k[1])
    tags_set = list(set(tags_set))
    for feature in tags_set:
         df["tags_"+feature] = df["tags"].apply(lambda x: 
                                 utils_ner_features(x, feature))
    
    #print(tags_set)
    x={'PER','MISC','ORG','LOC'}
    
    x.difference_update(tags_set) 
    for i in x:
      df["tags_"+i]=0

    df.drop([attribute_name,'punctuation_count','tags'],axis=1,inplace=True)

    from sklearn.preprocessing import StandardScaler

    scaler = StandardScaler()
    scaler = scaler.fit(df)
    x_train_scaled = scaler.transform(df)


    !wget https://github.com/soumayan/fake-news-spreader/blob/main/french/french_model_'$model_name'.sav?raw=true 
    loaded_model = pickle.load(open('./french_model_'+model_name+'.sav?raw=true', 'rb'))
    predicted_value = loaded_model.predict(x_train_scaled)
    '''
    if predicted_value[0]==0:
      print('true')
    else:
      print('fake')
    '''
    df['news_output']=predicted_value



def italian_fake(df,attribute_name,model_name):
    import it_core_news_sm
    ner = it_core_news_sm.load()
    nlp = it_core_news_sm.load()
    spacy_text_blob = SpacyTextBlob()
    nlp.add_pipe(spacy_text_blob)
    df['word_count'] = df[attribute_name].apply(lambda x: len(x.split()))
    df['char_count'] = df[attribute_name].apply(len)
    df['word_density'] = df['char_count'] / (df['word_count']+1)
    df['punctuation_count'] = df[attribute_name].apply(lambda x: len("".join(_ for _ in x if _ in string.punctuation))) 
    df['title_word_count'] = df[attribute_name].apply(lambda x: len([wrd for wrd in x.split() if wrd.istitle()]))
    df['upper_case_word_count'] = df[attribute_name].apply(lambda x: len([wrd for wrd in x.split() if wrd.isupper()]))
    df['noun_count'] = df[attribute_name].apply(lambda x: check_pos_tag(x, 'noun'))
    df['verb_count'] = df[attribute_name].apply(lambda x: check_pos_tag(x, 'verb'))
    df['adj_count'] = df[attribute_name].apply(lambda x: check_pos_tag(x, 'adj'))
    df['pron_count'] = df[attribute_name].apply(lambda x: check_pos_tag(x, 'pron'))
    df['adv_count'] = df[attribute_name].apply(lambda x: check_pos_tag(x, 'adv'))
    df['other_POS'] = df[attribute_name].apply(lambda x: check_pos_tag(x, 'others'))
    df["sentiment"] = df[attribute_name].apply(lambda x:nlp(x)._.sentiment.polarity)

        ## tag text and exctract tags into a list
    df["tags"] = df[attribute_name].apply(lambda x: [(tag.text, tag.label_) 
                                    for tag in ner(x).ents] )
    ## utils function to count the element of a list
    def utils_lst_count(lst):
        dic_counter = collections.Counter()
        for x in lst:
            dic_counter[x] += 1
        dic_counter = collections.OrderedDict( 
                         sorted(dic_counter.items(), 
                         key=lambda x: x[1], reverse=True))
        lst_count = [ {key:value} for key,value in dic_counter.items() ]
        return lst_count

    ## count tags
    df["tags"] = df["tags"].apply(lambda x: utils_lst_count(x))
    ## utils function create new column for each tag category
    def utils_ner_features(lst_dics_tuples, tag):
        if len(lst_dics_tuples) > 0:
            tag_type = []
            for dic_tuples in lst_dics_tuples:
                for tuple in dic_tuples:
                    type, n = tuple[1], dic_tuples[tuple]
                    tag_type = tag_type + [type]*n
                    dic_counter = collections.Counter()
                    for x in tag_type:
                        dic_counter[x] += 1
            return dic_counter[tag]
        else:
            return 0
    
    ## extract features
    tags_set = []
    for lst in df["tags"].tolist():
         for dic in lst:
            for k in dic.keys():
                tags_set.append(k[1])
    tags_set = list(set(tags_set))
    for feature in tags_set:
         df["tags_"+feature] = df["tags"].apply(lambda x: 
                                 utils_ner_features(x, feature))
    
    #print(tags_set)
    x={'PER','MISC','ORG','LOC'}
    
    x.difference_update(tags_set) 
    for i in x:
      df["tags_"+i]=0

    df.drop([attribute_name,'punctuation_count','tags'],axis=1,inplace=True)

    from sklearn.preprocessing import StandardScaler

    scaler = StandardScaler()
    scaler = scaler.fit(df)
    x_train_scaled = scaler.transform(df)

    !wget https://github.com/soumayan/fake-news-spreader/blob/main/italian/italian_model_'$model_name'.sav?raw=true 

    loaded_model = pickle.load(open('./italian_model_'+model_name+'.sav?raw=true', 'rb'))
    predicted_value = loaded_model.predict(x_train_scaled)
    '''
    if predicted_value[0]==0:
      print('true')
    else:
      print('fake')
    '''
    df['news_output']=predicted_value



def spanish_fake(df,attribute_name,model_name):
    import es_core_news_sm
    ner = es_core_news_sm.load()
    nlp = es_core_news_sm.load()
    spacy_text_blob = SpacyTextBlob()
    nlp.add_pipe(spacy_text_blob)
    df['word_count'] = df[attribute_name].apply(lambda x: len(x.split()))
    df['char_count'] = df[attribute_name].apply(len)
    df['word_density'] = df['char_count'] / (df['word_count']+1)
    df['punctuation_count'] = df[attribute_name].apply(lambda x: len("".join(_ for _ in x if _ in string.punctuation))) 
    df['title_word_count'] = df[attribute_name].apply(lambda x: len([wrd for wrd in x.split() if wrd.istitle()]))
    df['upper_case_word_count'] = df[attribute_name].apply(lambda x: len([wrd for wrd in x.split() if wrd.isupper()]))
    df['noun_count'] = df[attribute_name].apply(lambda x: check_pos_tag(x, 'noun'))
    df['verb_count'] = df[attribute_name].apply(lambda x: check_pos_tag(x, 'verb'))
    df['adj_count'] = df[attribute_name].apply(lambda x: check_pos_tag(x, 'adj'))
    df['pron_count'] = df[attribute_name].apply(lambda x: check_pos_tag(x, 'pron'))
    df['adv_count'] = df[attribute_name].apply(lambda x: check_pos_tag(x, 'adv'))
    df['other_POS'] = df[attribute_name].apply(lambda x: check_pos_tag(x, 'others'))
    df["sentiment"] = df[attribute_name].apply(lambda x:nlp(x)._.sentiment.polarity)

        ## tag text and exctract tags into a list
    df["tags"] = df[attribute_name].apply(lambda x: [(tag.text, tag.label_) 
                                    for tag in ner(x).ents] )
    ## utils function to count the element of a list
    def utils_lst_count(lst):
        dic_counter = collections.Counter()
        for x in lst:
            dic_counter[x] += 1
        dic_counter = collections.OrderedDict( 
                         sorted(dic_counter.items(), 
                         key=lambda x: x[1], reverse=True))
        lst_count = [ {key:value} for key,value in dic_counter.items() ]
        return lst_count

    ## count tags
    df["tags"] = df["tags"].apply(lambda x: utils_lst_count(x))
    ## utils function create new column for each tag category
    def utils_ner_features(lst_dics_tuples, tag):
        if len(lst_dics_tuples) > 0:
            tag_type = []
            for dic_tuples in lst_dics_tuples:
                for tuple in dic_tuples:
                    type, n = tuple[1], dic_tuples[tuple]
                    tag_type = tag_type + [type]*n
                    dic_counter = collections.Counter()
                    for x in tag_type:
                        dic_counter[x] += 1
            return dic_counter[tag]
        else:
            return 0
    
    ## extract features
    tags_set = []
    for lst in df["tags"].tolist():
         for dic in lst:
            for k in dic.keys():
                tags_set.append(k[1])
    tags_set = list(set(tags_set))
    for feature in tags_set:
         df["tags_"+feature] = df["tags"].apply(lambda x: 
                                 utils_ner_features(x, feature))
    
    #print(tags_set)
    x={'PER','MISC','ORG','LOC'}
    
    x.difference_update(tags_set) 
    for i in x:
      df["tags_"+i]=0

    df.drop([attribute_name,'punctuation_count','tags'],axis=1,inplace=True)

    from sklearn.preprocessing import StandardScaler

    scaler = StandardScaler()
    scaler = scaler.fit(df)
    x_train_scaled = scaler.transform(df)


    !wget https://github.com/soumayan/fake-news-spreader/blob/main/spanish/spanish_model_'$model_name'.sav?raw=true 

    loaded_model = pickle.load(open('./spanish_model_'+model_name+'.sav?raw=true', 'rb'))
    predicted_value = loaded_model.predict(x_train_scaled)
    '''
    if predicted_value[0]==0:
      print('true')
    else:
      print('fake')
    '''
    df['news_output']=predicted_value



def english_fake(df,attribute_name,model_name):
    import en_core_web_sm
    ner = spacy.load("en_core_web_sm")
    nlp = spacy.load("en_core_web_sm")
    spacy_text_blob = SpacyTextBlob()
    nlp.add_pipe(spacy_text_blob)
    df['word_count'] = df[attribute_name].apply(lambda x: len(x.split()))
    df['char_count'] = df[attribute_name].apply(len)
    df['word_density'] = df['char_count'] / (df['word_count']+1)
    df['punctuation_count'] = df[attribute_name].apply(lambda x: len("".join(_ for _ in x if _ in string.punctuation))) 
    df['title_word_count'] = df[attribute_name].apply(lambda x: len([wrd for wrd in x.split() if wrd.istitle()]))
    df['upper_case_word_count'] = df[attribute_name].apply(lambda x: len([wrd for wrd in x.split() if wrd.isupper()]))
    df['noun_count'] = df[attribute_name].apply(lambda x: check_pos_tag(x, 'noun'))
    df['verb_count'] = df[attribute_name].apply(lambda x: check_pos_tag(x, 'verb'))
    df['adj_count'] = df[attribute_name].apply(lambda x: check_pos_tag(x, 'adj'))
    df['pron_count'] = df[attribute_name].apply(lambda x: check_pos_tag(x, 'pron'))
    df['adv_count'] = df[attribute_name].apply(lambda x: check_pos_tag(x, 'adv'))
    df['other_POS'] = df[attribute_name].apply(lambda x: check_pos_tag(x, 'others'))
    df["sentiment"] = df[attribute_name].apply(lambda x:nlp(x)._.sentiment.polarity)

        ## tag text and exctract tags into a list
    df["tags"] = df[attribute_name].apply(lambda x: [(tag.text, tag.label_) 
                                    for tag in ner(x).ents] )
    ## utils function to count the element of a list
    def utils_lst_count(lst):
        dic_counter = collections.Counter()
        for x in lst:
            dic_counter[x] += 1
        dic_counter = collections.OrderedDict( 
                         sorted(dic_counter.items(), 
                         key=lambda x: x[1], reverse=True))
        lst_count = [ {key:value} for key,value in dic_counter.items() ]
        return lst_count

    ## count tags
    df["tags"] = df["tags"].apply(lambda x: utils_lst_count(x))
    ## utils function create new column for each tag category
    def utils_ner_features(lst_dics_tuples, tag):
        if len(lst_dics_tuples) > 0:
            tag_type = []
            for dic_tuples in lst_dics_tuples:
                for tuple in dic_tuples:
                    type, n = tuple[1], dic_tuples[tuple]
                    tag_type = tag_type + [type]*n
                    dic_counter = collections.Counter()
                    for x in tag_type:
                        dic_counter[x] += 1
            return dic_counter[tag]
        else:
            return 0
    
    ## extract features
    tags_set = []
    for lst in df["tags"].tolist():
         for dic in lst:
            for k in dic.keys():
                tags_set.append(k[1])
    tags_set = list(set(tags_set))
    for feature in tags_set:
         df["tags_"+feature] = df["tags"].apply(lambda x: 
                                 utils_ner_features(x, feature))
    
    #print(tags_set)
    x={'NORP', 'PRODUCT',
       'LANGUAGE', 'MONEY', 'ORDINAL', 'GPE', 'LOC',
       'QUANTITY', 'CARDINAL', 'PERSON', 'ORG',
       'TIME', 'WORK_OF_ART', 'FAC', 'PERCENT', 'LAW',
       'DATE', 'EVENT'}
    
    x.difference_update(tags_set) 
    for i in x:
      df["tags_"+i]=0

    df.drop([attribute_name,'tags'],axis=1,inplace=True)
    scaler = StandardScaler()
    scaler = scaler.fit(df)
    x_train_scaled = scaler.transform(df)
    !wget https://github.com/soumayan/fake-news-spreader/blob/main/english/english_model_'$model_name'.sav?raw=true 
    loaded_model = pickle.load(open('./english_model_'+model_name+'.sav?raw=true', 'rb'))
    predicted_value = loaded_model.predict(df)

    df['news_output']=predicted_value
            