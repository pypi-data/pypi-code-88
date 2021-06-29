from gitignore_parser import parse_gitignore
from pathlib import Path
import pyperclip

class TreeHandler():
    """
    TreeHandler contains methods to handle the Directory tree :
    
    @functions
    getTree    => Returns visual tree structure.
    formatTree => Formats tree structure.
    
    """

    # prefix components:
    space =  '    '
    branch = '│   '
    # pointers:
    tee =    '├── '
    last =   '└── '

    ignore_files = ['.git','__pycache__','node_modules','.env']

    @staticmethod
    def getTree(dir_path: Path, prefix: str='', gitignore_path: Path='.gitignore'):
        """
        A recursive generator function,
        which yeilds a visual tree structure line by line.

        @param dir_path: Path object of targeted directory 
        @param prefix: Prefix for every level of the tree structure 
        @param ignore_files: Files and directories to ignore

        """    
        if Path(gitignore_path).is_file():
            matches_gitignore = parse_gitignore(gitignore_path)
            contents = [path for path in dir_path.iterdir() if not matches_gitignore(path.absolute()) and not path.name.endswith('.git')]
        else:
            contents = [path for path in dir_path.iterdir() if path.name not in TreeHandler.ignore_files]
        pointers = [TreeHandler.tee] * (len(contents) - 1) + [TreeHandler.last]
        for pointer, path in zip(pointers, contents):
            yield prefix + pointer + path.name
            if path.is_dir(): 
                extension = TreeHandler.branch if pointer == TreeHandler.tee else TreeHandler.space 
                yield from TreeHandler.getTree(path, prefix=prefix+extension,gitignore_path=gitignore_path)

    @staticmethod
    def formatTree(dir_path: Path, gitignore_path: Path='.gitignore', dsc_spacing: int=4, base_spacing: int=2):
        """
        Adds spacing before and after every file.

        @param dir_path: Path object of targeted directory.
        @param dsc_spacing: Spacing between file and discription.
        @param base_spacing: Spacing before file. 

        @return List of tree contents.
        """
        tree_contents = [line for line in TreeHandler.getTree(Path().absolute(),gitignore_path=gitignore_path)]
        max_string_length = max(tree_contents, key=len)
        tree_contents = [' '*base_spacing + line + ' '*int(dsc_spacing + len(max_string_length) - len(line)) + '<- DSC' for line in tree_contents]
        return tree_contents
