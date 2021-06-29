from src.pyenv import options, message

def main(exit: bool = False):
    if exit is False:
        print("FORMAT: {action}:{name} -> name can be optional")
        print("ACTIONS: create | activate | deactivate | show")
        options(str(input("Input action: ")))
    else:
        message("DISCONNECTED")


if __name__ == '__main__':
    message("WELCOME to pyenv.command")
    main()


