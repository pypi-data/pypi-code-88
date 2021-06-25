# THIS FILE IS GENERATED FROM PADDLEPADDLE SETUP.PY
#
full_version    = '2.1.1'
major           = '2'
minor           = '1'
patch           = '1'
rc              = '0'
istaged         = True
commit          = '1e62c239d323354eccfc974d4e2e6496f93d848e'
with_mkl        = 'ON'

def show():
    if istaged:
        print('full_version:', full_version)
        print('major:', major)
        print('minor:', minor)
        print('patch:', patch)
        print('rc:', rc)
    else:
        print('commit:', commit)

def mkl():
    return with_mkl
