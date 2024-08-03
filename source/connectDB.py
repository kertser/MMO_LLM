from pymongo import MongoClient
import json


class MongoDBClient:
    def __init__(self, uri: str, db_name: str):
        self.uri = uri
        self.db_name = db_name
        self.client = None
        self.db = None

    def connect(self):
        """Connect to the MongoDB database."""
        try:
            self.client = MongoClient(self.uri)
            self.db = self.client[self.db_name]
            print(f"Connected to MongoDB database: {self.db_name}")
        except Exception as e:
            print(f"Error connecting to MongoDB: {e}")

    def fetch_collection(self, collection_name: str):
        """Fetch all documents from a collection and return them as JSON."""
        if self.db is None:
            print("Not connected to any database.")
            return None

        try:
            collection = self.db[collection_name]
            documents = list(collection.find())
            return json.dumps(documents, default=str)
        except Exception as e:
            print(f"Error fetching collection {collection_name}: {e}")
            return None

    def close_connection(self):
        """Close the MongoDB connection."""
        if self.client:
            self.client.close()
            print("Closed MongoDB connection.")


# Example usage:
uri = "mongodb://localhost:27017"  # Replace with your MongoDB URI
db_name = "MMODataBase"  # Replace with your database name

client = MongoDBClient(uri, db_name)
client.connect()

# Fetch and print four specific collections
collections_to_fetch = ["Items", "Maps", "Monsters",
                        "Resources"]  # Replace with your collection names
for collection_name in collections_to_fetch:
    print(f"Fetching data from collection: {collection_name}")
    json_data = client.fetch_collection(collection_name)
    print(json_data)  # Or handle the data as needed

client.close_connection()