import os
import subprocess

def cmd(cmd, redirect=False):
    # create a subprocess to run the command
    if redirect:
        p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
        # wait for it to finish and grab the output
        output = p.communicate()[0].decode()
        # grab and return the exit code
        rc = p.poll()
        return rc, output
    else:
        p = subprocess.Popen(cmd, shell=True)
        # wait for it to finish
        p.wait()
        # grab and return the exit code
        rc = p.poll()
        return rc

def check_program(program):
    if os.name == 'nt':
        if cmd(f'where {program}', redirect=True)[0] == 0:
            return True
    else:
        if cmd(f'command -v {program}', redirect=True)[0] == 0:
            return True
    return False

if __name__ == '__main__':
    print(check_program('python'))