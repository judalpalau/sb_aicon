import os
import mongoengine
from flask_mongoengine import MongoEngine
from app.Utilities.UtilLog import UtilLog as _log

class MongoDBConnection:
    engine = None
    app = None

    def initDB(app):
        if MongoDBConnection.app :
            return
        _log.debug('initDB...')
        
        if app is None :
            raise Exception('App not available')
        
        MongoDBConnection.app = app

        try:
            HOST = os.environ.get('MONGODB_HOST')
            PORT = os.environ.get('MONGODB_PORT')
            
            if(MongoDBConnection.engine is None):
                MongoDBConnection.engine = MongoEngine()

            MongoDBConnection.app.config['MONGODB_SETTINGS'] = {
				'host': HOST,
				'alias': 'default'
			}
			
            MongoDBConnection.engine.init_app(app)

        except:
            _log.error('Not able to connect to mongoDB')
            raise Exception('Not able to connect to mongoDB')