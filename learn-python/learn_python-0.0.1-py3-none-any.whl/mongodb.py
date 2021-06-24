from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
dbs = client.list_database_names()
mydb = "testdb"

print(dbs.__class__)

if mydb in dbs:
    print(mydb + ' exists')
    #db = dbs['testdb']
    #print(db)