# -*- coding:utf-8 -*-
# Author: Jim
# Date: 2021-06-23 13:45
import datetime
import glob
import gzip
import io
import logging
import os
import platform
import shutil
import sys
import tarfile
import tempfile
import urllib
import zipfile
from logging import LogRecord
from typing import Tuple, Optional
from urllib.parse import urlparse
from pathlib import Path
import termcolor
from hanlp_downloader import Downloader
from hanlp_downloader.log import DownloadCallback

from staff_ocr import __version__


class ColoredFormatter(logging.Formatter):
    def __init__(self, fmt=None, datefmt=None, style='%', enable=True):
        super().__init__(fmt, datefmt, style)
        self.enable = enable

    def formatMessage(self, record: LogRecord) -> str:
        message = super().formatMessage(record)
        if self.enable:
            return color_format(message)
        else:
            return remove_color_tag(message)


def init_logger(name=None, root_dir=None, level=logging.INFO, mode='w',
                fmt="%(asctime)s %(levelname)s %(message)s",
                datefmt='%Y-%m-%d %H:%M:%S') -> logging.Logger:
    if not name:
        name = datetime.datetime.now().strftime("%Y-%m-%d_%H.%M.%S")
    rootLogger = logging.getLogger(os.path.join(root_dir, name) if root_dir else name)
    rootLogger.propagate = False

    consoleHandler = logging.StreamHandler(sys.stdout)  # stderr will be rendered as red which is bad
    consoleHandler.setFormatter(ColoredFormatter(fmt, datefmt=datefmt))
    attached_to_std = False
    for handler in rootLogger.handlers:
        if isinstance(handler, logging.StreamHandler):
            if handler.stream == sys.stderr or handler.stream == sys.stdout:
                attached_to_std = True
                break
    if not attached_to_std:
        rootLogger.addHandler(consoleHandler)
    rootLogger.setLevel(level)
    consoleHandler.setLevel(level)

    if root_dir:
        os.makedirs(root_dir, exist_ok=True)
        log_path = "{0}/{1}.log".format(root_dir, name)
        fileHandler = logging.FileHandler(log_path, mode=mode)
        fileHandler.setFormatter(ColoredFormatter(fmt, datefmt=datefmt, enable=False))
        rootLogger.addHandler(fileHandler)
        fileHandler.setLevel(level)

    return rootLogger


logger = init_logger(name='staff_ocr', level=os.environ.get('OCR_LOG_LEVEL', 'INFO'))


def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def now_filename(fmt="%y%m%d_%H%M%S"):
    """Generate filename using current datetime, in 20180102_030405 format
    Args:
      fmt:  (Default value = "%y%m%d_%H%M%S")
    Returns:

    """
    now = datetime.datetime.now()
    return now.strftime(fmt)


def make_debug_corpus(path, delimiter=None, percentage=0.1, max_samples=100):
    files = []
    if os.path.isfile(path):
        files.append(path)
    elif os.path.isdir(path):
        files += [os.path.join(path, f) for f in os.listdir(path) if
                  os.path.isfile(os.path.join(path, f)) and '.debug' not in f and not f.startswith('.')]
    else:
        raise FileNotFoundError(path)
    for filepath in files:
        filename, file_extension = os.path.splitext(filepath)
        if not delimiter:
            if file_extension in {'.tsv', '.conll', '.conllx', '.conllu'}:
                delimiter = '\n\n'
            else:
                delimiter = '\n'
        with open(filepath, encoding='utf-8') as src, open(filename + '.debug' + file_extension, 'w',
                                                           encoding='utf-8') as out:
            samples = src.read().strip().split(delimiter)
            max_samples = min(max_samples, int(len(samples) * percentage))
            out.write(delimiter.join(samples[:max_samples]))


def path_join(path, *paths):
    return os.path.join(path, *paths)


def makedirs(path):
    os.makedirs(path, exist_ok=True)
    return path


def tempdir(name=None):
    path = tempfile.gettempdir()
    if name:
        path = makedirs(path_join(path, name))
    return path


def tempdir_human():
    return tempdir(now_filename())


def hanlp_home_default():
    """Default data directory depending on the platform and environment variables"""
    if windows():
        return os.path.join(os.environ.get('APPDATA'), 'ocr_model')
    else:
        return os.path.join(os.path.expanduser("~"), '.ocr_model')


def windows():
    system = platform.system()
    return system == 'Windows'


