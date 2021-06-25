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

APIS = {
    'amber':'AMBER_ALERT',
    'schiphol':'AMS_AIRPORT',
    'bbc':'BBC',
    'ns':'NS',
    'traffic':'TRAFFIC',
    'insta':'INSTAGRAM',
    'weather':'WEATHER',
    'jokes':'CHUCK_NORRIS',
    'eindhoven':'EHV_AIRPORT',
    'facebook':'FACEBOOK',
    'trends':'GOOGLE_TRENDS',
    'news_polish':'INTERIA',
    'concerts':'SONGKICK',
    'nu': 'NU'
}

VIDEO_EXTENSIONS = [ext for ext in mimetypes.types_map if mimetypes.types_map[ext].split('/')[0] == 'video']
IMG_EXTENSIONS = [ext for ext in mimetypes.types_map if mimetypes.types_map[ext].split('/')[0] == 'image']

MONTH_ABREVIATION_INDEX = 0
MONTH_FULLNAME_INDEX = 1

ENGLISH_INDEX = 0
DUTCH_INDEX = 1
