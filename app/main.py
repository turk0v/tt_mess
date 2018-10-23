import datetime
import json


def wsgi_application(environ, start_response):
	status = '200 OK'
	headers = [('Content-Type', 'application/json')]
	body = json.dumps({'time': str(datetime.datetime.now().time())[:8], 'url': environ['wsgi.url_scheme']+'://'+environ['HTTP_HOST']})
	start_response(status, headers)
	return [ body.encode('utf-8')]
