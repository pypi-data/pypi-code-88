#!/usr/bin/env python
import os

def openApiPath():

    relpath = os.path.join( os.path.dirname( __file__ ), 'http.schema.yml' )

    return os.path.abspath( relpath ) 