
__all__ = [
    "BaseExtractor",
    "MdpiExtractor",
    "NihExtractor",
    "ScienceDirectExtractor",
]

import re
from requests import get
from requests.exceptions import InvalidURL
from requests.utils import default_headers
from bs4 import BeautifulSoup as B
from tldextract import extract
from html import unescape
from json import loads
from pprint import pprint as cat, pformat as pcat
from datetime import datetime


from rollet import settings
from rollet.utils import (
    rfinditem
)


class BaseExtractor:
    def __init__(self, url, **kwargs):
        """
        Create BaseExtractor instance
        url: string
        timeout: float, request timeout. Default 1 sec.
        abstract_**kwargs: **kwargs for abstract fetch
        title_**kwargs: **kwargs for title fetch
        """
        
        self.url = url
        self.domain = extract(url).domain
        self.date = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
        self._scrap(**kwargs)
        self._init_kwargs(**kwargs)
    
    def _scrap(self, **kwargs):
        timeout = kwargs.pop('timeout', 1)
        headers = kwargs.pop('headers', None)
        with get(self.url, timeout = timeout, headers = headers) as response:
            self._status = response.status_code
            self._header = response.headers
            self._content_type()
            if self.content_type == 'html':
                self._page = B(response.text, 'html.parser')
            else:
                self._page = B()
    
    def _init_kwargs(self, **kwargs):
        self._abstract_kwargs, self._title_kwargs, self._lang_kwargs = {}, {}, {}
        for k,v in kwargs.items():
            field, key, *_ = k.split('__') + [None]
            if field == 'abstract': self._abstract_kwargs.update({key:v})
            elif field == 'title': self._title_kwargs.update({key:v})
            elif field == 'lang': self._lang_kwargs.update({key:v})
    

    def _content_type(self):
        if self.url[-3:] == 'pdf': content = 'pdf'
        else:
            charset = self._header.get('Content-Type', '')
            content = re.findall('(html|pdf|json|xml)', charset)
            content = content[0] if len(content) else 'html'
        self.content_type = content


    @staticmethod
    def _get_content(tag, **kwargs):
        """
        Get content from element Tag
        tag: bs4.element.Tag
        script_keys: List, of keys if tag is script
        attr: str, key attribute if tag is neither a meta nor a script
        :return: content
        """

        if tag.name == 'meta':
            content = tag.attrs.get('content', [])
        elif tag.name == 'script':
            keys = kwargs.get('script_keys', [])
            try:
                serie = loads(tag.content[0])
            except:
                content = list()
            else:
                content = [rfinditem(serie, key) for key in keys]
        elif kwargs.get('attr'):
            content = tag.attrs.get(kwargs.get('attr'))
        else:
            content = tag.text.strip().replace('\n', '')

        content = content[0] if isinstance(content, list) and len(content) else content
        content = unescape(content) if isinstance(content, str) else content
        return content
    

    def __repr__(self):
        string = "Title: {}\nFrom: {}\nFetched at: {}\nStatus: {}\nType: {}\n{} Abstract {}\n{}"
        return string.format(
            self.title, self.url, self.date,
            self._status, self.content_type,
            '-'*5, '-'*5, pcat(self.abstract), 
        )


    def fetch(self, selectors, which='first', **kwargs):
        content = list()
        arg_w = ('first', 'min', 'max')
        if which not in arg_w:
            raise ValueError(f'which should be one of {arg_w}')
        for s in selectors:
            contents_ = list()
            tags = self._page.select(s)
            if len(tags): contents_ = [self._get_content(tag, **kwargs) for tag in tags]
            if len(contents_) and which == 'first': 
                content = [contents_[0]]
                break
            else:
                try: content += ['. '.join(set(contents_))]
                except: pass
        content = content if len(content) else [None]
        if which == 'max': content = max(content, key=lambda x: len(str(x)))
        else: content = min(content, key=lambda x: len(str(x)))
        return content
    
    @property
    def title(self):
        title = None
        if self.content_type == 'html':
            title = self.fetch(settings.TITLE, **self._title_kwargs)
        return title
    
    @property
    def abstract(self):
        abstract = None
        if self.content_type == 'html':
            abstract = self.fetch(settings.ABSTRACT, **self._abstract_kwargs)
        return abstract
    
    @property
    def lang(self):
        lang = None
        if self.content_type == 'html':
            lang = self._page.html.get('lang', None)
        return lang
    
    
    def to_dict(self):
        return {
            'url': self.url,
            'status': self._status,
            'title': self.title,
            'abstract': self.abstract,
            'lang': self.lang,
            'content_type': self.content_type,
            'date': self.date
        }
    
    def to_list(self, *args):
        if len(args): listed = [getattr(self, arg, None) for arg in args]
        else: listed = list(self.to_dict().values())
        return listed


class MdpiExtractor(BaseExtractor):
    """
    Extractor for base mdpi.com domain
    """

    @property
    def abstract(self):
        abstract = self._page.find(class_='art-abstract').text.strip()
        abstract = super().abstract if not abstract else abstract
        return abstract

    @property
    def title(self):
        title = self._page.find(class_='title', attrs={
            'itemprop': 'name'
        }).text.strip()
        title = super().title if not title else title
        return title
    

class NihExtractor(BaseExtractor):
    """
    Extractor for base nih.gov domain
    """
    
    @property
    def abstract(self):
        abstract = self._page.find(id='enc-abstract').text.strip()
        abstract = super().abstract if not abstract else abstract
        return abstract

    @property
    def title(self):
        title = self._page.find('h1', class_='heading-title').text.strip()
        title = super().title if not title else title
        return title


class ScienceDirectExtractor(BaseExtractor):
    """
    Extractor for base sciencedirect.com domain
    """
    def _scrap(self, **kwargs):
        headers = default_headers()
        headers.update({
            'User-Agent':
            'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
        })
        super()._scrap(headers=headers, **kwargs)

    @property
    def abstract(self):
        abstract = self._page.find(id='abstracts',
                                   class_='Abstracts').text.strip()
        abstract = super().abstract if not abstract else abstract
        return abstract

    @property
    def title(self):
        title = self._page.find('span', class_='title-text').text.strip()
        title = super().title if not title else title
        return title