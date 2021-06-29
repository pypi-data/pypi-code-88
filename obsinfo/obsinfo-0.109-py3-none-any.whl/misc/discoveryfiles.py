import sys
import os
import re
from pathlib import Path
from urllib import parse as urlparse
from urllib.parse import urljoin 
from ..misc.remoteGitLab import gitLabFile

# We'll first create all the various objects. These strongly follow the
# hierarchy of StationXML files.

class Datapath(object):
    """
    Class to discover where information files are stored. GITLAB is used as a reserved word
    to signify the GITLAB repository
    """
    
    def __init__(self):
        """
        Create object
        """
        
        DATAPATH = os.environ.get('OBSINFO_DATAPATH')
        
        if DATAPATH:
           split_pattern = ':' if os.name == 'posix' else ';' 
           self.datapath_list = re.split(split_pattern, DATAPATH)
           i = 0
           for d in self.datapath_list:
               self.datapath_list[i] = re.sub('GITLAB/', 'http://www.gitlab.com/', d)
               i += 1
           
        else:  
           self.datapath_list = "./" # Use current directory as default.
        

    def build_datapath(self, file):
        """
        Create list of directories which may have data and schema
        """
        file, frag = urlparse.urldefrag(file)

        filestr = file if isinstance(file, str) else str(file)
        
        if not isinstance(file, Path):
            file = Path(file)
        
        if file.is_absolute(): 
            return filestr
    
        elif filestr[0:3] == "../" or filestr[0:2] == "./": # if path is absolute or relative to cwd:
            home = Path.cwd()
            self.datapath = str(Path.joinpath(home, file).resolve())
            return self.add_frag(self.datapath, frag)
                
        for dir in self.datapath_list:
             
            if gitLabFile.isRemote(dir):
                fn = urljoin(dir, filestr)
                if gitLabFile.get_gitlab_file(fn, False): #Check remote repository
                    self.datapath = fn
                    return self.add_frag(self.datapath, frag) # Don't forget to add frag back! 
            else:             
                fn = (Path(dir).resolve()).joinpath(file) 
                if os.path.isfile(str(fn)): # Check local repository
                   self.datapath = str(fn)
                   return self.add_frag(self.datapath, frag) # Don't forget to add frag back!

        raise FileNotFoundError(file)
    
    def add_frag(self, path, frag):
        
        return path + ("#" + frag if frag else "")
        