def nitrogen_utils():
    txt = '''\
import os
import shutil


def get_path():
    """
    Get DATAPATH, SAVEDPATH and STASHPATH from environment variable
    
    :return: absolute path of datapath, savedpath, stashpath
    """
    datapath = os.environ.get('DATAPATH')
    savedpath = os.environ.get('SAVEDPATH')
    stashpath = os.environ.get('STASHPATH')
    return datapath, savedpath, stashpath
    

def get_cpu_num():
    """
    Get number of CPU cores.
    
    :return: NUM_CPU if user specified, else os.cpu_count() or 2/3 limit
    """
    n_cpu = os.getenv('NUM_CPU')
    all_cpu = os.cpu_count()-1 if os.cpu_count() > 1 else 1

    if not n_cpu:
        n_cpu = all_cpu
    else:
        n_cpu = int(n_cpu)
        if n_cpu > all_cpu:
            n_cpu = all_cpu

    limit = os.getenv('CPU')
    if limit:
        n_cpu = int(float(limit))

    print(f'n_cpu:{n_cpu}')
    return n_cpu


def create_workdir(dir_name='workdir'):
    """
    Create a work directory in STASHPATH or /home/
    
    :param dir_name: basename of work directory
    :return: absolute path of work directory
    """
    stashpath = os.getenv('STASHPATH')
    if stashpath:
        # xbcp
        workdir = os.path.join(stashpath, dir_name)
    else:
        # local
        workdir = os.path.join('/home/', dir_name)

    if os.path.exists(workdir):
        shutil.move(workdir, workdir.replace(dir_name, 'trash'))
    os.mkdir(workdir)
    return workdir


def get_env_param(env_str, default_value=None, type_func=str):
    """
    Read parameters from environment variables and perform type conversions.
    
    :param env_str: field for the value of an environment variable
    :param default_value: the default value of the parameter
    :param type_func: type conversion function. (eg. int, float, eval, str, etc.)
    :return: parameter value after type conversion
    """
    value = os.getenv(env_str)
    
    # for bool value
    if (value == True or value == False) and type_func == eval:
        return value
        
    if value:
        value = type_func(value)
    else:
        value = default_value
    print('ENV:', env_str, '| VALUE:', value, '| TYPE:', type(value))
    return value
    
    
class GetInputData:
    """
    Gets the absolute path of the input file from the /job/data/.
    """
    def __init__(self):
        self.datapath = '/job/data/' if os.path.exists('/job/data/') else os.getenv('DATAPATH')
        self.files = [os.path.join(self.datapath, i) for i in os.listdir(self.datapath)]
        
    def by_extension(self, ext):
        """
        Gets all files with a specific suffix name.
        
        :param ext: the specified end of the filename character
        :return: a list of absolute path to all files ending in ext.
        """
        return [i for i in self.files if i.endswith(ext)]

    def by_name(self, file_name):
        """
        Get the absolute path to a particular filename file.
        
        :param file_name: particular filename
        :return: the absolute path to the file
        """
        return [i for i in self.files if os.path.basename(i) == file_name or i == file_name][0]
'''
    return txt
