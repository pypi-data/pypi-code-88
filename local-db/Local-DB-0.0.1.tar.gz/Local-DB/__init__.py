import json


class LocalDb:
    def __init__(self, DB_PATH):
        self.local_db = []
        self.DB_PATH = DB_PATH
        self.refresh_db_data()

    def find_one(self, query):
        self.refresh_db_data()
        query = self.validate_json(query)
        if query:
            query_key, query_value = next(iter(query.items()))
            for record in self.local_db:
                for field_key, field_value in record.items():
                    if query_key == field_key and query_value == field_value:
                        return record
        return None

    def find_many(self, query):
        self.refresh_db_data()
        results = []
        query = self.validate_json(query)
        if query:
            query_key, query_value = next(iter(query.items()))
            for record in self.local_db:
                for field_key, field_value in record.items():
                    if query_key == field_key and query_value == field_value:
                        results.append(record)
        return results

    def insert_one(self, record):
        self.refresh_db_data()
        record = self.validate_json(record)
        if record:
            self.local_db.append(record)
            self.save_to_db()

    def insert_many(self, records):
        self.refresh_db_data()
        records = self.validate_json(records)
        if records:
            records = map(lambda record: dict(record, _id=str(uuid.uuid4())), records)
            self.local_db.extend(records)
            self.save_to_db()

    def update_one(self, query, update_line, upsert=False):
        """
        use to update a record in db
        can update a record by using special keyword $set

        example:

        query = { "address": "Valley 345" }
        update_line = { "$set": { "address": "Canyon 123" } }

        mycol.update_one(myquery, newvalues)

        :param query:
        :return:
        """
        self.refresh_db_data()
        query = self.validate_json(query)
        update_line = self.validate_json(update_line)

        if query and update_line:
            command, new_field = next(iter(update_line.items()))
            command = command.split("$")[-1]
            new_field_key, new_field_value = next(iter(new_field.items()))

            record = self.find_one(query)
            if record and new_field_key in record.keys():
                if command == "set":
                    record[new_field_key] = new_field_value
                    self.save_to_db()
                if command == "push":
                    pass

            else:
                if upsert:
                    self.insert_one(new_field)

    def update_many(self, query, update_line, upsert=False):
        """
        use to update a record in db
        can update a record by using special keyword $set

        example:

        query = { "address": "Valley 345" }
        update_line = { "$set": { "address": "Canyon 123" } }

        mycol.update_one(myquery, newvalues)

        :param query:
        :return:
        """
        self.refresh_db_data()
        query = self.validate_json(query)
        update_line = self.validate_json(update_line)

        if query and update_line:
            command, new_field = next(iter(update_line.items()))
            command = command.split("$")[-1]
            new_field_key, new_field_value = next(iter(new_field.items()))

            records = self.find_many(query)
            if records:
                if command == "set":
                    for record in records:
                        if new_field_key in record.keys():
                            record[new_field_key] = new_field_value
                if command == "push":
                    pass

    def delete_one(self, query):
        self.refresh_db_data()
        try:
            query = self.validate_json(query)
            if query:
                record = self.find_one(query)
                if record:
                    self.local_db.remove(record)
                    self.save_to_db()

        except Exception as e:
            print(e)

    def delete_many(self, query):
        self.refresh_db_data()
        try:
            query = self.validate_json(query)
            if query:
                records = self.find_many(query)
                if records:
                    for record in records:
                        self.local_db.remove(record)
                    self.save_to_db()

        except Exception as e:
            print(e)

    @staticmethod
    def validate_json(data):  # validate user input as well as db
        try:
            if type(data) == dict:
                json.dumps(data)
            if type(data) == str:
                data = data.replace("\'", "\"")
                data = json.loads(data)
            return data
        except json.decoder.JSONDecodeError:
            print("please enter a valid json")

    def refresh_db_data(self):
        with open(self.DB_PATH, "r") as f:
            try:
                f.flush()
                self.local_db = json.load(f)
            except:
                pass

    def save_to_db(self):
        with open(self.DB_PATH, "w") as f:
            json.dump(self.local_db, f)
