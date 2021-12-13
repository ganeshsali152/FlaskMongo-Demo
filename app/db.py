from app.config import MongoUri
from flask_mongoengine import MongoEngine

#----------Setup MongoUri----------

def init_db():
    mongo = MongoEngine()
    return mongo

def get_db(app,mongo):

    app.config['MONGODB_SETTINGS'] = {
        'host': MongoUri
    }
    mongo.init_app(app)


