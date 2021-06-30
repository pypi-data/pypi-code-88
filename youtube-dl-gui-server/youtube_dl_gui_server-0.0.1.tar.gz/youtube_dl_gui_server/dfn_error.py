#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import render_template
import traceback,os
from http import HTTPStatus

MODE=os.environ.get("MODE")

def exception_handler(ex):
	if MODE=='DEBUG':
		print(traceback.format_exc())
		return (render_template("error.html",error=traceback.format_exc()),HTTPStatus.INTERNAL_SERVER_ERROR)
	else:
		return (render_template("error.html"),HTTPStatus.INTERNAL_SERVER_ERROR)

def not_found_handler(ex):
	return (render_template("404.html"),HTTPStatus.NOT_FOUND)

def over_max_file_size_handler(error):
	return(render_template("size_over.html",title="File Size is Over!"))

