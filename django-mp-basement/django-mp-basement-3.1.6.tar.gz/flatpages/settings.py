
class FlatpageSettings(object):

    @property
    def INSTALLED_APPS(self):
        return super().INSTALLED_APPS + [
            'flatpages'
        ]

default = FlatpageSettings
