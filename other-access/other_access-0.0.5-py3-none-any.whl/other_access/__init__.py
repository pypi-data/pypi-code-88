#!/usr/bin/env python3

import os
import pwd
import grp
import stat

def other_access(path, mode, uid, gids=None):


    if gids is None:
        gids = list()
    

    rpath = os.path.realpath(path)

    try:
        stat = os.stat(rpath)
    except FileNotFoundError:
        return False
    
    if mode == os.F_OK:
        # F_OK
        return True

    if uid==0:
        # root can read/write anything
        return True

    if stat.st_uid == uid:
        umode = (stat.st_mode & stat.S_IRWXU) >> 6
        return bool(mode & umode)

    if stat.st_gid in gids:
        gmode = (stat.st_mode & stat.S_IRWXG) >> 3
        return bool(mode & gmode)

    omode = stat.st_mode & stat.S_IRWXO
    return bool(mode & omode)


    # incomplete
    return False

def oaccess(path, mode, user, groups=None):
    if isinstance(user, str):
        uid = pwd.getpwnam(user).pw_uid
    else:
        uid = user
    
    if groups is not None:
        gids = [grp.getgrnam(group).gr_gid for group in groups]
    else:
        gids = [g.gr_gid for g in grp.getgrall() if user in g.gr_mem]
        gids.append(pwd.getpwnam(user).pw_gid)

    return other_access(path, mode, uid, gids)

