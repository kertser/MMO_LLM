from pymongo import MongoClient
import json
import pickle


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

    def save_mongo_database_to_binary(self, output_file: str):
        """Save the entire MongoDB database to a binary file."""
        if self.db is None:
            print("Not connected to any database.")
            return

        # Dictionary to hold the database content
        db_content = {}

        try:
            # Iterate over all collections in the database
            for collection_name in self.db.list_collection_names():
                collection = self.db[collection_name]
                db_content[collection_name] = list(collection.find())

            # Serialize the database content to a binary file
            with open(output_file, 'wb') as file:
                pickle.dump(db_content, file)

            print(f"Database {self.db_name} saved to {output_file}")
        except Exception as e:
            print(f"Error saving database to binary file: {e}")

    def load_mongo_database_from_binary(self, input_file: str):
        """Load MongoDB database content from a binary file."""
        try:
            with open(input_file, 'rb') as file:
                db_content = pickle.load(file)
                print(f"Loaded data from {input_file}")
                return db_content
        except Exception as e:
            print(f"Error loading binary file: {e}")
            return None

    def import_data_to_mongo(self, data):
        """Import data into the MongoDB database, replacing old documents."""
        if self.db is None:
            print("Not connected to any database.")
            return
        try:
            for collection_name, documents in data.items():
                collection = self.db[collection_name]
                collection.delete_many({})# Clear existing documents
                if documents:# Insert new documents
                    collection.insert_many(documents)
            print("Data imported into MongoDB database successfully.")
        except Exception as e:
            print(f"Error importing data to MongoDB: {e}")

    def close_connection(self):
        """Close the MongoDB connection."""
        if self.client:
            self.client.close()
            print("Closed MongoDB connection.")


# Example usage:
uri = "mongodb://localhost:27017"
db_name = "MMODataBase"

client = MongoDBClient(uri, db_name)
client.connect()

# Load the database from a binary file
data = client.load_mongo_database_from_binary("D:\\Projects\\MMO_LLM\\resources\\test.bin")

# Fetch and print collections
collections_to_fetch = ["API", "Items", "Maps", "Monsters", "Resources"]
for collection_name in collections_to_fetch:
    print(f"Fetching data from collection: {collection_name}")
    json_data = client.fetch_collection(collection_name)
    print(json_data)

if data:
    client.import_data_to_mongo(data)

    client.close_connection()