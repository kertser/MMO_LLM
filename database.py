# open database (mongoDB)
# collectionItems
collectionItemsJsonPath = "resources/DB/MMODataBase.Items.json"

import json
import pymongo

def open_database():
    """Open a connection to a MongoDB database"""

    # Connect to MongoDB
    client = pymongo.MongoClient("mongodb://localhost:27017/")

    # Get the database
    db = client["mmo_database"]

    print("Connected to MongoDB database")
    return db

def close_database(db):
    """Close the connection to the MongoDB database"""
    db.client.close()
    print("Disconnected from MongoDB database")

def load_json_to_db(db, collection_name, json_data):
    """Load JSON data to a MongoDB collection"""
    collection = db[collection_name]
    # load json from file:

    with open(json_data, "r") as f:
        json_data = json.load(f)
        print(f"Loaded {len(json_data)} documents from {json_data}")

    result = collection.insert_many(json_data)
    print(f"Loaded {len(result.inserted_ids)} documents into the {collection_name} collection")

def save_db_to_file(db, collection_name, file_path):
    """Save a MongoDB collection to a JSON file"""
    collection = db[collection_name]
    with open(file_path, "w") as f:
        json.dump(list(collection.find()), f, indent=4)
    print(f"Saved {collection.count_documents({})} documents to {file_path}")

def print_collection(db, collection_name):
    """Print the contents of a MongoDB collection"""
    collection = db[collection_name]
    for doc in collection.find():
        print(doc)

db = open_database()
load_json_to_db(db, "items", collectionItemsJsonPath)
#print_collection(db, "items")
save_db_to_file(db, "items", "resources/DB/items.db")
close_database(db)