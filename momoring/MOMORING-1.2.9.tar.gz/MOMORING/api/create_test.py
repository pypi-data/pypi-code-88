import os
import shutil
from MOMORING.modules.files.test_template import get_test_template


def create_test_dir(path):
    template = get_test_template(path)
    test_py_path = os.path.join(path, 'test.py')
    if not os.path.exists(test_py_path):
        with open(test_py_path, 'w') as f:
            f.write(template)

    test_dir = os.path.join(path, 'test')
    if os.path.exists(test_dir):
        shutil.rmtree(test_dir)
    os.mkdir(test_dir)

    for i in ['datapath', 'stashpath', 'savedpath']:
        new_dir_path = os.path.join(test_dir, i)
        if os.path.exists(new_dir_path):
            shutil.rmtree(new_dir_path)
        os.mkdir(new_dir_path)
