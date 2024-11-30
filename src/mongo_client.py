from abc import ABC, abstractmethod
import logging
from pymongo import MongoClient, errors
from pymongo.collection import Collection

logger = logging.Logger(__name__)

class MongoDBClient(ABC):
    """Base MongoDB class to connect to an mongo database"""
    def __init__(self, host: str, port: str, database: str) -> None:
        self.host = host
        self.port = port
        self.database = database
        self.client = MongoClient(host=self.host, port=int(self.port), uuidRepresentation='pythonLegacy')
        self.connect()

    def connect(self) -> None:
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
        if self.database in self.client.list_database_names():
            db = self.client[self.database]
            if collection in db.list_collection_names():
                col = db[collection]
                return col
        logging.error("No database %s with collection %s found...", self.database, collection)
        return None
