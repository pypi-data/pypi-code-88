class UrlParser:
    def __init__(self, command: str, args_dict: dict) -> None:
        self.api_url = "https://coh2-api.reliclink.com/community/leaderboard/"
        self.command = command
        self.args = self.parse_args(args_dict)

        self.repr = f"{self.api_url}{self.command}?{self.args}"

    def parse_args(self, args_dict):
        args_dict["title"] = "coh2"
        arg_str = "&".join([f"{key}={value}" for (key, value) in args_dict.items()])
        return arg_str

    def __repr__(self) -> str:
        return self.repr