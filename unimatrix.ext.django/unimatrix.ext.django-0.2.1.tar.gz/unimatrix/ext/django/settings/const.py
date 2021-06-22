"""Constants used in the Unimatrix One/CM platforms,
for deployments for Django.
"""
import os


SESSIONS_PERSISTENT = os.getenv('SESSIONS_PERSISTENT') == '1'

STATICFILES_DIRS = []
if os.path.exists('dist/assets'):
    STATICFILES_DIRS.append('dist/assets')

STATIC_ROOT = 'static'
