import json
from urllib import response
from wsgiref.simple_server import make_server

def application(environ, start_response):
    headers = [('Content-type','application/json')]
    
    start_response('200 OK',headers)
    response = {
        'mensaje':'Hola Gaston, lo lograste!!!'
    }
    
    return [ bytes(json.dumps(response),'utf-8')]
servidor = make_server('localhost',8000,application)
servidor.handle_request()

