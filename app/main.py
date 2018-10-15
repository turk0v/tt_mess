import datetime
import json
from pprint import pprint 

def debug_print(env):
    pprint(env.keys())
    for key in env.keys():
        pprint(pprint("=== KEY: {} == VALUE: {} ===".format(key, env[key])))

def wsgi_application(environ, start_response):
	status = '200 OK'
	headers = [('Content-Type', 'application/json')]
	body = {'time': str(datetime.datetime.now().time())[:8], 'url': environ['wsgi.url_scheme']+'://'+environ['HTTP_HOST']}
	start_response(status, headers)
	return [ json.dumps(body).encode('utf-8') ]