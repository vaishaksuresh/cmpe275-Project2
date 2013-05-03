import json
import bottle
from bottle import route,run,request,abort,response
from pymongo import Connection
from json import JSONEncoder
from bson.objectid import ObjectId

connection  = Connection('localhost',27017)
db=connection.test
     
class MongoEncoder(JSONEncoder):
    def default(self, obj, **kwargs):
        if isinstance(obj, ObjectId):
            return str(obj)
        else:
            return JSONEncoder.default(obj, **kwargs)

@route('/announcements', method='GET')
def get_announcements():
    entity = db['coursecollection'].find({'courseId':'course1'})
    if not entity:
        abort(404, 'No document with id %s' % id)
    response.content_type = 'application/json'
    entries = [entry for entry in entity]
    return MongoEncoder().encode(entries)
 
run(host='localhost', port=8080)