import os
import mimetypes
from datetime import datetime
import tarfile
from pathlib import Path


class FileScanner:

    def __init__(self, collection, path):
        self.collection = collection
        self.path = path

    def _new_entry(self):
        return {
            'xml': None,
            'images': [],
            'run_id': None,
            'last_modified': None,
            'lire': None
        }

    def to_csv(self, path_to_file):
        data = self.get_raw_files()
        self._to_csv(path_to_file, data)

    def _to_csv(self, path_to_file, data):
        with open(path_to_file, 'w') as fin:
            for appnum in data.keys():
                high_image = None
                icon_image = None
                thumbnail_image = None
                tmp = data[appnum]
                if not tmp.get('xml'):
                    continue
                for f in tmp['images']:
                    if '.high' in f:
                        high_image = f
                    if '-ic' in f:
                        icon_image = f
                    if '-th' in f:
                        thumbnail_image = f
                # Appnum, Copy, HIGH, TUMB, ICON, LIRE, Last_updated
                line = '%s,%s,%s,%s,%s,%s,%s;\n' % (appnum, tmp['xml'],
                                                       high_image,
                                                       thumbnail_image,
                                                       icon_image,
                                                       tmp['lire'] if high_image else None,
                                                       tmp['last_modified'])
                line = line.replace('None', '')
                fin.write(line)

    def extract_release(self, tar_file, file_name):
        local_files = {}
        my_tar = tarfile.open(tar_file)
        for member in my_tar.getnames():
            member = '/'.join(member.split('/')[2:])
            path = os.path.join(self.path, member)
            if os.path.isdir(path):
                continue
            if member.endswith('.gz'):
                full_appnum = os.path.basename(member).replace('.xml.gz', '')
                tmp = full_appnum.split('_')
                if len(tmp) > 1 and '.' in tmp[-1]:
                    appnum = '_'.join(tmp[0:-1])
                else:
                    appnum = full_appnum
                p = Path(os.path.dirname(path))
                files = list(p.glob('**/%s*' % appnum))
                for f in files:
                    self._prepare_entry(os.path.dirname(path), f.name, local_files)
        self._to_csv(file_name, local_files)

    def from_csv(self, path_to_file, start=0, end=None):
        local_files = {}
        run_id = os.path.basename(path_to_file).split('_')[0].replace('snapshot.', '').replace('release.', '')
        run_id = run_id.replace('.', '_')
        with open(path_to_file, 'r') as fout:
            cursor = 0
            for line in fout.readlines():
                cursor += 1
                if cursor < start:
                    continue
                if end and cursor > end:
                    break
                line = line.replace(';', '')
                tmp = line.split(',')
                appnum = tmp[0]
                # Appnum, Copy, HIGH, TUMB, ICON, LIRE, Last_updated
                local_files[appnum] = self._new_entry()
                local_files[appnum]['xml'] = tmp[1]
                local_files[appnum]['run_id'] = run_id
                local_files[appnum]['lire'] = tmp[5]
                local_files[appnum]['last_modified'] = tmp[6]
                local_files[appnum]['images'].append(tmp[2])
                local_files[appnum]['images'].append(tmp[3])
                local_files[appnum]['images'].append(tmp[4])
        return local_files

    def get_raw_files(self):
        local_files = {}
        for root, dirs, files in os.walk(self.path):
            for f in files:
                self._prepare_entry(root, f, local_files)
        return local_files

    def _prepare_entry(self, root, f, local_files):
        file_path = os.path.abspath(os.path.join(root, f))
        file_mime = mimetypes.guess_type(f)[0]
        if not os.path.exists(file_path):
            return
        if f.endswith('.gz'):
            stat = os.stat(file_path)
            last_modified = datetime.fromtimestamp(stat.st_mtime)
            full_appnum = f.replace('.xml.gz', '')
            tmp = full_appnum.split('_')
            if len(tmp) > 1 and '.' in tmp[-1]:
                appnum = '_'.join(tmp[0:-1])
            else:
                appnum = full_appnum
            if appnum not in local_files.keys():
                local_files[appnum] = self._new_entry()
            local_files[appnum]['xml'] = file_path
            local_files[appnum]['last_modified'] = last_modified.strftime("%Y-%m-%d %H:%M:%S")
        elif (file_mime or '').startswith('image/'):
            name, _ = os.path.splitext(f)
            appnum = name.replace('-th', '').replace('.high', '').replace('-ic', '')
            if appnum not in local_files.keys():
                local_files[appnum] = self._new_entry()
            local_files[appnum]['images'].append(file_path)
        elif '.lire8.xml' in f:
            appnum = f.split('.')[0]
            if appnum not in local_files.keys():
                local_files[appnum] = self._new_entry()
            local_files[appnum]['lire'] = file_path


