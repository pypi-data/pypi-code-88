import sys
import os
import time
import shutil
import tempfile
import subprocess
import json
import glob
import logging
import unicodedata
import re
from jsonpath_ng import jsonpath, parse


logger = logging.getLogger(__name__)


def try_fnc(fnc):
    try:
        return fnc()
    except:
        pass


def chunks(items, size):
    for i in range(0, len(items), size):
        yield items[i : i + size]


def jsonpath(path, obj, allow_none=False):
    r = [m.value for m in parse(path).find(obj)]
    return r[0] if not allow_none else (r[0] if r else None)


# Source: rtt-deployment-openshift/common/rtt_utils.py
def try_which(cmd):
    try:
        p = subprocess.Popen("which %s" % (cmd,), stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                             shell=True, text=True)
        stdout, stderr = p.communicate()
        if p.returncode == 0 and stdout.strip() != "":
            return stdout.strip()
    except:
        pass
    return None


def try_remove(path):
    if not path:
        return
    try:
        os.unlink(path)
    except:
        pass


# Source: rtt-deployment-openshift/common/rtt_cryptostreams.py, edited
def get_cryptostreams_bin(binpath=None, rtt_settings_path=None, rtt_config=None, search_dir=None):
    if binpath is not None and os.path.exists(binpath):
        return binpath

    if rtt_settings_path or rtt_config:
        if rtt_settings_path:
            with open(rtt_settings_path, 'r') as fh:
                rtt_config = json.load(fh)

        cand = jsonpath('$.toolkit-settings.binaries.cryptostreams', rtt_config, True)
        if cand is not None and os.path.exists(cand):
            return cand

    cand = os.getenv("CRYPTOSTREAMS")
    if cand is not None and os.path.exists(cand):
        return cand

    if search_dir is None and rtt_settings_path is not None:
        search_dir = os.path.dirname(rtt_settings_path)

    if search_dir:
        dname = search_dir
        cands = glob.glob('%s/crypto-streams*' % dname)
        if cands and len(cands) > 0 and os.path.exists(cands[0]):
            rcand = os.path.realpath(cands[0])
            if os.access(rcand, os.X_OK):
                return rcand

    cand = try_which('crypto-streams-v3.0')
    if cand is not None:
        return cand

    cand = try_which('crypto-streams')
    if cand is not None:
        return cand

    return None


def get_sage_bin(binpath=None, rtt_settings_path=None, rtt_config=None, search_dir=None):
    if binpath is not None and os.path.exists(binpath):
        return binpath

    if rtt_settings_path or rtt_config:
        if rtt_settings_path:
            with open(rtt_settings_path, 'r') as fh:
                rtt_config = json.load(fh)

        cand = jsonpath('$.toolkit-settings.binaries.sage', rtt_config, True)
        if cand is not None and os.path.exists(cand):
            return cand

    cand = os.getenv("SAGE_PATH")
    if cand is not None and os.path.exists(cand):
        return cand

    if search_dir is None and rtt_settings_path is not None:
        search_dir = os.path.dirname(rtt_settings_path)

    if search_dir:
        cand = os.path.realpath(os.path.join(search_dir, 'sage'))
        if os.path.exists(cand):
            if os.access(cand, os.X_OK):
                return cand
            else:
                logger.info("sage found in search-dir but it is not executable")

    cand = try_which('sage')
    if cand is not None:
        return cand

    return None


def get_sage_python_bin(binpath=None, rtt_settings_path=None, rtt_config=None, search_dir=None):
    if binpath is not None and os.path.exists(binpath):
        return binpath

    if rtt_settings_path or rtt_config:
        if rtt_settings_path:
            with open(rtt_settings_path, 'r') as fh:
                rtt_config = json.load(fh)

        cand = jsonpath('$.toolkit-settings.binaries.sage-python', rtt_config, True)
        if cand is not None and os.path.exists(cand):
            return cand

    cand = os.getenv("SAGE_PYTHON_PATH")
    if cand is not None and os.path.exists(cand):
        return cand

    if search_dir is None and rtt_settings_path is not None:
        search_dir = os.path.dirname(rtt_settings_path)

    if search_dir:
        cand = os.path.realpath(os.path.join(search_dir, 'sage-python'))
        if os.path.exists(cand):
            if os.access(cand, os.X_OK):
                return cand
            else:
                logger.info("sage found in search-dir but it is not executable")

    sage = get_sage_bin(rtt_settings_path=rtt_settings_path, rtt_config=rtt_config, search_dir=search_dir)
    if not sage:
        return None

    # auto-detect
    try:
        sage_dir = os.path.dirname(os.path.realpath(sage))
        cands = [
            os.path.join(sage_dir, 'local/bin/python3'),
            os.path.join(sage_dir, 'local/bin/python'),
        ]

        for c in cands:
            if os.path.exists(c) and os.access(c, os.X_OK):
                return c

    except Exception as e:
        pass

    return None


# Source: rtt-deployment-openshift/common/rtt_cryptostreams.py
def eval_cryptostreams_to_file(generator_path, out_file, tmpdir, config_file=None, config=None):
    new_tmp_dir = None
    tmp_cfg_file = None
    try:

        if tmpdir is None:
            new_tmp_dir = tempfile.TemporaryDirectory('-cryptostreams')
            tmpdir = new_tmp_dir.name

        if config_file:
            with open(config_file) as fh:
                config = json.load(fh)

        if not config:
            raise ValueError('Cryptostreams config is empty')

        config['stdout'] = True
        tmp_cfg_file = tempfile.NamedTemporaryFile('w+', suffix="-generator", dir=tmpdir, delete=False)
        tmp_cfg_file.write(json.dumps(config))
        tmp_cfg_file.flush()

        cmd = "%s -c=\"%s\" > %s" % (generator_path, os.path.abspath(tmp_cfg_file.name), out_file)
        p = subprocess.Popen(cmd, shell=True, cwd=tmpdir, stderr=subprocess.PIPE)
        out, err = p.communicate()
        if p.returncode != 0:
            logger.error('Could not generate data, code: %s, err: %s' % (p.returncode, err))
            raise ValueError("Cryptostreams failed to execute, return code: %")

    except Exception as e:
        logger.error("Exception in cryptostreams eval, %s" % (e,), exc_info=e)

    finally:
        if tmp_cfg_file:
            try_remove(tmp_cfg_file)


# Source: rtt-deployment-openshift/files/run_jobs.py
def get_rtt_root_dir(config_dir):
    CACHE_CONFIG_DIR = "config_files"  # rtt_constants.Backend.CACHE_CONFIG_DIR
    config_els = config_dir.split(os.sep)
    base_els = CACHE_CONFIG_DIR.split(os.sep)
    return os.sep.join(config_els[:-1 * len(base_els)])


def slugify(value, allow_unicode=False):
    """
    Taken from https://github.com/django/django/blob/master/django/utils/text.py
    Convert to ASCII if 'allow_unicode' is False. Convert spaces or repeated
    dashes to single dashes. Remove characters that aren't alphanumerics,
    underscores, or hyphens. Convert to lowercase. Also strip leading and
    trailing whitespace, dashes, and underscores.
    """
    value = str(value)
    if allow_unicode:
        value = unicodedata.normalize('NFKC', value)
    else:
        value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore').decode('ascii')
    value = re.sub(r'[^\w\s-]', '', value.lower())
    return re.sub(r'[-\s]+', '-', value).strip('-_')

