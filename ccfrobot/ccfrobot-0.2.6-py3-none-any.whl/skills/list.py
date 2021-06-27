#!/bin/env python3
"""skill functions for hashing ccf objects
"""
import  os, yaml, glob, traceback, warnings


class Exception(BaseException):
    
    pass



class SafeLoaderIgnoreUnknown( yaml.SafeLoader ):

    def ignore_unknown( self, node ):

        return None 

SafeLoaderIgnoreUnknown.add_constructor(
    None,
    SafeLoaderIgnoreUnknown.ignore_unknown
)



def environment( data ):

    return data
