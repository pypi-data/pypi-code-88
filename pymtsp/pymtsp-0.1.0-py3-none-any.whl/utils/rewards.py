def default_reward_func(env):
    # make span reward
    reward = 0 if not env.done else env.manager.time
    return reward
