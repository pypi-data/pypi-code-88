import replitdb.commands
def DeprecationWarning(text):
    print(f"\033[1;31mDeprecationWarning: {text}\033[0;0m")


def main():
	DeprecationWarning("This package has been deprecated use the offical one found at: https://pypi.org/p/replit")
	return
    import sys
    import os
    del sys.argv[0]
    url = False
    setUrl = os.environ['REPLIT_DB_URL']
    args = []
    for i in sys.argv:
      if(url):
        url = False
        setUrl = i
      elif(i.lower()=='-url'):
        url = True
      else:
        args.append(i)
    try:
      replitdb.commands.commandHandler(args,setUrl)
    except IndexError:
      print('Too little arguments entered (requesrs at leat 2)')


if __name__ == '__main__':
    main()