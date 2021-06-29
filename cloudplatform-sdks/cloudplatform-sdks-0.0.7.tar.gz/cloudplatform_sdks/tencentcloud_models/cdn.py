from .clients import cdn_client


class TencentCdnDomain:
    def __init__(self, object):
        self.object = object

    @classmethod
    def list(cls, **kwargs):
        domains = cdn_client.list_domains(**kwargs).get('DomainList')
        return [cls(domain) for domain in domains]

    @classmethod
    def get(cls, **kwargs):
        domains = cdn_client.list_domains(**kwargs).get('DomainList')
        if len(domains) > 0:
            return cls(domains[0])
        else:
            return None

    @staticmethod
    def fresh_urls_cache(**kwargs):
        return cdn_client.refresh_urls_cache(**kwargs)

    @staticmethod
    def fresh_path_cache(**kwargs):
        return cdn_client.refresh_path_cache(**kwargs)

    @staticmethod
    def push_urls_cache(**kwargs):
        return cdn_client.push_urls_cache(**kwargs)

    @property
    def status(self):
        return self.object.get('Status')

    @property
    def name(self):
        return self.object.get('Domain')

    def __repr__(self):
        return "<TencentCdnDomain object:{}>".format(self.name)