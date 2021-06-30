from ratings.inclusion import installed_stochastic, installed_matplotlib
if installed_stochastic:
    from stochastic.processes.diffusion.vasicek import VasicekProcess
import numpy as np
import pandas as pd
import random
from pprint import pprint
from random import randint
from ratings.hereiam import DATA
import os
from winning.std_calibration import std_ability_implied_dividends


GENERATIVE_MODEL_COLUMNS = ['day', 'contest_id', 'contestant_id', 'performance', 'true_ability','true_relative_ability', 'market_relative_ability','won', 'true_dividend', 'market_dividend']


# Synthetic contest data generation


def mock_data(n_contestants=100, n_days =1000, min_contest_size:int=6, max_contest_size:int=16,
              idio_std=3, field_std=2, market_std=0.5, show_progress=True):
    """ For each contest day, find all performances that are not nan and assign them
        to contests based loosely on the previous performance (so strong play strong etc)

    :param n_contestants                        total universe of contestants
    :param n_days                               a 'day' is just a quantized time when contests take place
    :param data:    [ [ ability on a day ] ]    taking the output of mock_ability
    :param min_contest_size, max_contest_size   controls contest size. e.g. set to 2 for chess
    :param idio_std                             variation in performance of contestant "on the day", relative to ability
    :param market_std                           error in market's ability to estimate true ability
    :param field_std                            variation in measured absolute performance for the field as a whole (slow pace etc)
    :return:
    """
    ability_data = mock_ability(n_contestants=n_contestants, n_days =n_days)

    sparse_data = list()
    most_recent_performance = dict()
    contest_ndx = 0
    for day_ndx, row in enumerate(ability_data):
        if show_progress:
            print('Generating day '+str(day_ndx)+' of '+str(len(ability_data)))
        candidates = list()
        # Create ability/performance tuples and sort by previous performance, if available
        for i,ability in enumerate(row):
            if not np.isnan(ability):
                performance = ability + np.random.randn() * idio_std
                prev_performance = most_recent_performance[i] if i in most_recent_performance else np.random.randn()
                randomized_prev_performance = prev_performance+np.random.randn()
                candidates.append( (randomized_prev_performance,(i,(ability,performance))))
        sorted_candidates = sorted(candidates)

        if any(sorted_candidates):
            # Split the row into separate contests that occur on the same day
            for contest in random_chunk(sorted_candidates, min_chunk=min_contest_size, max_chunk=max_contest_size):
                 field_performance = np.random.randn()*field_std  # Translate everyone's performance (e.g. slower or faster pace)
                 scores  = [ perf for _,(i,(ability,perf)) in contest ]
                 min_score = min(*scores)
                 won     = [ score<=min_score for score in scores ]
                 relative_abilities = [ ability for _,(i,(ability,perf)) in contest ]
                 mean_ability = np.mean(relative_abilities)
                 centered_relative_abilities = [ ra-mean_ability for ra in relative_abilities ]
                 true_dividends = std_ability_implied_dividends(ability=centered_relative_abilities, scale=idio_std)
                 noisy_relative_abilities = [ ra+np.random.randn()*market_std for ra in centered_relative_abilities ]
                 market_dividends = std_ability_implied_dividends(ability=noisy_relative_abilities, scale=idio_std)
                 race_abilities = [ a for _,(i,(a,_)) in contest ]
                 race_performances = [p for _,(i, (_, p)) in contest]
                 race_i = [i for _,(i, (a, _)) in contest]

                 for j, (i,a,p,w,td,cra,nra,md) in enumerate(zip(race_i,race_abilities,race_performances,won,true_dividends,centered_relative_abilities,noisy_relative_abilities,market_dividends)):
                     sparse_data.append( (day_ndx,contest_ndx, i,p+field_performance,a,cra,nra,w,td,md) )
                     most_recent_performance[i] = p+field_performance
                 contest_ndx+=1

    columns = GENERATIVE_MODEL_COLUMNS
    df = pd.DataFrame(columns=columns)
    for j, col in enumerate(columns):
        df[col] = [d[j] for d in sparse_data]

    return df


def mock_ability(n_contestants=100, n_days =1000):
    """ Creates a list of daily performances for all contestants, with most masked by np.nan
        Ability is a mean reverting random walk
    :return:
    """
    assert installed_stochastic, 'pip install stochastic'
    times = range(n_days+1)
    abilities = list()
    for horse_id in range(n_contestants):
        log_hazard_process = VasicekProcess(speed=0.1, mean=1, vol=0.1, t=1)
        hazard = 0.05*np.exp(0.5*log_hazard_process.sample_at(times=times))
        participation = np.random.rand(n_days)<hazard
        mean_ability = np.random.randn()
        speed = random.choice([0.1,0.05,0.025])
        vol = random.choice([0.07,0.01,1.13])
        ability_process = VasicekProcess(speed=speed, mean=mean_ability, vol=0.1, t=1)
        latent_ability = ability_process.sample_at(times)
        ability = [ a if participated else np.nan for a,participated in zip(latent_ability,participation)]
        abilities.append(ability)
    abilities_transposed = list(map(list, zip(*abilities)))
    return abilities_transposed


def canonical_ids(n_contestants):
    return ['c' + str(i) for i in range(n_contestants)]


def dense_performances_to_frame(data, contestant_ids=None):
    n_contestants = len(data[0])
    contestant_ids = canonical_ids(n_contestants) if (contestant_ids is not None) else contestant_ids
    return pd.DataFrame(columns=contestant_ids, data=data)


def random_chunk(li:list, min_chunk=4, max_chunk=8):
    """ Splits list into random sized chunks """
    chunks = list()
    remaining = [ it for it in li ]
    while len(remaining)>=min_chunk:
        if min_chunk<=len(remaining)<=max_chunk:
            n_chunk = len(remaining)
        else:
            n_chunk = randint(min_chunk,max_chunk)
        chunk = [ remaining.pop(0) for _ in range(n_chunk) ]
        chunks.append(chunk)
    return chunks


if __name__=='__main__':
    # See also scripts/prepare_synthetic_train_test
    import time
    st = time.time()
    df = mock_data(n_contestants=1000, n_days=1000)
    print(df)
    print(time.time()-st)
    print(len(df))