def hanlp_home():
    """ Home directory for HanLP resources.

    Returns:
        Data directory in the filesystem for storage, for example when downloading models.

    This home directory can be customized with the following shell command or equivalent environment variable on Windows
    systems.

    .. highlight:: bash
    .. code-block:: bash

        $ export HANLP_HOME=/data/hanlp

    """
    return os.getenv('OCR_MODEL_HOME', hanlp_home_default())


def file_exist(filename) -> bool:
    return os.path.isfile(filename)


def remove_file(filename):
    if file_exist(filename):
        os.remove(filename)


def parent_dir(path):
    return os.path.normpath(os.path.join(path, os.pardir))


def cprint(*args, file=None, **kwargs):
    out = io.StringIO()
    print(*args, file=out, **kwargs)
    text = out.getvalue()
    out.close()
    c_text = color_format(text)
    print(c_text, end='', file=file)


def color_format(msg: str):
    for tag in termcolor.COLORS, termcolor.HIGHLIGHTS, termcolor.ATTRIBUTES:
        for c, v in tag.items():
            start, end = f'[{c}]', f'[/{c}]'
            msg = msg.replace(start, '\033[%dm' % v).replace(end, termcolor.RESET)
    return msg


def get_resource(path: str, save_dir=hanlp_home(), extract=True, append_location=True,
                 verbose=True) -> str:
    """Fetch real (local) path for a resource (model, corpus, whatever) to ``save_dir``.

    Args:
      path: A local path (which will returned as is) or a remote URL (which will be downloaded, decompressed then
        returned).
      save_dir: Where to store the resource (Default value = :meth:`hanlp.utils.io_util.hanlp_home`)
      extract: Whether to unzip it if it's a zip file (Default value = True)
      prefix: A prefix when matched with an URL (path), then that URL is considered to be official. For official
        resources, they will not go to a folder called ``thirdparty`` under :const:`~hanlp_common.constants.IDX`.
      append_location:  (Default value = True)
      verbose: Whether to print log messages.

    Returns:
      The real path to the resource.

    """

    anchor: str = None
    compressed = None
    if os.path.isdir(path):
        return path
    elif os.path.isfile(path):
        pass
    elif path.startswith('http:') or path.startswith('https:'):
        url = path
        if '#' in url:
            url, anchor = url.split('#', maxsplit=1)
        realpath = path_from_url(path, save_dir, append_location)
        realpath, compressed = split_if_compressed(realpath)
        # check if resource is there
        if anchor:
            if anchor.startswith('/'):
                # indicates the folder name has to be polished
                anchor = anchor.lstrip('/')
                parts = anchor.split('/')
                renamed_realpath = str(Path(realpath).parent.joinpath(parts[0]))
                if os.path.isfile(realpath + compressed):
                    os.rename(realpath + compressed, renamed_realpath + compressed)
                realpath = renamed_realpath
                anchor = '/'.join(parts[1:])
            child = path_join(realpath, anchor)
            if os.path.exists(child):
                return child
        elif os.path.isdir(realpath) or (os.path.isfile(realpath) and (compressed and extract)):
            return realpath
        else:
            if compressed:
                pattern = realpath + '.*'
                files = glob.glob(pattern)
                files = list(filter(lambda x: not x.endswith('.downloading'), files))
                zip_path = realpath + compressed
                if zip_path in files:
                    files.remove(zip_path)
                if files:
                    if len(files) > 1:
                        logger.debug(f'Found multiple files with {pattern}, will use the first one.')
                    return files[0]
        # realpath is where its path after exaction
        if compressed:
            realpath += compressed
        if not os.path.isfile(realpath):
            path = download(url=path, save_path=realpath, verbose=verbose)
        else:
            path = realpath
    if extract and compressed:
        path = uncompress(path, verbose=verbose)
        if anchor:
            path = path_join(path, anchor)

    return path


