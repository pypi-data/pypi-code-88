#!python

import pyforms
from wp_dso_publish.app_gui import AppGUI
from wp_dso_publish import local_settings
from confapp import conf

conf += local_settings

# Execute the application
if __name__ == "__main__":   pyforms.start_app(AppGUI, geometry=[100, 100, 500, 700])

