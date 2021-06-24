from typing import Optional
from requests import Session
from urllib.parse import urljoin

# https://stackoverflow.com/a/51026159/3833159
class LiveServerSession(Session):
    def __init__(self, prefix_url: Optional[str] = None, *args, **kwargs):
        super(LiveServerSession, self).__init__(*args, **kwargs)
        self.prefix_url = prefix_url

    def request(self, method, url, *args, **kwargs):
        url = urljoin(self.prefix_url or "", url)
        return super(LiveServerSession, self).request(method, url, *args, **kwargs)
