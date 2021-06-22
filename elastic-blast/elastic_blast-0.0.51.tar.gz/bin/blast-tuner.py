#!/usr/bin/env python3
#                           PUBLIC DOMAIN NOTICE
#              National Center for Biotechnology Information
#  
# This software is a "United States Government Work" under the
# terms of the United States Copyright Act.  It was written as part of
# the authors' official duties as United States Government employees and
# thus cannot be copyrighted.  This software is freely available
# to the public for use.  The National Library of Medicine and the U.S.
# Government have not placed any restriction on its use or reproduction.
#   
# Although all reasonable efforts have been taken to ensure the accuracy
# and reliability of the software and data, the NLM and the U.S.
# Government do not and cannot warrant the performance or results that
# may be obtained by using this software or data.  The NLM and the U.S.
# Government disclaim all warranties, express or implied, including
# warranties of performance, merchantability or fitness for any particular
# purpose.
#   
# Please cite NCBI in any work or product based on this material.
"""
blast-tuner.py - See DESC constant below

Author: Christiam Camacho (camacho@ncbi.nlm.nih.gov)
Created: Tue 21 Apr 2020 12:07:42 PM EDT
"""
import os
import argparse
import json
import logging
from elastic_blast import VERSION
from elastic_blast.config import configure
from elastic_blast.util import ElbSupportedPrograms, UserReportError
from elastic_blast.util import get_query_batch_size, config_logging
from elastic_blast.tuner import get_db_data, SeqData, MTMode, MolType
from elastic_blast.tuner import get_mt_mode, get_num_cpus, get_batch_length
from elastic_blast.base import DBSource, PositiveInteger
from elastic_blast.constants import CFG_BLAST, CFG_CLUSTER
from elastic_blast.constants import CFG_BLAST_DB, CFG_BLAST_PROGRAM, CFG_BLAST_BATCH_LEN
from elastic_blast.constants import CFG_BLAST_OPTIONS, CFG_CLUSTER_NUM_CPUS

DESC = r"""This application's purpose is to provide suggestions to run help run
BLAST efficiently. It is meant to be used in conjunction with BLAST+ and
ElasticBLAST."""


def main():
    """ Entry point into this program. """
    try:
        parser = create_arg_parser()
        args = parser.parse_args()
        config_logging(args)
        cfg = configure(args)

        options = '' if args.options is None else args.options

        conf = {CFG_BLAST: {}, CFG_CLUSTER: {}}
        if args.db is not None:
            db_source = DBSource[args.db_source]
            db_data = get_db_data(args.db, db_source)
            conf[CFG_BLAST][CFG_BLAST_DB] = args.db

        query_data = SeqData(args.total_query_length, MolType(args.query_mol_type.lower()))
        mt_mode = get_mt_mode(args.program, args.options, db_data, query_data)
        options += f' {mt_mode}'

        num_cpus = get_num_cpus(mt_mode = mt_mode, query = query_data)
        conf[CFG_BLAST][CFG_BLAST_PROGRAM] = args.program
        conf[CFG_BLAST][CFG_BLAST_BATCH_LEN] = str(get_batch_length(program = args.program,
                                                          mt_mode = mt_mode,
                                                          num_cpus = num_cpus))

        if len(options):
               conf[CFG_BLAST][CFG_BLAST_OPTIONS] = options

        conf[CFG_CLUSTER][CFG_CLUSTER_NUM_CPUS] = str(num_cpus)


        print('Please consider the following ElasticBLAST configuration settings:\n')

        for section in [CFG_BLAST, CFG_CLUSTER]:
            print(f'\t[{section}]')
            for key, value in sorted(conf[section].items(), key=lambda x: x[0]):
                print(f'\t{key} = {value}')
            print('')

        return 0
    except UserReportError as err:
        logging.error(err.message)
        return err.returncode


def create_arg_parser():
    """ Create the command line options parser object for this script. """
    DFLT_LOGFILE = 'stderr'
    parser = argparse.ArgumentParser(prog=os.path.basename(os.path.splitext(sys.argv[0])[0]), 
                                     description=DESC)
    parser._action_groups.pop()
    required = parser.add_argument_group('required arguments')
    optional = parser.add_argument_group('optional arguments')
    required.add_argument("--db", type=str, help="BLAST database to search", required=True)
    optional.add_argument("--db-source", type=str, help="Where NCBI-provided databases are downloaded from", choices=['AWS', 'GCP', 'NCBI'], default='AWS')
    required.add_argument("--program", type=str, help="BLAST program to run",
                        choices=ElbSupportedPrograms().get(), required=True)
    required.add_argument("--total-query-length", type=PositiveInteger,
                        help='Number of residues or bases in query sequecnes')
    required.add_argument("--query-mol-type", type=str,
                        help='Query molecular type: prot or nucl',
                        choices=['prot', 'nucl'], required=True)
    optional.add_argument("--options", type=str, help='BLAST options', default='')
    optional.add_argument('--version', action='version',
                        version='%(prog)s ' + VERSION)
    optional.add_argument("--logfile", default=DFLT_LOGFILE, type=str,
                        help="Default: " + DFLT_LOGFILE)
    optional.add_argument("--loglevel", default='INFO',
                        choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"])
    return parser


if __name__ == "__main__":
    import sys, traceback
    try:
        sys.exit(main())
    except Exception as e:
        traceback.print_exc(file=sys.stderr)
        sys.exit(1)

