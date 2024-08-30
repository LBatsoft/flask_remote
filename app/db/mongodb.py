import pymongo


def get_connection():
    return pymongo.MongoClient('mongodb://localhost:27017/')
