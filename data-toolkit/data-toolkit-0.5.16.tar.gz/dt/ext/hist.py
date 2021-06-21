import sys
import pandas as pd
import datetime as dt
import subprocess as sp
from Levenshtein import distance as dist
import os
import humanize

term_wdith = os.get_terminal_size().columns

pd.set_option('display.max_colwidth',term_wdith - 20)

# TODO: treat 'cd' in a special way s.t. we can generate the absolute path wherever possible
# TODO: treat 'cd' in a specical way so that it can keep track of location.
FILTER_TERMS = ['ls','install','dt hist', 'git ', 'dt ', 'code',
                'ipython','htop','git push','git pull','git stash',
                'tmux', 'nvidia-smi', 'ping']

def dt_conv(l: str):
    try:
        # TODO: correct timezone? why does midnight show up as 4 pm?
        pd_dt_repr = pd.to_datetime(dt.datetime.fromtimestamp(int(l[1].strip())))
        # ret_val = '_'.join(str(pd_dt_repr).split(' ')[::-1])
        return  humanize.naturaldelta(pd_dt_repr)
    except ValueError as e:
        # TODO: why does this occur
        # print(e)
        pass


def filter_term(term: tuple):
    # Logic: all filter terms need to _not_ match
    if 'cd' in term[0][:2]:
        try:
            if term[0].split(' ')[1][0] not in ['~','/']:
                return False
            else:
                return True
        except:
            print(f"Error with {term[0]}")

    return all([ft not in term[0] for ft in FILTER_TERMS])

def hist_tail(n_lines=20):
    shell = os.environ['SHELL'].split('/')[-1]

    if shell=='sh': shell = 'bashrc'

    # checks that we can find 
    zsh_hist = f"{os.path.expanduser('~')}/.{shell}_history"
    if not os.path.exists(zsh_hist):
        # dumb hack for bashrc
        # zsh_hist = f"{os.path.expanduser('~')}/.{shell}rc"
        # if not.path.exists(zsh_hist): raise NotImplementedError('Not sure where to look')
    # else:
        raise NotImplementedError('Not sure where to look')
    split_f = str(sp.check_output(['tail',zsh_hist,'-n',str(n_lines * 5)])).split(':')

    # TODO: \n -> \\n for Mac, check if this is an issue on Linux
    # Work Ubuntu 20.04 so far so good
    parsed_commands = [ ''.join(l.replace('\\n','').strip().split(';')[-1:]) for l in split_f if '\\n' in l]
    parsed_dt = [ t for t in split_f if '\\n' not in t]

    parsed = list(zip(parsed_commands, parsed_dt))

    # remove FILTER_TERMS 
    cmds = [ t for t in parsed if filter_term(t) ]

    # identify Levenstein distance
    lev_dist = [ dist(cmds[i][0],cmds[i+1][0]) for i in range(len(cmds)-1) ]

    # TODO: make more efficent
    # Lev dist with previous terms (1 approx to catch typos)
    ld = lev_dist + [9999]
    # dist_dict = { k:v for k,v in zip(cmds,ld) }
    dist_dict = { k:v for k,v in zip(cmds,ld) if v>4 }
    # TODO check if ordered before
    last_list = list(dist_dict.keys())[-n_lines:]

    # constructs DF with one line per command
    last_cmds = [ l[0].replace('\\','') for l in last_list ]
    # TODO: the time seems to be wrong still
    last_dt = [ dt_conv(l) for l in last_list]
    df = pd.DataFrame([last_cmds,last_dt]).T
    df.columns = ['Command', 'Time']

    return df

def hist_show(line: str):
    # TODO: some weird number shows up? Why?
    history = hist_tail()
    return history.loc[8].Command