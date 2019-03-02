#!/usr/bin/python3
#by @CyrilSebastian

#this script checks for dbs and collections and exports in JSON format.

import sys, pymongo
from pymongo import MongoClient

#lists the DBs in mongo
client = MongoClient('localhost', 27017)
print(client.list_database_names())
print(client.list_collection_names())

client = MongoClient('localhost', 27017)
#db_names = client.list_database_names()
db_name = client["pilot"]
print(db_name.list_collection_names())

db_names = client.list_database_names()
for i in db_names:
    sole_db = client["i"]
    print(sole_db.list_collection_names())
