from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter:
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password):
        # Connection setup
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 32084
        DB = 'AAC'
        COL = 'animals'
        try:
            self.client = MongoClient(f'mongodb://{username}:{password}@{HOST}:{PORT}/?authSource=admin')
            self.database = self.client[DB]
            self.collection = self.database[COL]
        except Exception as e:
            print("Error connecting to MongoDB:", e)
            raise

    def create(self, data):
        """ Inserts a document into the collection """
        try:
            if data is not None and isinstance(data, dict):
                result = self.collection.insert_one(data)
                return result.acknowledged
            else:
                print("Invalid data: must be a non-empty dictionary.")
                return False
        except Exception as e:
            print("Error inserting document:", e)
            return False

    def read(self, query=None):
        """ Reads documents based on a query and returns a list """
        try:
            if query is not None and isinstance(query, dict):
                results = list(self.collection.find(query))
            else:
                results = list(self.collection.find())  # return all
            return results
        except Exception as e:
            print("Error reading documents:", e)
            return []

    def update(self, query, new_values):
        """ Updates documents based on a query and new values """
        try:
            if isinstance(query, dict) and isinstance(new_values, dict):
                result = self.collection.update_many(query, {'$set': new_values})
                return result.modified_count
            else:
                print("Both query and new_values must be dictionaries.")
                return 0
        except Exception as e:
            print("Error updating document(s):", e)
            return 0

    def delete(self, query):
        """ Deletes documents based on a query """
        try:
            if isinstance(query, dict):
                result = self.collection.delete_many(query)
                return result.deleted_count
            else:
                print("Query must be a dictionary.")
                return 0
        except Exception as e:
            print("Error deleting document(s):", e)
            return 0

