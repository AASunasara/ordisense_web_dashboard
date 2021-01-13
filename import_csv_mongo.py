from pymongo import MongoClient
import csv

client = MongoClient('localhost', 27017)

# target collection
collection_ordis = client.ordisense_db.ordisense_data
def import_csv_mongo():
    reader = csv.DictReader(open("ordisense_data.csv"))
    
    # delete all previos data
    collection_ordis.delete_many({})
    for row in reader:
        collection_ordis.insert_one(row)

import_csv_mongo()
