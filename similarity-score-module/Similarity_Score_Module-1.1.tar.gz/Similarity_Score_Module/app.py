import pandas as pd
import numpy as np

from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

import neattext.functions as nfx
import json

def check_similarity_score(data, column_name, _id, num_of_recommendations = 5, output_filename = 'output.json'):
	data_idea = data.loc[data['id'] == _id]
	data_idea = data_idea[column_name]
	data = data.dropna()
	data.isna().sum()

	data['cleaned'] = data[column_name].apply(nfx.remove_stopwords)

	data['cleaned'] = data['cleaned'].apply(nfx.remove_special_characters)

	count_vectorization = CountVectorizer()
	count_vectorizer_matrix = count_vectorization.fit_transform(data['cleaned'])

	# sparse to dense
	count_vectorizer_matrix.todense()

	cosine_similarity_matrix = cosine_similarity(count_vectorizer_matrix)

	idea_index = pd.Series(data.index, index = data[column_name]).drop_duplicates()

	def similar_results(title, num_of_recommendations = 5):
	    try:
	        #ID
	        idx = idea_index[title]

	        # search cosine similiarty matrix
	        scores = list(enumerate(cosine_similarity_matrix[idx]))

	        # sort the score
	        sort_scores = sorted(scores, key = lambda x:x[1], reverse = True)

	        # recommendation
	        selected_idea_indices = [i[0] for i in sort_scores[1:]]
	        selected_idea_scores = [i[1] for i in sort_scores[1:]]

	        # result
	        result = data[column_name].iloc[selected_idea_indices]
	        similar_results = pd.DataFrame(result)
	        similar_results['similarity_score'] = selected_idea_scores
	        similar_results['id'] = data['id'].iloc[selected_idea_indices]

	        return similar_results.head(num_of_recommendations)

	    except:
	        pass
	        # result_df = data[data.idea.str.contains(title,case=False)]
	        # #result_df = result_df[result_df['num_subscribers'] > 1000]
	        # return result_df[['id', 'idea']].head(num_of_recommendations)

	idea_list = []
	for i in data_idea.iteritems():
	    idea_list.append(i[1])

	for index, i in enumerate(idea_list):
	    result = similar_results(i,num_of_recommendations)

	    result = result.to_dict()
	    with open(output_filename, "w") as outfile: 
	    	json.dump(result, outfile)
	    result = json.dumps(result)


	return result