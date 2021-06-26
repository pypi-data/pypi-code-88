import pandas as pd
def hindi_fake(df,attribute_name,model_name):
    import nltk
    nltk.download('indian')
    nltk.download('punkt')
    from nltk.tag import tnt 
    from nltk.corpus import indian 
    train_data = indian.tagged_sents('hindi.pos')
    tnt_pos_tagger = tnt.TnT() 
    tnt_pos_tagger.train(train_data)
    tagged_text = df[attribute_name].apply(lambda x:tnt_pos_tagger.tag(nltk.word_tokenize(x)))
    def count_tags(texts_with_tags):
        tag_count = {}
        for word, tag in texts_with_tags:
            if tag in tag_count:
                tag_count[tag] += 1
            else:
                tag_count[tag] = 1
        return(tag_count)
    tagged_text.map(count_tags).head()
    tagged_text = pd.DataFrame(tagged_text)
    tagged_text['tag_counts'] = tagged_text[attribute_name].map(count_tags)
    tag_set = list(set([tag for tags in tagged_text['tag_counts'] for tag in tags]))
    for tag in tag_set:
        tagged_text[tag] = tagged_text['tag_counts'].map(lambda x: x.get(tag, 0))

    x={'','CC','NNP','INTF','QF','RP','NNPC','QW','VAUX','NLOC','JVB','VJJ','QFNUM',
    'SYM','NNC','JJ','RB','Unk','VNN','PUNC','NN','VRB','PREP','NEG','PRP','VFM','NVB'}
    x.difference_update(tag_set) 
    for i in x:
      tagged_text[i]=0

    
    df['word_count'] = df[attribute_name].apply(lambda x: len(x.split()))
    df['char_count'] = df[attribute_name].apply(len)
    df['word_density'] = df['char_count'] / (df['word_count']+1)
    df['punctuation_count'] = df[attribute_name].apply(lambda x: len("".join(_ for _ in x if _ in string.punctuation))) 
        
    
    df3=df.drop([attribute_name],axis = 1)
    df1=tagged_text.drop([attribute_name,'tag_counts'],axis = 1)
    df2=df.drop([attribute_name],axis = 1)
    DF= pd.concat([df1,df2], axis=1, join='inner')
    from sklearn.preprocessing import StandardScaler
    scaler = StandardScaler()
    scaler = scaler.fit(DF)
    x_scaled = scaler.transform(DF)
    import pickle
    loaded_model = pickle.load(open('hindi_model_'+model_name+'.sav?raw=true', 'rb'))
    predicted_value = loaded_model.predict(x_scaled)
    DF['news_output']=predicted_value
    return DF