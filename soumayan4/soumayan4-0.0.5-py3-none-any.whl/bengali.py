def bengali_fake(df,attribute_name,model_name):
    from bnlp import POS
    bn_pos = POS()
    model_path = "bn_pos.pkl"
    tagged_text = df[attribute_name].apply(lambda x:bn_pos.tag(model_path,x))
    def count_tags(texts_with_tags):
        tag_count = {}
        for word, tag in texts_with_tags:
            if tag in tag_count:
                tag_count[tag] += 1
            else:
                tag_count[tag] = 1
        return(tag_count)
    tagged_text.map(count_tags)
    import pandas as pd
    tagged_text = pd.DataFrame(tagged_text)
    tagged_text['tag_counts'] = tagged_text[attribute_name].map(count_tags)
    tag_set = list(set([tag for tags in tagged_text['tag_counts'] for tag in tags]))
    for tag in tag_set:
        tagged_text[tag] = tagged_text['tag_counts'].map(lambda x: x.get(tag, 0))

    x={'VM','PU','CCL','RDS','PP','CX','LC','RDX','DAB','PRL','ALC','AMN','CCD',
    'VAUX','NC','CSB','PWH','NP','RDF','DRL','PRF','NST','JQ','PPR','JJ','NV'}
    x.difference_update(tag_set) 
    for i in x:
      tagged_text[i]=0

    from bnlp import NER
    bn_ner = NER()
    model_path = "bn_ner.pkl"
    tagged_text1 = df[attribute_name].apply(lambda x:bn_ner.tag(model_path,x))
    def count_tags(texts_with_tags):
        tag_count1 = {}
        for word, tag in texts_with_tags:
            if tag in tag_count1:
                tag_count1[tag] += 1
            else:
                tag_count1[tag] = 1
        return(tag_count1)
    tagged_text1.map(count_tags)
    tagged_text1 = pd.DataFrame(tagged_text1)
    tagged_text1['tag_counts1'] = tagged_text1[attribute_name].map(count_tags)
    tag_set = list(set([tag for tags in tagged_text1['tag_counts1'] for tag in tags]))
    for tag in tag_set:
        tagged_text1[tag] = tagged_text1['tag_counts1'].map(lambda x: x.get(tag, 0))

    x={'I-LOC','S-OBJ','S-LOC','B-ORG','B-LOC','I-ORG','E-ORG','E-PER','O','S-PER',
    'E-LOC','I-PER','S-ORG','B-PER'}
    x.difference_update(tag_set) 
    for i in x:
      tagged_text1[i]=0

    df1=tagged_text.drop([attribute_name,'tag_counts'],axis = 1)
    df2=tagged_text1.drop([attribute_name,'tag_counts1'],axis = 1)

    
    df['word_count'] = df['text'].apply(lambda x: len(x.split()))
    df['char_count'] = df['text'].apply(len)
    df['word_density'] = df['char_count'] / (df['word_count']+1)
        
    
    df3=df.drop(['text'],axis = 1)
    DF= pd.concat([df1,df2,df3], axis=1, join='inner')
    from sklearn.preprocessing import StandardScaler
    scaler = StandardScaler()
    scaler = scaler.fit(DF)
    x_scaled = scaler.transform(DF)
    import pickle
    loaded_model = pickle.load(open('/content/models/bengali_model_'+model_name+'.sav?raw=true', 'rb'))
    predicted_value = loaded_model.predict(x_scaled)
    DF['news_output']=predicted_value
    
    df=DF
    #print(df.columns)
    return df