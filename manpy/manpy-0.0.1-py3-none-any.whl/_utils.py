import os
import re
import shutil


def checking_boolean_input(msg=None):
    if msg is not None:
        print(msg + '([y]/n) ?')
    test = input('>')
    if test == 'y' or test == 'Y':
        return True
    elif test == 'n':
        return False
    else:
        print('Invalid choice:', test)
        return checking_boolean_input()


def checking_special_character(msg=None):
    if msg is not None:
        print(msg)
    test = input('>')
    for c in "@_!#$%^&*()<>?/\|}{~:;.[]":
        if c in test:
            print('Not allowed special character:', c, 'in', test)
            checking_special_character()
    else:
        return test

def modify_setup(file:str, modifs:dict, anchor_before, anchor_middle, anchor_after):
    shutil.move(file, file + "~")
    destination = open(file, "w")
    source = open(file + "~", "r")
    line = source.readline()
    print("Checking", file)
    while line:
        if line.strip() == "# manpy: start":
            while line.strip() != "# manpy: end":
                for key in modifs.keys():
                    value = re.findall(anchor_before + key + anchor_middle + "(.*?)" + anchor_after, line)
                    if value:
                        if value[0] == modifs[key]:
                            print("  "+ u"\u2713" + " Nothing to change for", key)
                        else:
                            print("  "+ u'\u00b1' + " Updating value for", key, f'{value[0]} -> {modifs[key]}')
                            # line = re.sub('    '+key+'="(.*?)",', '    '+key+f'="{modifs[key]}",', line)
                            line = re.sub(anchor_before + key + anchor_middle + "(.*?)" + anchor_after,
                                          anchor_before + key + anchor_middle + modifs[key] + anchor_after,
                                          line)
                destination.write(line)
                line = source.readline()
            destination.write(line)
        else:
            destination.write(line)
        line = source.readline()
    source.close()
    destination.close()
    os.remove(file + "~")

