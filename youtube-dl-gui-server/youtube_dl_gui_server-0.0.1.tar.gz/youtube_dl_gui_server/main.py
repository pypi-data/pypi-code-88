#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, request, make_response, redirect, url_for
from youtube_dl_gui_server import routing, dfn_error
import youtube_dl
import os

app=Flask(__name__)

app.secret_key="#o\xfbqi\xf2P{R\xe9\x9cd=\x90[\x97"

HOME=""

@app.route(HOME+'/',methods=['GET'])
def index():
	return routing.show_home()

@app.route(HOME+'/',methods=['POST'])
def add_download():
	return routing.do_add_download()

@app.route('/stream/<int:id>')
def stream(id):
    return routing.return_stream(id)

@app.route(HOME+'/cache/rm/<string:file>',methods=['GET'])
def del_cache(file):
	return routing.do_del_cache(file)


app.after_request(routing.after_request)

app.register_error_handler(Exception, dfn_error.exception_handler)
app.register_error_handler(404, dfn_error.not_found_handler)

def main():
	try:
		if os.environ.get("MODE")=="DEBUG":
			debug=True
		else:
			debug=False
		app.run(debug=debug,host='0.0.0.0',port=8080, threaded=True)
	except KeyboardInterrupt:
		routing.tmp_dir.cleanup()
		routing.executor.shutdown()

if __name__=="__main__":
	main()
