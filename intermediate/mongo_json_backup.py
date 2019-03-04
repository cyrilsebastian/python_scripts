#!/usr/bin/python3
#by @CyrilSebastian

#this script checks for dbs and collections and exports in JSON format.

import os, pymongo
from pymongo import MongoClient

#lists the DBs in mongo
client = MongoClient('localhost', 27017)
db_names = client.list_database_names()

for i in db_names:
    print(i)
    print(client[i].list_collection_names())

for j in db_names:
    if not os.path.exists(j):
        os.makedirs(j)
        os.chdir(j)
