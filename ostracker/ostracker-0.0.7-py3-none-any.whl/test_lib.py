import ostracker


def test_update():
    before = ostracker.scores("zezima")
    ostracker.update("zezima")
    after = ostracker.scores("zezima")

    assert before["current_at"] < after["current_at"], "update() did not find hiscores"


def test_scores():
    scores = ostracker.scores("zezima")
    assert scores["hiscores"], "scores() did not find hiscores"
