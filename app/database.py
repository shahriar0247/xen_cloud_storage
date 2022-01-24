import pymongo

db = pymongo.MongoClient().xenusersdb
users = db.users
storage = db.storage