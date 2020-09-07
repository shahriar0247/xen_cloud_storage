import pymongo

db = pymongo.MongoClient().xenusersdb
users = db.users
awaiting_users = db.awaitingusers