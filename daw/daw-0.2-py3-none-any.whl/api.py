from .query import *


class DAW:

    def __init__(self, token, bot_token=None):
        """
        Intialize the wrapper
        """
        
        self._token = token
        self._bot_token = bot_token

    ### USER DATA ###

    def get_current_user_data(self):
        """
        Gets current user data\n
        Identify scope required
        """
        api_user_auth(url="https://discord.com/api/v9/users/@me", token=self._token)

    def get_user_data(self, user_id):
        """
        Gets user data 
        Note: Bot token required
        """
        api_bot_auth(url=f"https://discord.com/api/v9/users/{user_id}", token=self._bot_token)


    def get_current_user_guilds(self):
        """
        Gets user guilds
        Guilds scope required
        """
        api_user_auth(url="https://discord.com/api/v9/users/@me/guilds", token=self._token)
        

    def get_current_user_connections(self):
        """
        Gets user connections
        Connections scope required
        """
        api_user_auth(url="https://discord.com/api/v9/users/@me/connections", token=self._token)
        
    ### GUILDS ###

    def get_guild_data(self, guild_id):
        """
        Gets user data 
        Note: Bot token required
        """
        api_bot_auth(url=f"https://discord.com/api/v9/guilds/{guild_id}", token=self._bot_token)