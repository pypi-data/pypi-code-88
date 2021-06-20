import requests
import statistics

class PingAttempt:
    def __init__(self, url):
        self.url = url
        self.response = None
        self.content = None
        self.content_size = None
        self.request_time = None
        self.num_redirects = None
        self.http_to_https_redirect = None

        try:
            self.response = requests.get(url)

            self.content = self.response.text
            self.content_size = len(self.content.encode('utf-8'))
            self.request_time = self.response.elapsed.total_seconds()
            self.num_redirects = len(self.response.history)
            self.http_to_https_redirect = True if self.url.startswith("http://") and self.response.url.startswith("https://") else False

        except requests.exceptions.RequestException as e:
            pass

class Pinger:

    def __init__(self, url):
        self.url = url
        self.url_valid = False
        self.pings = self.get_pings()

        self.num_pings = len(self.pings)
        self.num_successful_pings = len([ping for ping in self.pings if ping.response is not None])

        self.average_content_size = None
        self.average_request_time = None
        self.average_redirects = None
        self.does_redirect_http_to_https = None

        if self.num_successful_pings > 0:
            self.url_valid = True
            self.average_request_time = statistics.mean([ping.request_time for ping in self.pings if ping.response is not None])
            self.average_content_size = statistics.mean([ping.content_size for ping in self.pings if ping.response is not None])
            self.average_redirects = statistics.mean([ping.num_redirects for ping in self.pings if ping.response is not None])
            self.does_redirect_http_to_https = True if any([ping.http_to_https_redirect for ping in self.pings if ping.response is not None]) else False

    def get_pings(self, *, num=10):
        pings = list()

        for i in range(num):
            pings.append(PingAttempt(self.url))

        return pings