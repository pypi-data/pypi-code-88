# pip install github3.py
import github3
import pandas as pd
import sys
import subprocess as sp

def init():
    git_config = sp.run(["git","config","-l"], capture_output=True).stdout
    split_config = git_config.decode().split("\n")
    git_dict = {s[0]:s[1] for s in [ s.split('=') for s in split_config[:-11] ]}

    gh_username = git_dict['user.email']
    gh_password = git_dict['user.token']

    return gh_username, gh_password

def find_forks(repo_url: str):
    gh_username, gh_password = init()

    user, repo = repo_url.split('/')[-2:]

    g = github3.login(gh_username, gh_password)
    r = g.repository(user, repo)
    total_list = list(r.forks(sort='commits', number=r.fork_count))
    data = [ (i,i.updated_at,
            i.pushed_at, i.updated_at == i.created_at) for i in total_list ]
    df = pd.DataFrame(data,columns=['name','updated_at','pushed_at','ever_changed'])

    # TODO: humanize dates/times
    # https://github.com/jmoiron/humanize
    df = df.sort_values('ever_changed')
    print(df.ever_changed.value_counts())
    return df


def find_contributors(repo_url: str):
    from .sshconf import SshConfig
    # gh_username, gh_password = init()

    user, repo = repo_url.split('/')[-2:]
    f = open('/Users/jakub/.gitconfig').read().splitlines()
    c = SshConfig(f)

    g = github3.login(gh_username, gh_password)
    r = g.repository(user, repo)