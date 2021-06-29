import subprocess
import os


def options(command: str):
    exit_main = False
    cmd = command.split(":")
    if len(cmd) >= 2:
        [action, name] = cmd
        if action == "create":
            state_env_name(name)
        elif action == "activate":
            activate_env(name)
            exit_main = True
        elif action == "show":
            environment_value(name)
        else:
            print("{message}: ".format(message=message("INVALID COMMAND")))
    elif len(cmd) == 1:
        [action] = cmd
        if action == "show":
            show_all_environment()
        else:
            print("{message}: ".format(message=message("INVALID COMMAND")))
    else:
        print("{message}: ".format(message=message("INVALID COMMAND")))
    main(exit=exit_main)


def message(title: str):
    return f'======= {title} ======='


def state_env_name(name: str):
    subprocess.call(["python3", "-m", "venv", name])
    message("Success")


def activate_env(name: str):
    try:
        subprocess.call(["source", "{name}/bin/activate".format(name=name)])
    except OSError as error:
        message("INVALID")
        error_message(str(OSError), str(error))


def show_all_environment():
    for key, value in os.environ.items():
        print(f'{key}={value}')


def environment_value(key: str) -> str:
    return os.getenv(key)


def error_message(os_error: str, msg: str):
    print(f'{os_error}: {msg}')
