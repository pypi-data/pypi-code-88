#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import subprocess
from datetime import datetime

import configparser
import coloredlogs
import logging
import json
import itertools
import shlex
import time
import base64
import binascii
import queue
import sys
import os
import random
import hashlib
import sys
import tempfile
from jsonpath_ng import jsonpath, parse
from typing import Optional, List

from ph4runner import AsyncRunner

from .utils import try_fnc, slugify, get_cryptostreams_bin, get_sage_bin, get_sage_python_bin, eval_cryptostreams_to_file
from .qrng import Qrng

logger = logging.getLogger(__name__)
coloredlogs.install(level=logging.INFO)


def jsonpath(path, obj, allow_none=False):
    r = [m.value for m in parse(path).find(obj)]
    return r[0] if not allow_none else (r[0] if r else None)


def listize(obj):
    return obj if (obj is None or isinstance(obj, list)) else [obj]


def get_runner(cli, cwd=None, rtt_env=None):
    async_runner = AsyncRunner(cli, cwd=cwd, shell=False, env=rtt_env)
    async_runner.log_out_after = False
    async_runner.preexec_setgrp = True
    return async_runner


class DataGenerator:
    def __init__(self):
        self.args = None
        self.db = None
        self.rtt_config = None
        self.rtt_config_dir = None
        self.rtt_config_hash = None
        self.bool_config = None
        self.tmp_root = None
        self.tmp_dir = None
        self.parallel_tasks = None
        self.bool_wrapper = None
        self.temp_files = {}  # type: dict[str, tempfile.NamedTemporaryFile]
        self.cstream_files = {}  # type: dict[str, tempfile.NamedTemporaryFile]
        self.sage_bin = None
        self.sage_python_bin = None
        self.cs_bin = None
        self.python_bin = None

    def init_rtt_config(self):
        try:
            self.rtt_config_dir = os.path.dirname(self.args.rtt_config)
            with open(self.args.rtt_config) as fh:
                dt = fh.read()
                self.rtt_config = json.loads(dt)
                self.rtt_config_hash = hashlib.sha256(dt.encode("utf8")).hexdigest()

            self.bool_config = jsonpath('"toolkit-settings"."booltest"', self.rtt_config, False)
            if not self.bool_wrapper:
                self.bool_wrapper = jsonpath("$.wrapper", self.bool_config, True)

            if not self.args.threads:
                self.parallel_tasks = try_fnc(lambda: int(os.getenv('RTT_PARALLEL', None)))
            if not self.parallel_tasks:
                self.parallel_tasks = jsonpath('$."toolkit-settings".execution."max-parallel-tests"', self.rtt_config, True) or 1

        except Exception as e:
            logger.error("Could not load RTT config %s at %s" % (e, self.args.rtt_config), exc_info=e)

        finally:
            if self.parallel_tasks is None:
                self.parallel_tasks = self.args.threads or try_fnc(lambda: int(os.getenv('RTT_PARALLEL', None))) or 1

    def init_config_backend(self):
        if not self.args.back_config:
            return

        main_cfg = configparser.ConfigParser()
        main_cfg.read(self.args.back_config)
        if len(main_cfg.sections()) == 0:
            raise ValueError("Could not read backend config %s" % (self.args.back_config,))

        try:
            rtt_binary = main_cfg.get('RTT-Binary', 'Binary-path')
            booltest_rtt_binary = main_cfg.get('RTT-Binary', 'booltest-rtt-path')

        except BaseException as e:
            raise ValueError('Exception in config pocessing %s, %s' % (self.args.back_config, e))

    def init_config_defaults(self):
        if not self.bool_wrapper:
            self.bool_wrapper = "\"%s\" -m booltest.booltest_main" % sys.executable

    def run_job(self, cli):
        async_runner = get_runner(shlex.split(cli))

        logger.info("Starting async command %s" % cli)
        async_runner.start()

        while async_runner.is_running:
            time.sleep(1)
        logger.info("Async command finished")

    def resolve_rtt_exec_dir(self):
        if not self.rtt_config_dir:
            self.rtt_config_dir = os.getenv('RTT_EXEC')
        return self.rtt_config_dir

    def resolve_cstreams_bin(self):
        if not self.cs_bin:
            self.cs_bin = get_cryptostreams_bin(rtt_config=self.rtt_config, search_dir=self.resolve_rtt_exec_dir())
        return self.cs_bin

    def handle_input_files(self, config):
        """
        Process temp file records, generate to temp folder, create names
        input_files: {"file1": {"data":....}}
        """
        if 'input_files' not in config:
            return

        inp_files = config['input_files']
        for fname in inp_files:
            rec = inp_files[fname]
            data = rec['data']
            is_base64 = 'dtype' in rec and rec['dtype'] == 'base64'
            is_hexenc = 'dtype' in rec and rec['dtype'] == 'hex'
            is_binary = is_base64 or is_hexenc
            mode = 'w+' if not is_binary else 'w+b'

            # extension: type can contain base64, then decode as binary data (affects mode)
            suffix = slugify(fname)
            cur_file = tempfile.NamedTemporaryFile(mode, dir=self.tmp_dir.name,
                                                   prefix='rtt-data-file-', suffix='-%s' % suffix, delete=False)

            logger.info("Generating file: %s" % (cur_file.name,))
            if isinstance(data, (list, tuple, dict)):
                if 'stdout' in rec and rec['stdout']:  # cryptostreams hack, dump to stdout, pipe-able
                    data['stdout'] = True
                json.dump(data, cur_file)
            elif is_base64:
                cur_file.write(base64.b64decode(data))
            elif is_hexenc:
                cur_file.write(binascii.unhexlify(data))
            else:
                cur_file.write(data)
            cur_file.flush()

            self.temp_files[fname] = cur_file

    def handle_cstreams_files(self, config):
        """
        Process cryptostreams generated input files
        {"cstream_files": {"file1": {"data":{}}}}
        """
        if 'cstream_files' not in config:
            return

        cs_files = config['cstream_files']
        for fname in cs_files:
            rec = cs_files[fname]
            data = rec['data']
            stdout = 'stdout' in rec and rec['stdout']
            if stdout:
                data['stdout'] = True

            suffix = slugify(fname)
            cur_file = tempfile.NamedTemporaryFile('w+b', dir=self.tmp_dir.name,
                                                   prefix='rtt-cs-file-', suffix='-%s' % suffix, delete=False)

            logger.info("Generating CS-file: %s" % (cur_file.name,))
            eval_cryptostreams_to_file(self.resolve_cstreams_bin(), out_file=cur_file.name,
                                       tmpdir=self.tmp_dir.name, config=data)
            self.cstream_files[fname] = cur_file

    def substitute_files(self, template: str):
        """Substitutes temp files created by the program"""
        cmap = {'{{FILE_%s}}' % x.upper(): x for x in self.temp_files}
        res = template  # type: str
        for cfile in cmap:
            fname = cmap[cfile]
            tmp_file = self.temp_files[fname]  # type: tempfile.NamedTemporaryFile
            res = res.replace(cfile, os.path.abspath(tmp_file.name))
        return res

    def substitute_cs_files(self, template: str):
        """Substitutes cryptostreams-generated files"""
        cmap = {'{{CSFILE_%s}}' % x.upper(): x for x in self.cstream_files}
        res = template  # type: str
        for cfile in cmap:
            fname = cmap[cfile]
            tmp_file = self.cstream_files[fname]  # type: tempfile.NamedTemporaryFile
            res = res.replace(cfile, os.path.abspath(tmp_file.name))
        return res

    def substitute_bins(self, template: str):
        """Substitutes basic binaries resolved from the configuration"""
        if '{{CRYPTOSTREAMS_BIN}}' in template:
            self.resolve_cstreams_bin()
        if '{{PYTHON_BIN}}' in template and not self.python_bin:
            self.python_bin = sys.executable
        if '{{SAGE_BIN}}' in template and not self.sage_bin:
            self.sage_bin = get_sage_bin(rtt_config=self.rtt_config, search_dir=self.resolve_rtt_exec_dir())
        if '{{SAGE_PYTHON_BIN}}' in template and not self.sage_python_bin:
            self.sage_python_bin = get_sage_python_bin(rtt_config=self.rtt_config, search_dir=self.resolve_rtt_exec_dir())

        res = template
        if '{{CRYPTOSTREAMS_BIN}}' in template:
            res = res.replace('{{CRYPTOSTREAMS_BIN}}', self.cs_bin)

        res = res.replace('{{PYTHON_BIN}}', self.python_bin or 'python3')
        res = res.replace('{{SAGE_BIN}}', self.sage_bin or 'sage')
        res = res.replace('{{SAGE_PYTHON_BIN}}', self.sage_python_bin or 'sage -python')
        res = res.replace('{{RTT_EXEC}}', self.resolve_rtt_exec_dir() or '')
        res = res.replace('{{OFILE}}', self.args.data_path or '')
        return res

    def check_template_resolution(self, template):
        if '{{' in template:
            raise ValueError('Template contains unresolved {{ element')

    def substitute_template(self, template):
        res = self.substitute_files(template)
        res = self.substitute_cs_files(res)
        res = self.substitute_bins(res)
        self.check_template_resolution(res)
        return res

    def work(self):
        """
        read job config, supported usage:
          - executable stream first, usually sage script, e.g.,
            /full/sage-bin/path /full/script/path.sage

          - cstreams on input, pipe to executable

          - "shell" execution stream. cstreams -c=config.json | sage script.sage -b 512 -key 010203040405050503020
          config.json ideally stored here locally (all configs in one)

          - "configs" [{"name": "cstreams", data: ""}, ...], then referencable
            config: {"type": "configref", name: "cstreams"} OR directly in-place?

          - example config: {"stream": {"type": "shell", "exec": [], "exec": "", "stdin": {}}}
          - placeholders from the json path? sage, python, cryptostreams bin, ...
          {{CRYPTOSTREAMS_BIN}}, {{SAGE_BIN}}, {{SAGE_PYTHON_BIN}}, {{PYTHON_BIN}}

          - keys configurable as file? use cstreams/native generator to generate a temp file, placeholder then.
          "tempfiles": {}
        {
          "stream": {
            "type": "shell",
            "direct_file": false,
            "exec": "{{CRYPTOSTREAMS_BIN}} -c={{FILE_CONFIG1.JSON}} | {{SAGE_BIN}} {{RTT_EXEC}}/sage/lowmimc.sage -keys={{CSFILE_CSFILE1}}"
          },
          "input_files": {
            "CONFIG1.JSON": {
              "data": {"json_example_cfg":{}}
            },
            "CONFIG2.JSON": {
              "data": "0102030405",
              "dtype": "hex"
            }
          },
          "cstream_files": {
            "CSFILE1": {
              "data": {"seed": "4464a22651888b31", "stdout": true, ...}
            }
          }
        }
        """
        if not self.args.config:
            raise ValueError('Config file not provided')

        config = None
        with open(self.args.config) as fh:
            config = json.load(fh)

        if not config:
            raise ValueError('Invalid config file %s' % (self.args.config,))

        stream_type = config['stream']['type']
        if stream_type not in ['shell', 'qrng']:
            raise ValueError("Only master stream supported is {shell, qrng}")

        is_qrng = stream_type == 'qrng'
        stream = config['stream']
        direct_file = 'direct_file' in stream and stream['direct_file']

        scratch_tmp = tempfile.TemporaryDirectory(prefix='rtt-temp') if not self.args.scratch_dir else None
        self.tmp_root = self.args.scratch_dir if self.args.scratch_dir else scratch_tmp.name
        self.tmp_dir = tempfile.TemporaryDirectory(prefix='rtt-data-gen-', dir=self.tmp_root)

        self.handle_input_files(config)
        self.handle_cstreams_files(config)

        proc_stdout = None
        if direct_file:
            proc_stdout = sys.stdout.buffer  # exec cmd writes to file directly.
        elif self.args.data_path:
            proc_stdout = open(self.args.data_path, 'wb+')
        else:
            proc_stdout = sys.stdout.buffer

        if is_qrng:
            creds = self.substitute_template(stream['cred_file'])
            total_size = stream['total_size']
            creds_js = None
            with open(creds) as fh:
                creds_js = json.load(fh)

            qrng = Qrng(user=creds_js['user'], passwd=creds_js['passwd'])
            nread = 0
            while nread < total_size:
                for chunk in qrng.download():
                    csize = len(chunk)
                    if csize + nread > total_size:
                        chunk = chunk[:total_size - nread]
                    proc_stdout.write(chunk)
                    nread += len(chunk)
                    if nread >= total_size:
                        break

        else:
            exec = stream['exec']
            exec_is_str = isinstance(exec, str)
            exec_arr = exec if isinstance(exec, list) else [exec]
            exec_arr = [self.substitute_template(x) for x in exec_arr]
            exec = exec_arr if exec_is_str else exec_arr[0]
            logger.info('Starting generation process..., cmd: %s, direct: %s, file: %s'
                        % (exec, direct_file, self.args.data_path))

            p = subprocess.Popen(exec, shell=True, cwd=self.tmp_dir.name, stderr=sys.stderr, stdout=proc_stdout)
            out, err = p.communicate()
            if p.returncode != 0:
                logger.error('Could not generate data, code: %s, err: %s' % (p.returncode, err))
                raise ValueError("Generator failed to execute, return code: %")

        if not direct_file and self.args.data_path:
            proc_stdout.close()

        logger.info("Generator ended")

    def main(self):
        logger.debug('App started')

        parser = self.argparser()
        self.args = parser.parse_args()
        if self.args.debug:
            coloredlogs.install(level=logging.DEBUG)

        self.init_rtt_config()
        self.init_config_backend()
        self.init_config_defaults()
        self.work()

    def argparser(self):
        parser = argparse.ArgumentParser(description='RTT data generator')

        parser.add_argument('--debug', dest='debug', action='store_const', const=True,
                            help='enables debug mode')
        parser.add_argument('-s', '--rtt-config', dest='rtt_config',
                            help='RTT Configuration path')
        parser.add_argument('--back-config', dest='back_config',
                            help='Backend config path')
        parser.add_argument('-c', '--config', default=None,
                            help='Job config JSON')
        parser.add_argument('-f', '--data-path', dest='data_path', default=None,
                            help='Where to generate resulting file, if not defined, stdout is used')
        parser.add_argument('--scratch', dest='scratch_dir', default=None,
                            help='Scratch dir to use for temp files')
        parser.add_argument('-t', dest='threads', type=int, default=None,
                            help='Maximum parallel threads')
        return parser


def main():
    br = DataGenerator()
    return br.main()


if __name__ == '__main__':
    main()
