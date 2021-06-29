from repostruc.argHandler import GetArgumentParser
from repostruc.returnUtils import ReturnHandler
from repostruc.treeUtils import TreeHandler
from pathlib import Path

def main():
    """
    Main function which handles argumenst passed,
    and calls respective functions. 

    """
    argparse = GetArgumentParser()
    arguments = argparse.getArguments()
    cur_dir = Path.cwd()
    if arguments['--clip']:
        ReturnHandler.copyToClipboard(TreeHandler.formatTree(cur_dir))
    elif arguments['-f'] or arguments['--file']:
        file_path = Path.absolute(Path(arguments['<filepath>'])) if arguments['<filepath>'] else Path('PROJECTINFO.md') 
        ReturnHandler.saveAsFile(
            TreeHandler.formatTree(cur_dir),
            file_path,
            arguments['--readme']
            )
    else:
        print(argparse.doc)


if __name__ == '__main__' :
    main()