def download(url, save_path=None, save_dir=hanlp_home(), append_location=True, verbose=True):
    if not save_path:
        save_path = path_from_url(url, save_dir, append_location)
    if os.path.isfile(save_path):
        if verbose:
            eprint('Using local {}, ignore {}'.format(save_path, url))
        return save_path
    else:
        makedirs(parent_dir(save_path))
        if verbose:
            eprint('Downloading {} to {}'.format(url, save_path))
        tmp_path = '{}.downloading'.format(save_path)
        remove_file(tmp_path)
        try:
            downloader = Downloader(url, tmp_path, 4, headers={
                'User-agent': f'HanLP/{__version__} ({platform.platform()})'})
            if verbose:
                downloader.subscribe(DownloadCallback(show_header=False))
            downloader.start_sync()
        except BaseException as e:
            remove_file(tmp_path)
            url = url.split('#')[0]
            if not windows():
                hints_for_download = f'e.g. \nwget {url} -O {save_path}\n'
            else:
                hints_for_download = ' Use some decent downloading tools.\n'
            message = f'Download failed due to [red]{repr(e)}[/red]. Please download it to {save_path} by yourself. ' \
                      f'[yellow]{hints_for_download}[/yellow]'
            if verbose:
                cprint(message)
            if hasattr(e, 'msg'):
                e.msg += '\n' + remove_color_tag(message)
            raise e
        remove_file(save_path)
        os.rename(tmp_path, save_path)
    return save_path


def remove_color_tag(msg: str):
    for tag in termcolor.COLORS, termcolor.HIGHLIGHTS, termcolor.ATTRIBUTES:
        for c, v in tag.items():
            start, end = f'[{c}]', f'[/{c}]'
            msg = msg.replace(start, '').replace(end, '')
    return msg


def parse_url_path(url):
    parsed: urllib.parse.ParseResult = urlparse(url)
    path = os.path.join(*parsed.path.strip('/').split('/'))
    return parsed.netloc, path


def uncompress(path, dest=None, remove=True, verbose=True):
    """Uncompress a file and clean up uncompressed files once an error is triggered.

    Args:
      path: The path to a compressed file
      dest: The dest folder.
      remove: Remove archive file after decompression.
      verbose: ``True`` to print log message.

    Returns:
        Destination path.

    """
    # assert path.endswith('.zip')
    prefix, ext = split_if_compressed(path)
    folder_name = os.path.basename(prefix)
    file_is_zip = ext == '.zip'
    root_of_folder = None
    if ext == '.gz':
        try:
            with gzip.open(path, 'rb') as f_in, open(prefix, 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)
        except Exception as e:
            remove_file(prefix)
            remove_file(path)
            raise e
    else:
        try:
            with zipfile.ZipFile(path, "r") if ext == '.zip' else tarfile.open(path, 'r:*') as archive:
                if not dest:
                    namelist = sorted(archive.namelist() if file_is_zip else archive.getnames())
                    if namelist[0] == '.':
                        namelist = namelist[1:]
                        namelist = [p[len('./'):] if p.startswith('./') else p for p in namelist]
                    if ext == '.tgz':
                        roots = set(x.split('/')[0] for x in namelist)
                        if len(roots) == 1:
                            root_of_folder = next(iter(roots))
                    else:
                        # only one file, root_of_folder = ''
                        root_of_folder = namelist[0].strip('/') if len(namelist) > 1 else ''
                    if all(f.split('/')[0] == root_of_folder for f in namelist[1:]) or not root_of_folder:
                        dest = os.path.dirname(path)  # only one folder, unzip to the same dir
                    else:
                        root_of_folder = None
                        dest = prefix  # assume zip contains more than one file or folder
                if verbose:
                    eprint('Decompressing {} to {}'.format(path, dest))
                archive.extractall(dest)
                if root_of_folder:
                    if root_of_folder != folder_name:
                        # move root to match folder name
                        os.rename(path_join(dest, root_of_folder), path_join(dest, folder_name))
                    dest = path_join(dest, folder_name)
                elif len(namelist) == 1:
                    dest = path_join(dest, namelist[0])
        except Exception as e:
            remove_file(path)
            if os.path.exists(prefix):
                if os.path.isfile(prefix):
                    os.remove(prefix)
                elif os.path.isdir(prefix):
                    shutil.rmtree(prefix)
            raise e
    if remove:
        remove_file(path)
    return dest


def split_if_compressed(path: str, compressed_ext=('.zip', '.tgz', '.gz', 'bz2', '.xz')) -> Tuple[str, Optional[str]]:
    tar_gz = '.tar.gz'
    if path.endswith(tar_gz):
        root, ext = path[:-len(tar_gz)], tar_gz
    else:
        root, ext = os.path.splitext(path)
    if ext in compressed_ext or ext == tar_gz:
        return root, ext
    return path, None


def path_from_url(url, save_dir=hanlp_home(), append_location=True):
    if not save_dir:
        save_dir = hanlp_home()
    domain, relative_path = parse_url_path(url)
    if append_location:
        realpath = os.path.join(save_dir, relative_path)
    else:
        realpath = os.path.join(save_dir, os.path.basename(relative_path))
    return realpath
