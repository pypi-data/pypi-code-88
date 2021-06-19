import pandas as pd 
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
from PIL import Image

class WordCloudLite:

    def generate_wordcloud(data, bg_color = 'white',max_words=1000, max_font_size=100, random_state=42, height = 640, width = 1080, output_filename='wordCloud.png'):
        
        stopwords = set(STOPWORDS)

        wordcloud = WordCloud(
                              background_color=bg_color,
                              stopwords=stopwords,
                              max_words=max_words,
                              max_font_size=max_font_size, 
                              random_state=random_state,
                              width= width,
                              height= height,
                             ).generate(str(data))

        wordcloud.to_file(output_filename)

        fig = plt.figure(figsize = (16,12))
        plt.imshow(wordcloud)
        plt.axis('off')
        plt.show()