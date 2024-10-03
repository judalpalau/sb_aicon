
from flask import request,Response
import connexion
import traceback
import json


from app.Utilities.UtilLog import UtilLog as _log
#from app.DBConnection import MongoDBConnection as DBConnection
from app.Server.ResponseApi import ResponseApi

class ServerApi:
    app = None
    useDB = True
    @staticmethod
    def init(useDB=True):
        ServerApi.useDB = useDB
        # Create the application instance
        connx_app = connexion.App(__name__)

        #getting flask app
        app = connx_app.app
        app.url_map.strict_slashes = False

        # Read the swagger.yml file to configure the endpoints
        connx_app.add_api('/app-run/app/openapi.yaml')

        ServerApi.app = connx_app

        return ServerApi.app

    @staticmethod
    def before_request(request):
        # if ServerApi.useDB :
        #     DBConnection.initDB(ServerApi.app.app)
        pass

    @staticmethod
    def after_request(response):
        #to avoid swagger validation format response
        _log.debug('status:%s mimetype:%s'%(response.status,response.mimetype))
        if not isinstance(response,ResponseApi) and response.status_code >= 400 :
            res = {}
            if response.mimetype == "application/json" or response.mimetype == "application/problem+json":
                if isinstance(response.response,list):
                    res = json.loads(response.response[0])
                else:
                    res = json.loads(response.response)
            status_code = response.status_code
            message = response.status
            if 'status' in res:
                status_code = res['status']
            if 'detail' in res:
                message = res['detail']

            return Response(
                    response=json.dumps({'message':message, 'status':status_code}), 
                    status=status_code,
                    mimetype="application/problem+json"
            )
        return response

    @staticmethod
    def errorhandler(error):
        #getting and printing stacktrace
        trace = traceback.format_exc()
        traceback.print_exc()

        #getting error code and message
        status_code = getattr(error, 'status_code', 500)
        message		= getattr(error, 'message', 'Server Internal Error')
        error_code  = getattr(error, 'error_code', 'N/A')

        if error_code!= 'N/A':
            return ResponseApi(
                response=json.dumps({'message':message, 'status':status_code, 'error_code':error_code}), 
                status=status_code
            )

        return ResponseApi(
                response=json.dumps({'message':message, 'status':status_code}), 
                status=status_code
        )