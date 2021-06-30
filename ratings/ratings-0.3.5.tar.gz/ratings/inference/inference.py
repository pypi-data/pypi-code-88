from ratings.lattice.lattice_bayes import std_posterior_dividend
from winning.lattice_conventions import STD_UNIT, STD_L, NAN_DIVIDEND
from winning.std_calibration import std_dividend_implied_ability
from ratings.inference.utils import center
import pandas as pd
import numpy as np
import math
from pprint import pprint


# Inference of an (ephemeral) "true" prior probability is performed on a collection of contest results

INFERENTIAL_COLUMNS = ['contest_id', 'contestant_id', 'won', 'performance', 'market_dividend']


def assert_inferential_columns(df):
    for col in INFERENTIAL_COLUMNS:
        assert col in df.columns


def add_posterior_dividend(df, ability_std:float, idio_std:float, nan_value=NAN_DIVIDEND, unit:float=STD_UNIT, L=STD_L, check_inversion=False, col='posterior_dividend'):
    """
    :param df:                     dataframe holding contest results and also market prices for contests
    :param ability_std:            assumed standard deviation of true ability from market implied relative ability (i.e. market's uncertainty)
    :param idio_std:               assumed standard deviation of performance "on the day"
    :param nan_value:              decimal price to use where market_dividend is np.nan
    :param unit:                   lattice width
    :param L:                      lattice length is 2L*1
    :param check_inversion:        if flag is set, the inversion of ability will be checked each time for numerical accuracy
    :param col:                    name of new column to store posterior dividend
    :return: pd.DataFrame with one additional column
    """
    assert_inferential_columns(df)
    # Pandas dataframe must contain:
    #
    #   - contest_id of some sort assumed to be monotonic in time.
    #   -"dividend" refers to inverse of state price, which is almost identical to winning probability
    #   -"won" is boolean or numeric indicator that contestant won the contest
    #   -"market_dividend" is the price (inverse probability) assigned by the 'market'

    def _add_posterior_dividend(df_contest, ability_std, performance_std, nan_value, unit, L, check_inversion, col):
        assert_inferential_columns(df_contest)
        dividends = df_contest['market_dividend'].values
        performances = center( df_contest['performance'].values )
        df_contest[col] = std_posterior_dividend(dividends=dividends, ability_std=ability_std, idio_std=performance_std, observations=performances,
                                                 nan_value=nan_value, unit=unit, L=L, check_inversion=check_inversion)
        return df_contest

    return df.groupby('contest_id').apply(_add_posterior_dividend, ability_std=ability_std,
                                          performance_std=idio_std,
                                          nan_value=nan_value, unit=unit, L=L, check_inversion=check_inversion, col=col)


def add_relative_performance_std(df):

    def _add_relative_performance_std(df_contest):
        performances = center(df_contest['performance'].values)
        df_contest['relative_performance_std'] = np.nanstd(performances)
        return df_contest 

    assert_inferential_columns(df)
    return df.groupby('contest_id').apply(_add_relative_performance_std)


def add_implied_relative_ability_std(df):
    
    def _add_implied_relative_ability_std(df_contest):
        abilities = center(df_contest['implied_relative_ability'].values)
        df_contest['implied_relative_ability_std'] = np.nanstd(abilities)
        return df_contest 

    assert_inferential_columns(df)
    return df.groupby('contest_id').apply(_add_implied_relative_ability_std)


def add_implied_relative_ability(df, idio_std, nan_value=NAN_DIVIDEND, unit:float=STD_UNIT, L=STD_L):
    """  Solves the market inversion problem race by race, to compute centered relative abilities.
    :param df: 
    :param idio_std:         standard deviation in performance on the day
    :param nan_value:        decimal price to use where market_dividend is np.nan
    :param unit:             lattice width
    :param L:                lattice length is 2L*1\
    :return: 
    """
    assert_inferential_columns(df)
    
    def _add_implied_relative_ability(df_race):
        dividends = df_race['market_dividend']
        df_race['implied_relative_ability'] = center(std_dividend_implied_ability(dividends=dividends, nan_value=nan_value, L=L, unit=unit, scale=idio_std))
        return df_race
    
    return df.groupby('contest_id').apply(_add_implied_relative_ability)


