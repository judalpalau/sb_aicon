from flask import request, Response
from app.Server.ServerApi import ServerApi

app = ServerApi.init(useDB=False)

@app.app.before_request
def before_request_api():
	ServerApi.before_request(request)

@app.app.after_request
def after_request_api(response):
	return ServerApi.after_request(response)

@app.app.errorhandler(Exception)
def errorhandler(error):
	return ServerApi.errorhandler(error)