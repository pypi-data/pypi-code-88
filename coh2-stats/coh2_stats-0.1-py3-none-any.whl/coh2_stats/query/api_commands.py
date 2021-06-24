from .url_parser import UrlParser

class UrlWithApiCommands:
    @classmethod
    def get_leaderboard(cls, leaderboard_id: int, start: int, count: int):
        command = "getLeaderBoard2"
        api_args = dict()
        api_args["leaderboard_id"] = leaderboard_id
        api_args["start"] = start
        api_args["count"] = count
        return str(UrlParser(command, api_args))

    @classmethod
    def get_recent_match_history(cls, profile_ids: list):
        command = "getRecentMatchHistory"
        api_args = dict()
        api_args["profile_ids"] = cls.format_profile_ids(profile_ids)
        return str(UrlParser(command, api_args))

    @classmethod
    def get_personal_stat(cls, profile_ids: list):
        command = "GetPersonalStat"
        api_args = dict()
        api_args["profile_ids"] = cls.format_profile_ids(profile_ids)
        return str(UrlParser(command, api_args))

    @classmethod
    def format_profile_ids(cls, profile_ids: list[int]):
        joined_str = ','.join([f"'{p_id}'" for p_id in profile_ids])
        coat_with_brackets = f'[{joined_str}]'
        return coat_with_brackets
