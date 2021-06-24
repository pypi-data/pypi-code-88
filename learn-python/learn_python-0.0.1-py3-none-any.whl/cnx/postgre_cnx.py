import psycopg2
import xlsxwriter
import logging
import requests
from src.models.database import Database
from src.exceptions import InvalidFilePath


log = logging.getLogger(__name__)

database = Database(dbname='db_test', host='host', user='user', password='password')

STATUS_DOWN = "DOWN"
STATUS_OK = "OK"


def is_database_up(dbname, host, user, password):

    try:
        conn = psycopg2.connect("dbname='{}' user='{}' host='{}' password='{}' connect_timeout=1 ".format
                (dbname, host, user, password))
        conn.close()
        return True
    except:
        return False


def is_hue_up(login_url, username, password):

    next_url = "/"
    login_url = "http://localhost:8888/accounts/login"

    session = requests.Session()
    response = session.get(login_url)

    form_data = {
        'username': 'mapr',
        'password': 'mapr',
        'csrfmiddlewaretoken': session.cookies['csrftoken'],
        'next': next_url
    }
    response = session.post(login_url, data=form_data, cookies={}, headers={'Referer': login_url})

    print('Logged in successfully: %s %s' % (response.status_code == 200, response.status_code))

    cookies = session.cookies
    headers = session.headers

    response = session.get('http://localhost:8888/metastore/databases/default/metadata')
    print(response.status_code)
    print(response.text)


def generate_excel(file_path):

    if file_path is not None:
        workbook = xlsxwriter.Workbook(path)
        worksheet = workbook.add_worksheet()
        worksheet.write('A1', database.dbname)
        if is_database_up(dbname=database.dbname, host=database.host, user=database.user, password=database.password):
            worksheet.write('B1', STATUS_OK)
            log.info("Connection to database: %s is %s" % (database.dbname, STATUS_OK))
        else:
            worksheet.write('B1', STATUS_DOWN)
            log.info("Connection to database: %s is %" % (database.dbname, STATUS_DOWN))
        workbook.close()
    else:
        raise InvalidFilePath("Invalid excel file path")


if __name__ == '__main__':

    login_url = "http://localhost:8888/accounts/login?next=/"
    path = "E:/DEV/dev-python/learn-python/conf/result.xlsx"
    is_hue_up(login_url=login_url, username="mapr", password="mapr")
    # generate_excel(path)