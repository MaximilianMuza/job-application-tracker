# src/mongo_client.py
from abc import ABC
import logging
from pymongo import MongoClient, errors
from pymongo.collection import Collection

logger = logging.Logger(__name__)

class MongoDBClient(ABC):
    """Base MongoDB class to connect to an mongo database"""
    def __init__(self, host: str, port: int, database: str):
        self.database = database
        self.client = MongoClient(
            host=host,
            port=port,
            uuidRepresentation='pythonLegacy'
        )
        self.connect()

    def connect(self):
        """Check if client is connected to database"""
        try:
            self.client.server_info()
            logger.info("Mongo client connected.")
        except errors.ServerSelectionTimeoutError as err:
            logger.error("Mongo client connection failed\n%s", err)

    def get_collection(self, collection: str) -> Collection | None:
        """Method to retrieve a specific collection
        
        Args:
            collection (str): Name of the wanted collection
        """
        db = self.client[self.database]
        if collection in db.list_collection_names():
            col = db[collection]
            return col
        logging.error("No database %s with collection %s found...", self.database, collection)
        return None

class UserDBClient(MongoDBClient):
    """User DB Client to connect to an user database."""
    def __init__(self, host: str, port: str, database: str):
        super().__init__(host, port, database)
        self.users_collection = self.get_collection("users")

    def find_user(self, username: str) -> dict:
        """Find user by username.
        
        Args:
            username (str): Username of user
            
        Returns:
            User object (dict)
        """
        return self.users_collection.find_one({"username": username})

    def insert_user(self, username: str, password: str) -> None:
        """Insert new user.
        
        Args:
            username (str): Username
            password (str): User password hashed
        """
        self.users_collection.insert_one({"username": username, "password": password})
