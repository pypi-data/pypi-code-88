import re
import urllib.parse as urlparse
from cachetools import TTLCache

from bs4 import BeautifulSoup
from rsi.session import RSISession
from rsi.conf import DEFAULT_RSI_URL
from rsi.exceptions import RSIException

DEFAULT_CACHE_TTL = 300
HANGAR_ENDPOINT = '/account/pledges'
PLEDGE_UPGRADES_ENDPOINT = '/api/account/upgradeLog'
BUYBACKS_ENDPOINT = '/account/buy-back-pledges'

_ITEM_TYPE_MAP = {
    'ship': 'ships',
    'package': 'packages',
    'upgrade': 'upgrades',
    'skin': 'paint',
    'fps': 'fps',
    'flair': 'flair',
}
BG_IMAGE_RE = re.compile(r"background-image:url\('([^']+)'\);")
UPGRADE_LOG_RE = re.compile(r"[^-]*- (?P<from>(?! to ).*) to (?P<to>[^,]+), "
                            r"new value: (?P<new_value>[^\s]+ [A-Z]+)")


class Hangar(object):
    def __init__(self, session=None, rsi_url=DEFAULT_RSI_URL, hangar_endpoint=HANGAR_ENDPOINT,
                 pledge_upgrade_endpoint=PLEDGE_UPGRADES_ENDPOINT, buyback_endpoint=BUYBACKS_ENDPOINT,
                 cache_ttl=DEFAULT_CACHE_TTL):
        """ Returns the `sessions` hangar. """
        self.session = session or RSISession(url=rsi_url)
        self.rsi_url = rsi_url.rstrip('/')
        self.hangar_url = f'{self.rsi_url}/{hangar_endpoint.lstrip("/")}'
        self.pledge_upgrade_url = f'{self.rsi_url}/{pledge_upgrade_endpoint.lstrip("/")}'
        self.buyback_url = f'{self.rsi_url}/{buyback_endpoint.lstrip("/")}'
        self.is_empty = False

        self._ttlcache = TTLCache(maxsize=1, ttl=cache_ttl)

    @property
    def list_items(self):
        return self._cache('data', self._update_details)['list_items']

    @property
    def items(self):
        return self._cache('data', self._update_details)['items']

    @property
    def ships(self):
        return self._cache('data', self._update_details)['ships']

    @property
    def paint(self):
        return self._cache('data', self._update_details)['paint']

    @property
    def packages(self):
        return self._cache('data', self._update_details)['packages']

    @property
    def upgrades(self):
        return self._cache('data', self._update_details)['upgrades']

    @property
    def fps(self):
        return self._cache('data', self._update_details)['fps']

    @property
    def flair(self):
        return self._cache('data', self._update_details)['flair']

    @property
    def buybacks(self):
        return self._cache('data', self._update_details)['buybacks']

    def clear_cache(self):
        """ Resets the cache """
        for key in self._ttlcache.keys():
            del self._ttlcache[key]

    def _cache(self, key, update_func, *args, **kwargs):
        if key not in self._ttlcache:
            self._ttlcache[key] = update_func(*args, **kwargs)
        return self._ttlcache[key]

    def _hangaritem_from_li(self, li, data):
        """ parse an <li> from the hangar page and stick the results into `data` """
        insurance = ""
        added_ships = []
        upgrades = []

        attrs = {
            _.get("class")[0].replace('js-pledge-', ''): _.get('value')
            for _ in li.select('input') if 'js-pledge-' in str(_)
        }

        if not attrs:
            print(f"Could not parse hangar item: {li}")
            return attrs

        if list(li.select('a.upgrade')):
            # parse the upgrade log
            r = self.session.post(self.pledge_upgrade_url, data={'pledge_id': attrs['id']})
            if r.status_code == 200 and r.json()['success'] == 1:
                s = BeautifulSoup(r.json()['data']['rendered'], features='html.parser')
                for u in s.select('span'):
                    m = UPGRADE_LOG_RE.match(u.text)
                    if m:
                        upgrades.append(m.groupdict())

        if 'name' in attrs:
            attrs['items'] = []
            for i in li.select('.item'):
                i = {
                    field: BG_IMAGE_RE.sub("\\1", _.get("style")) if field == 'image' else _.text.strip()
                    for _ in i.select('div')
                    if (field := _.get("class")[0]) != 'text'
                }

                if 'upgrade' in i['title'].lower():
                    i['kind'] = 'Upgrade'
                elif 'digital download' in i['title'].lower():
                    i['kind'] = 'package'

                if i.setdefault('kind', 'items').split()[0].lower() in _ITEM_TYPE_MAP:
                    i['category'] = _ITEM_TYPE_MAP[i['kind'].split()[0].lower()]
                else:
                    i['category'] = i['kind']

                if 'insurance' in i['title'].lower():
                    insurance = i['title']
                    for s in added_ships:
                        s['insurance'] = i['title']
                    continue

                if i['category'] == 'ships':
                    if insurance:
                        i['insurance'] = insurance
                    added_ships.append(i)

                attrs['items'].append(i)
                data.setdefault(i['category'], []).append(i)
            data['list_items'].append(attrs)
        else:
            # TODO: use logging
            print(f"Could not parse hangar item: {li}")

        if insurance:
            attrs['insurance'] = insurance
        if upgrades:
            attrs['upgrades'] = upgrades

        return attrs

    def _buyback_from_article(self, a, data):
        try:
            b = {
                'title': a.select_one('h1').text.strip(),
                'image': a.select_one('img').attrs['src']
            }
        except Exception as e:
            print(f'Error parsing buyback: {a}')
            b = {'title': str(a), 'image': ''}
        return b

    def _update_details(self):
        if self.session is None or not self.session.is_authenticated:
            return RSIException('Hangar requires and authenticated session')

        self.is_empty = False
        r = self.session.get(self.hangar_url)
        r.raise_for_status()

        data = {
            'list_items': [],
            'items': [],
            'ships': [],
            'packages': [],
            'upgrades': [],
            'flair': [],
            'buybacks': [],
        }

        lis = []

        num_pages = BeautifulSoup(r.text, features='html.parser').select_one('.inner-content .pager .raquo')
        if not num_pages:
            num_pages = 1
        else:
            num_pages = int(urlparse.parse_qs(urlparse.urlparse(num_pages.get('href')).query)['page'][0])

        for i in range(1, num_pages + 1):
            r = self.session.get(self.hangar_url, params={'page': i, 'pagesize': 10})
            r.raise_for_status()
            lis.extend(BeautifulSoup(r.text, features='html.parser').select('.list-items li'))

        if len(lis) == 1 and lis[0].select_one('.empy-list'):
            self.is_empty = True
            lis = []

        for i in lis:
            self._hangaritem_from_li(i, data)

        # fetch buybacks
        r = self.session.get(self.buyback_url)
        r.raise_for_status()

        articles = []
        num_pages = BeautifulSoup(r.text, features='html.parser').select_one('.inner-content .pager .raquo')
        if not num_pages:
            num_pages = 1
        else:
            num_pages = int(urlparse.parse_qs(urlparse.urlparse(num_pages.get('href')).query)['page'][0])

        for i in range(1, num_pages + 1):
            r = self.session.get(self.buyback_url, params={'page': i, 'pagesize': 10})
            r.raise_for_status()
            articles.extend(BeautifulSoup(r.text, features='html.parser').select('article.pledge'))

        if len(articles) == 1 and articles[0].select_one('.empy-list'):
            articles = []

        data['buybacks'] = [self._buyback_from_article(a, data) for a in articles]

        return data
