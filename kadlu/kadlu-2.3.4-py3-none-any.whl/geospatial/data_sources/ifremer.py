import os
import sys
import logging
import requests
from ftplib import FTP

import kadlu

def fetch_netcdf_FTP(ftpurl, ftpdir, localdir):
    """ fetch files from an FTP server

        args:
            ftpurl: string
                FTP domain to connect
            ftpdir: string
                collect files within this FTP path directory
            localdir: string
                save files to this location
    """
    ftp = FTP(ftpurl)
    ftp.login()
    ftp.cwd(ftpdir)
    with kadlu.Capturing() as output: ftp.retrlines('NLST')
    for ncfile in [f for f in output if kadlu.ext(f, ('.nc',))]:
        logging.info(f'fetching {ncfile}')
        with open(f'{localdir}{ncfile}', 'wb') as fp:
            ftp.retrbinary(f'RETR {ncfile}', fp.write)


class Ifremer():
    """ collect files from ifremer FTP server """

    def fetch_ifremer_netcdf_hs2013(self, localdir=f'{kadlu.storage_cfg()}testfiles/'): 
        """ download netcdf waveheight files for testing kadlu """
        if not os.path.isdir(localdir): os.mkdir(localdir)
        fetch_netcdf_FTP(ftpurl='ftp.ifremer.fr', ftpdir='/ifremer/ww3/HINDCAST/ATNW/2013_CFSR/hs/', localdir=localdir)


