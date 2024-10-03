from app.ServiceImp import ServiceImp

from flask import request, Response
from app.Utilities.UtilLog import UtilLog as _log
import json

class ServiceFacade:
    
    @staticmethod
    def createResponse(status,message,mimetype="application/json"):
        return Response(
					response=message,
					status=status, 
					mimetype=mimetype
		)

    @staticmethod
    def hello():
        try:
            name = request.args.get('name', default = "World")
            ans = ServiceImp.hello(name)
            return ServiceFacade.createResponse(200, ans)

        
        except Exception as e:
            _log.error(f"Error in request {request}")
            return '[Error Request] ' + str(e), 500
    
    @staticmethod
    def example():
        descriptions = request.args.get('descriptions', default = "")
        try:
            ans = ServiceImp.example(descriptions)
            return ServiceFacade.createResponse(200, ans)

        
        except Exception as e:
            _log.error(f"Error in request {request}: {e}")
            return '[Error Request] ' + str(e), 500

    @staticmethod
    def example2():
        url = request.args.get('url', default = "")
        try:
            ans = ServiceImp.example2(url)
            return ServiceFacade.createResponse(200, ans)

        
        except Exception as e:
            _log.error(f"Error in request {request}: {e}")
            return '[Error Request] ' + str(e), 500