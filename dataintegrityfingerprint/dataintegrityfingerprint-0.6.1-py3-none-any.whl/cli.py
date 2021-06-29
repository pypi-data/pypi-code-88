import os
import sys
import argparse

from . import DataIntegrityFingerprint
from . import __version__


def cli():

    def progress(count, total, status=''):
        bar_len = 50
        filled_len = int(round(bar_len * count / float(total)))
        percents = round(100.0 * count / float(total), 1)
        bar = '=' * filled_len + ' ' * (bar_len - filled_len)
        sys.stdout.write('{:5.1f}% [{}] {}\r'.format(percents, bar, status))
        sys.stdout.flush()

    parser = argparse.ArgumentParser(
        description="""Data Integrity Fingerprint (DIF)
Python Reference Implementation v{0}""".format(__version__),
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""Authors:
Oliver Lindemann <oliver@expyriment.org>
Florian Krause <florian@expyriment.org""")

    parser.add_argument("PATH", nargs='?', default=None,
                        help="the path to the data folder or file")
    parser.add_argument("-f", "--from-checksums-file",
                        dest="fromchecksumsfile", action="store_true",
                        help="Calculate dif from checksums file. " +
                             "PATH is a checksums file",
                        default=False)
    parser.add_argument("-a", "--algorithm", metavar="ALGORITHM",
                        type=str,
                        help="the hash algorithm to be used (default=sha256)",
                        default="sha256")
    parser.add_argument("-C", "--checksums", dest="checksums",
                        action="store_true",
                        help="print checksums only",
                        default=False)
    parser.add_argument("-D", "--dif-only", dest="difonly",
                        action="store_true",
                        help="print dif only",
                        default=False)
    parser.add_argument("-G", "--gui", dest="gui",
                        action="store_true",
                        help="open graphical user interface",
                        default=False)
    parser.add_argument("-L", "--list-available-algorithms", dest="listalgos",
                        action="store_true",
                        help="print available algorithms",
                        default=False)
    parser.add_argument("-s", "--save-checksums-file",
                        dest="savechecksumsfile", action="store_true",
                        help="save checksums to file",
                        default=False)
    parser.add_argument("-d", "--diff-checksums-file", metavar="CHECKSUMSFILE",
                        type=str,
                        help="Calculate differences of checksums file to " +
                             "CHECKSUMSFILE")
    parser.add_argument("-n", "--no-multi-processing", dest="nomultiprocess",
                        action="store_true",
                        help="switch of multi processing",
                        default="")
    parser.add_argument("-p", "--progress", dest="progressbar",
                        action="store_true",
                        help="show progressbar",
                        default=False)
    parser.add_argument("--non-crypthographic",
                        dest="noncrypto",
                        action="store_true",
                        help="allow non crypthographic algorithms " +
                             "(Not suggested, please read documentation " +
                             "carefully!)",
                        default=False)

    args = vars(parser.parse_args())

    if args['listalgos']:
        print("Crypothographic algorithms")
        print("- " + "\n- ".join(
            DataIntegrityFingerprint.CRYPTOGRAPHIC_ALGORITHMS))
        if args['noncrypto']:
            print("Non-crypothographic algorithms")
            print("- " + "\n- ".join(
                DataIntegrityFingerprint.NON_CRYPTOGRAPHIC_ALGORITHMS))
        sys.exit()

    if args['gui']:
        from .gui import start_gui
        start_gui(data_dir=args["PATH"], hash_algorithm=args["algorithm"])
        sys.exit()

    if args["PATH"] is None:
        print("Use -G to launch the GUI interface or -h for help.")
        sys.exit()

    dif = DataIntegrityFingerprint(
        data=args["PATH"],
        from_checksums_file=args['fromchecksumsfile'],
        hash_algorithm=args["algorithm"],
        multiprocessing=not(args['nomultiprocess']),
        allow_non_cryptographic_algorithms=args['noncrypto'])

    if not args['fromchecksumsfile'] and args['progressbar']:
        dif.generate(progress=progress)
        print("")

    # Output
    if args['savechecksumsfile']:
        outfile = os.path.split(
            dif.data)[-1] + ".{0}".format(dif._hash_algorithm)
        answer = "y"
        if os.path.exists(outfile):
            answer = input(
                "'{0}' already exists! Overwrite? [y/N]: ".format(outfile))
        if answer == "y":
            dif.save_checksums()
            print("Checksums have been written to '{0}'.".format(outfile))
        else:
            print("Checksums have NOT been written.")

    elif args['diff_checksums_file']:
        diff = dif.diff_checksums(args['diff_checksums_file'])
        if diff != "":
            print(diff)

    elif args['difonly']:
        print(dif)
    elif args['checksums']:
        print(dif.checksums.strip())
    else:
        print("Data Integrity Fingerprint (DIF)".format(__version__))
        print("")
        print("Folder: {0}".format(dif.data))
        print("Files: {0} included".format(dif.count_files()))
        print("Algorithm: {0}".format(dif.hash_algorithm))
        print("DIF: {}".format(dif))