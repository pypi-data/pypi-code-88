import pymongo
import os

class Mongo_DB():

    def __init__(self):
        #self.client = pymongo.MongoClient("mongodb+srv://admin:admin@cluster0.ttorf.mongodb.net/sro?retryWrites=true&w=majority")	
        self.client = pymongo.MongoClient(f"mongodb://{os.environ.get('MongoDB','localhost')}:27017/")	
        self.sro_db =  self.client["sro"]
	
    def insert_many(self, list_entities, collection_name):
        if len(list_entities) > 0:
            mongo_collection_name = self.sro_db[collection_name]
            return mongo_collection_name.insert_many(list_entities)
    
    def insert_one(self, entity, collection_name):
        mongo_collection_name = self.sro_db[collection_name]
        return mongo_collection_name.insert_one(entity)

    def find_one_and_update(self, collection_name, index_name, index_value, entity):
        mongo_collection_name = self.sro_db[collection_name]
        return mongo_collection_name.find_one_and_update(
            {str(index_name): index_value},
            {'$set': entity }
        )

    def get_collection(self, collection_name):
        return  self.sro_db[collection_name]

    def find_all_distinct(self, collection_name):
        mongo_collection_name = self.sro_db[collection_name]
        return mongo_collection_name.find({},{ "accountId": 1, "displayName": 1, "emailAddress": 1 })
    
    def delete_data_collection(self, collection_name):
        mongo_collection_name = self.sro_db[collection_name]
        return mongo_collection_name.delete_many({})

    def update_one_query (self, collection_name, index_name, index_value, field_name,field_value):
        mongo_collection_name = self.sro_db[collection_name]
        myquery = { str(index_name): index_value }
        newvalues  = { "$set": { str(field_name): field_value } }
        return mongo_collection_name.update_many(myquery, newvalues)

    def update_two_query (self, collection_name, index_name, index_value, index_name_2, index_value_2, field_name, field_value):
        mongo_collection_name = self.sro_db[collection_name]
        myquery = { str(index_name): index_value , str(index_name_2): index_value_2 }
        newvalues  = { "$set": { str(field_name): field_value } }
        return mongo_collection_name.update_many(myquery, newvalues)

    def update_one_query_array(self, collection_name, index_name, index_value, index_name_2, index_value_2, array_search_name, field_value):
        mongo_collection_name = self.sro_db[collection_name]
        myquery = { str(index_name): index_value, str(index_name_2): index_value_2 }
        newvalues  = { "$addToSet": { str(array_search_name): field_value } }
        return mongo_collection_name.update_many(myquery, newvalues)    

    def update_one (self, collection_name, element,field_name):
        mongo_collection_name = self.sro_db[collection_name]
        myquery = { '_id': element['_id'] }
        newvalues  = { "$set": { str(field_name): element[field_name] } }
        mongo_collection_name.update_one(myquery, newvalues)