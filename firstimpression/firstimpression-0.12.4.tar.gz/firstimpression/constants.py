from tempfile import gettempdir
import os
import mimetypes

mimetypes.init()

PICTURE_FORMATS = {
    'fullscreen': "http://narrowcasting.fimpweb.nl/imageresize.php?width=1920&url=",
    'square':     "http://narrowcasting.fimpweb.nl/imageresize.php?width=512&url=",
}

TEMP_FOLDER = gettempdir()
LOCAL_INTEGRATED_FOLDER = 'C:/Users/Public/Documents/Scala/LocalIntegratedContent'
PLACEHOLDER_FOLDER = os.path.join(LOCAL_INTEGRATED_FOLDER, 'placeholders')

APIS = [
    '',
    'BBC',
    'NS',
    'NU',
    'TRAFFIC',
    'INSTAGRAM',
    'WEATHER',
    'AMBER_ALERT',
    'AMS_AIRPORT',
    'CHUCK_NORRIS',
    'EHV_AIRPORT',
    'FACEBOOK',
    'GOOGLE_TRENDS',
    'INTERIA',
    'SONGKICK'
    ]

VIDEO_EXTENSIONS = [ext for ext in mimetypes.types_map if mimetypes.types_map[ext].split('/')[0] == 'video']
IMG_EXTENSIONS = [ext for ext in mimetypes.types_map if mimetypes.types_map[ext].split('/')[0] == 'image']
