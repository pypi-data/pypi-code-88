import requests
import datetime

_API_PATH = 'https://studies.helsinki.fi/api/search'

def _collect( query ):

    page = 0
    content = []

    while True:

        query['page'] = page

        r = requests.get( _API_PATH , params = query )
        data = r.json()

        content += data['hits']
        page += 1

        if len( content ) >= data['totalHits']:
            break

    return content

## a bit weird heuristic
def _guess_study_year():
    now = datetime.datetime.now()

    if now.month < 7:
        return now.year - 1
    else:
        return now.year

def _select_language( courses, lang ):
    _courses = []
    for course in courses:
        for key, value in course.items():
            if isinstance( value, dict ) and lang in value:
                course[ key ] = value[ lang ]
        _courses.append( course )
    return _courses


def search( search = '', lang = 'en', academic_year = _guess_study_year() ):
    courses = _collect( {'searchText': search, 'studyYear' : academic_year, 'lang' : lang } )
    return _select_language( courses, lang )

def by_organisation( organisations = [], lang = 'en', academic_year = _guess_study_year() ):
    ## todo: can requests multiple organisations at the same time, but not easy to plug in with the collect implementation
    ret = []

    for org in organisations:

        org = str( org )

        if not org.startswith( 'hy-org-' ):
            org = 'hy-org-' + org

        ret += _collect( {'organisation': org, 'studyYear' : academic_year, 'lang' : lang } )

    return ret
