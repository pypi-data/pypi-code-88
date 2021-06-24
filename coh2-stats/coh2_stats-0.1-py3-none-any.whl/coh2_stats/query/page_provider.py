from urllib.request import urlopen
from coh2_stats.utils.logger import Logger

class PageFromInternet:
    def get(self, url):
        try:
            f = urlopen(url)
            Logger(f"url visited: {url}")
            return f.read()
        except:
            Logger(f"url ({url}) is invalid")

class PageFromLocal:
    def get(self, url):
        try:
            #cohio = Coh2IO()
            #return cohio.read(url)
            pass
        except:
            page = PageFromInternet().get(url)
