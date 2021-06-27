from .main import load_corpus
import litcorpt.settings as settings
from litcorpt.crawlers.gutenberg_crawl import download_all_books as gutenberg_download_all_books
from litcorpt.crawlers.gutenberg_preproc import preprocess as gutenberg_preprocess
from tinydb import Query as Query

__version__ = '0.0.1'
__author__ = 'Igor Morgado'
__author_email__ = 'morgado.igor@gmail.com'

settings.init()


