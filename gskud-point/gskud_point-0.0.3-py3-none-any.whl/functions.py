import datetime


def update_last_state(last_states: dict, state: str, timestamp=datetime.datetime.now(), *args, **kwargs):
    last_states[state] = timestamp

