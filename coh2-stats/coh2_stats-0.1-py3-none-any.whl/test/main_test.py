#from coh2_stats import query
import unittest

class TestInc(unittest.TestCase):
    def test_leaderboard(self):
        # arrange
        leaderboard_id = 16
        start = 1
        count = 50
        query = Query()
        # act
        query_url = query.get_leaderboard(16, 1, 50)
        url = f"getLeaderBoard2?leaderboard_id={leaderboard_id}&start={start}&count={count}&title=coh2"
        # assert
        self.assertEqual(url, query_url)

    def test_leaderboard2(self):
        # arrange
        leaderboard_id = 16
        start = 2
        count = 50
        query = Query()
        # act
        query_url = query.get_leaderboard(16, 1, 50)
        url = f"getLeaderBoard2?leaderboard_id={leaderboard_id}&start={start}&count={count}&title=coh2"
        # assert
        self.assertEqual(url, query_url)

class Query:
    def get_leaderboard(self, leaderboard_id, start, count):
        return "getLeaderBoard2?leaderboard_id=16&start=1&count=50&title=coh2"


if __name__ == "__main__":
    unittest.main()