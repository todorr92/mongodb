import pymongo
import os
from os import path 
if path.exists("env.py"):
    import env 


MONGODB_URI = os.environ.get("MONGO_URI")
SECRET_KEY = os.environ.get('SECRET_KEY')
DBS_NAME = "myTestDB"
COLLECTION_NAME = "myFirstMDB"


def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is connected!")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e
        

conn = mongo_connect(MONGODB_URI)

coll = conn[DBS_NAME][COLLECTION_NAME]

# Adding new data to database

# new_docs = [{'first': 'terry', 'last': 'pratchett', 'dob': '28/04/1948', 'gender': 'm',
#        'hair_colour': 'not much', 'occupation': 'writer',
#       'nationality': 'english'},
#      {'first': 'george', 'last': 'rr martin', 'dob': '20/09/1948', 'gender': 'm',
#     'hair_colour': 'white', 'occupation': 'writer',
#    'nationality': 'american'}]


# coll.insert_many(new_docs) # insert_many for inserting more then one, and .insert is one

documents = coll.find()
# coll.find({'name': 'douglas'}) finding specific property in database
# coll.remove({'name': 'douglas'}) removes specific property
# coll.update_one({'nationality': 'american'}, {'$set': {'hair_colour': 'maroon'}}) updating one property
# coll.update_many({'nationality': 'american'}, {'$set': {'hair_colour': 'maroon'}}) updating many properties

for doc in documents:
    print(doc)
