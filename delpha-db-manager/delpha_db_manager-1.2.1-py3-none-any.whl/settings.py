#database configuration settings

constants = dict(
    DELPHA_KEYSPACES = ["delpha_actions_dev", "delpha_actions", "delpha_behavior_dev", "delpha_behavior", "delpha_analytics", "delpha_analytics_dev", "delpha_use_case"],
)

#application predefined constants

app = dict(
    VERSION   = 1.0,
    GITHUB    = "https://github.com/Delpha-Assistant/DelphaDBManagement"
)

def set_mode(mode):
    global constants
    if mode == 'dev':
        constants['DELPHA_KEYSPACES'] = list(filter(lambda m: 'dev' in m or 'use_case' in m, constants['DELPHA_KEYSPACES']))
    else:
        constants['DELPHA_KEYSPACES'] = list(filter(lambda m: 'dev' not in m, constants['DELPHA_KEYSPACES']))

def get_keyspace(k_type):
    try:
        return list(filter(lambda m: k_type in m, constants['DELPHA_KEYSPACES']))[0]
    except:
        return ''