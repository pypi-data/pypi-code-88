import os

def init():
    global GUTENBERG_URL
    GUTENBERG_URL = "http://www.gutenberg.org/browse/languages/pt"

    global GUTENBERG_DATAPATH
    GUTENBERG_DATAPATH = ""
    #GUTENBERG_DATAPATH = os.environ.get('GUTENBERG_DATAPATH', '~/data/gutenberg')
    #GUTENBERG_DATAPATH = os.path.expanduser(GUTENBERG_DATAPATH)

    global LITCORPUSPT_DATAPATH
    LITCORPUSPT_DATAPATH = os.environ.get('LITCORPUSPT_DATAPATH', '~/litcorpt_data')
    LITCORPUSPT_DATAPATH = os.path.expanduser(LITCORPUSPT_DATAPATH)

if __name__ == '__main__':
    pass
