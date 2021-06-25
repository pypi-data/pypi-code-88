# coding=utf-8

import logging
import os.path

from astropy.io import fits

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('FitsSanitizer')


# You can import this and use the two functions at your convenience
# or call this script : `python fits_sanitizer.py FILE`
# See options with `python fits_sanitizer.py -h`
# Note that you can use wildcards in the FILE.


def sanitize_fits_file(filename, prefix=''):
    fits_file = fits.open(filename)
    fits_file, fits_has_changed = sanitize_fits(fits_file)
    if fits_has_changed:
        prefix = str(prefix)
        filename = os.path.join(os.path.dirname(filename), prefix+os.path.basename(filename))
        fits_file.writeto(filename, clobber=True)


def sanitize_fits(hdulist):
    assert isinstance(hdulist, fits.HDUList)
    fits_has_changed = False
    for header_index, header in enumerate(hdulist):
        header = header.header
        for key in header:
            value = header.get(key)
            #print key+' -- '+str(value)
            changed = False

            # Lowercase 'DEG' to 'deg'
            if value == 'DEG':
                value = 'deg'
                changed = True
                logger.info("Lowercased %s 'DEG' into 'deg'.", key)

            if changed:
                fits_has_changed = True
                header.set(key, value)

        # Set um (microns) as the default CUNIT3 when missing
        #if not header.get('CUNIT3'):
        #    header.set('CUNIT3', 'um')

    return hdulist, fits_has_changed


# MAIN SCRIPT RUN WHEN LAUNCHED FROM CLI
if __name__ == '__main__':

    from argparse import ArgumentParser
    from argparse import RawTextHelpFormatter

    def is_valid_file(parser, arg):
        if not os.path.exists(arg):
            parser.error("The file %s does not exist!" % arg)
        else:
            return arg

    parser = ArgumentParser(formatter_class=RawTextHelpFormatter, description="""
Sanitize specified FITS files. By default, this will overwrite the FITS files.
To create another file(s), you can specify a prefix using the --prefix option.
What this actually does :
    - Lowercase 'DEG' unit
    - that's all folks !""")
    parser.add_argument('filenames', metavar='FILE', nargs='+',
                        type=lambda x: is_valid_file(parser, x),
                        help='A FITS file to sanitize')
    parser.add_argument('--prefix', dest='prefix', default='',
                        help='A prefix to prepend to the filename(s), to create new files')

    args = parser.parse_args()

    for filename in args.filenames:
        sanitize_fits_file(filename, args.prefix)
