from adapt import calcmags


def test_simple():
    """ Simply check all is up and running """
    mlv, mlh = calcmags.main()
    if "%4.2f" % mlv != "0.40":
        raise ValueError("MLv doesn't match: %r" % mlv)
    if "%4.2f" % mlh != "0.22":
        raise ValueError("MLv doesn't match: %r" % mlh)
