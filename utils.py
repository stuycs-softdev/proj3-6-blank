from pymongo import MongoClient
from flask import session
c = MongoClient()
db = c.users
def authorize(username, password):
    user = db.Collections.find_one({'username':username, 'password':password})
    if user:
        return 0
    else:
        return None
def userExists(username):
    return len(list(db.Collections.find({'username':username}))) == 1
def createUser(username, password):
    if len(username) < 4 or len(password) < 6:
        return 2
    if not userExists(username):
        ui = db.Collections.count()+1
        db.Collections.insert({'id':ui,'username':username, 'password':password})
        return 0
    else:
        return 1
