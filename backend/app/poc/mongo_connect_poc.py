# Script is a demo poc for connecting to mongoDB

import pymongo

def connect_to_mongo():
    """
    Connects to a MongoDB instance running on localhost:27017.
    
    :return: MongoClient object or error message
    """
    try:
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        return client
    except pymongo.errors.ConnectionFailure as e:
        return {"error": str(e)}


if __name__ == "__main__":
    
    client = connect_to_mongo()
    print(client)
    # Output: MongoClient(host=['localhost:27017'], document_class=dict, tz_aware=False, connect=True)
    
    # If there is an error
    # print(connect_to_mongo())  # Output: {'error': 'connection error'}