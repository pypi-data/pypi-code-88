r"""Identify piecewise trace of a tset.

refer also to myapps\00-working-dir\00_misc_to_do\sklearn-tfidf-chinese-text\gen_cmat.py
"""
from typing import List, Union

import numpy as np
from sklearn.cluster import OPTICS
from scipy.stats import linregress

# import cytoolz as tlz
from functional import seq


def check_valid(elm, slope=0.9, rvalue=0.9, stderr=0.21):
    """Check validity of elm.

    Args
        elm: tset
        slope: lower bound
        rvaue: lower bound
        stderr: upper bound
    """
    linreg = linregress(np.array(elm)[:, 0], np.array(elm)[:, 1])
    if linreg.slope >= slope and linreg.rvalue >= rvalue and linreg.stderr <= stderr:
        return True

    return False


# fmt: off
def lrtrace_tset(
        tset_: Union[List[float], np.ndarray],
        min_samples: int = 2,
        min_cluster_size: int = 5,
) -> np.ndarray:
    # fmt: on
    """Id piecewise trace of a tset via linear regression/OPTICS.

    Args:
        tset: nx2 or nx3 triple set
        min_samples: OPTICS param
        min_cluster_size: OPTICS param

    Returns:
        aling trace based piecewise linear regression

    import toolz as tlz  # cytoolz

    len_ = len(set(labels_)) - 1
    vlist = [tset_[labels_ == elm] for elm in range(len_)]
    # vlist0 = [elm.tolist() for elm in vlist]
    # or vlist1 = [*map(lambda x: x.tolist(), vlist)]

    v0 = [*tlz.filter(check_valid, vlist)]
    tr0 = [elm.tolist() for elm in  tlz.concat(v0)]

    # v00 = [*tlz.filter(check_valid, vlist0)]
    # assert  [elm.tolist() for elm in v0] == v00

    # vset00 = [*tlz.concat(v00)]
    # assert [*tlz.concat(v00)] == [elm.tolist() for elm in  tlz.concat(v0)]

    # assert np.all(np.array(vset00) == np.array(vset))

    """
    tset_ = np.array(tset_)

    labels_ = OPTICS(min_samples=min_samples, min_cluster_size=min_cluster_size).fit(tset_).labels_

    # valid_set = tlz.concat(elm for elm in tset_[labels_ > -1] if check_valid(elm))

    len_ = len(set(labels_)) - 1
    valid_set = seq([tset_[labels_ == elm] for elm in range(len_)]).filter(check_valid)

    vset = valid_set.reduce(lambda x, y: np.concatenate((x, y))).to_list()

    # to_panas()
    # fig = plt.figure()
    # ax = fig.add_subplot(111)
    # sns.scatterplot(x=1, y=0, data=df, ax=ax)
    # ax.set_xlable set_ylabel set_title

    # plot_tset(vset)

    return np.array(vset)


def main():
    """Main."""
    import os
    from pathlib import Path
    import joblib

    print(f"__file__: {__file__}, parent {Path(__file__).resolve().parent} cwd: {os.getcwd()}")
    tset00 = joblib.load("data/tset.lzma")
    print(lrtrace_tset(tset00).__len__(), )

if __name__ == "__main__":
    main()
