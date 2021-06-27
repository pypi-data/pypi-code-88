import random
from cbcdb.main import DBManager


db = DBManager()

res = db.get_sql_list_dicts('select * from bi.transactions limit 5')

a = 0
