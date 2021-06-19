

class SeoAppSettings(object):

    @property
    def MIDDLEWARE(self):
        return super().MIDDLEWARE + [
            'seo.middleware.PageMetaMiddleware'
        ]

    @property
    def INSTALLED_APPS(self):
        return super().INSTALLED_APPS + [
            'sitemetrics',
            'seo'
        ]

default = SeoAppSettings
