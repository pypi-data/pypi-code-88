#!/usr/bin/env python

import asyncio, os, sys

async def __executeShellCommandAsync( cmd, **kwargs ):

    kwargs[ "cwd" ] = kwargs[ "cwd" ] if  "cwd" in kwargs.keys() else os.getcwd()

    proc = await asyncio.create_subprocess_shell( cmd, cwd=kwargs[ "cwd" ], stdout=sys.stdout, stderr=sys.stderr, stdin=sys.stdin )

    await proc.wait()

    return proc.returncode



def __executeShellCommand( *args, **kwargs ):

    return asyncio.run( __executeShellCommandAsync( *args, **kwargs ) )



def deploy(*args, **kwargs):

    parameters = {
        "alias": "customer1",
        "tags": {},
        "location": "", 
        "compute__system_id": "",
        "compute__sas_key": "",
        "compute__sas_key_systemconf": "",
        "compute__admin_username": "",
        "compute__admin_password": "",
        "compute__dns_label_prefix": "",
        "compute__windows_os_version": "",
        "compute__vm_size": "",
        "database__administrator_login": "",
        "database__administrator_login_password": "",
        "database__transparent_data_encryption": "",
        "database__server_name": "",
        "database__database_name": "",
        "database__database_edition": "",
        "database__database_collation": "",
        "database__database_service_object_name": "",
    }

    name = parameters['alias']

    basepath = '/Users/tiara-work/Repositories/bitbucket.org/inno-on-trodney/ccf/ccfref-az'

    params = ""


    for parameter in parameters.keys():

        params += "    " + parameter + "=" + str(parameters[ parameter ]) + "\n"

    string = f'module "{name}"'
    string += ' {\n'
    string += f'    source = "{basepath}/my/variant2"'
    string += '\n'
    string += params
    string += '}'

    with open( f'{basepath}/main.tf','a' ) as f:

        f.write( '\n\n' + string )

    __executeShellCommand( f'cd \'{basepath}\'; terraform init; terraform apply -auto-approve' )

    return ''