
class SliderSettings(object):
    @property
    def INSTALLED_APPS(self):
        return super().INSTALLED_APPS + [
            'slider'
        ]

    @property
    def STYLESHEETS(self):
        return super().STYLESHEETS + (
            'slider/slideshow.css',
        )

    @property
    def STATIC_APPS(self):
        apps = super().STATIC_APPS

        if 'slick' not in apps:
            apps.append('slick')

        if 'fancybox' not in apps:
            apps.append('fancybox')

        return apps


default = SliderSettings