def truncate(df,n_performances):
    """ Truncate data but don't chop a contest in half """
    included_ids = list(set(df['contest_id'].values[:n_performances]))
    return df[df['contest_id'].isin(included_ids)]


def calibrate(df, performance_fraction_guess=0.8, loop:bool = False, show_progress=False):
    """ Calibrate the standard deviations for
         1. idiosyncratic performance variation and
         2. ability diversity in a race as implied by the market

    :param df:  contest results
    :param loop:                          If set, will iterate even though this should not be necessary
    :param performance_fraction_guess     Initial guess for
    :returns four standard deviations:
            idio_std            ... idiosyncratic performance deviation "on the day"
            ability_std         ... typical deviation in ability in a race
            performance_std     ... total deviation due to both of the above
            empirical_std       ... total deviation that we actually observe in the data set, for comparison
    :side effects:
            Adds or updates 'relative_performance_std'
                            'implied_relative_ability_std'
                            'implied_relative_ability'

    The task of calibration is to marry the last two numbers, assuming independence of the first two
    """
    assert_inferential_columns(df)
    df = add_relative_performance_std(df)  # Empirical std of relative performance
    empirical_relative_performance_std = np.nanmean(df['relative_performance_std'].values)
    implied_ratio = 10.
    assumed_idio_std = performance_fraction_guess * empirical_relative_performance_std

    countdown = 3 if loop else 0
    while abs(implied_ratio-1.0)>0.1 and countdown>=0:
        df = add_implied_relative_ability(df, idio_std=assumed_idio_std)
        df = add_implied_relative_ability_std(df)
        implied_ability_var = np.nanmean( df['implied_relative_ability_std'].pow(2) )
        implied_ability_std = math.sqrt(implied_ability_var)
        assumed_idio_var = assumed_idio_std**2
        implied_relative_performance_std = math.sqrt( implied_ability_var + assumed_idio_var )
        implied_ratio = implied_relative_performance_std / empirical_relative_performance_std
        if show_progress:
            pprint({'assumed_idio_std':assumed_idio_std,
                    'assumed_idio_std_next_guess':assumed_idio_std / implied_ratio,
                    'implied_ability_std':implied_ability_std,
                    'implied_relative_performance_std':implied_relative_performance_std,
                    'empirical_relative_performance_std':empirical_relative_performance_std,
                    'implied_ratio':implied_ratio})
        assumed_idio_std = assumed_idio_std / implied_ratio
        countdown -= 1

    # Infer what the last iteration would do...everything is linear modulo possible lattice effects
    ability_std = implied_ability_std / implied_ratio
    performance_std = math.sqrt( ability_std**2 + assumed_idio_std**2 )
    df['implied_relative_ability'] = df['implied_relative_ability'] / implied_ratio
    df['implied_relative_ability_std'] = df['implied_relative_ability_std'] / implied_ratio
    df['relative_performance_std'] = df['relative_performance_std'] / implied_ratio
    return df, assumed_idio_std, ability_std, performance_std, empirical_relative_performance_std


if __name__=='__main__':
    # See also "scripts/prepare_synthetic_training_testing"
    from ratings.hereiam import TRAIN_CSV, TRAINING_CSV
    df = pd.read_csv(TRAIN_CSV)
    calib_df = truncate(df, n_performances=100)
    calib_df, idio_std, ability_std, performance_std, empirical_std = calibrate(calib_df, loop=False)
    pprint({"idio":idio_std,'ability':ability_std,'performance':performance_std,'empirical':empirical_std})
    print('  calibration done')
    calif_df = add_posterior_dividend(calib_df, ability_std = ability_std, idio_std=idio_std)
    print('  posterior dividends added')
    print(df)
