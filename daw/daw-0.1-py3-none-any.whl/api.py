import requests
from .errors import *


class DAW:

    def __init__(self, token, bot_token=None):
        """
        Intialize the wrapper
        """
        
        self.token = token
        self.bot_token = bot_token

    ### USER DATA ###

    def get_current_user_data(self):
        """
        Gets current user data\n
        Identify scope required (email scope is optional)
        """
        request = requests.get(f"https://discord.com/api/v9/users/@me/", headers={"Authorization": f"Bearer {self.token}"})
        if request.status_code == 200:
            response = request.json()
            return response
        else:
            raise APIError(f"Something failed. Server response: {request.status_code}")

    def get_user_data(self, user_id):
        """
        Gets user data 
        Note: Bot token required
        """
        if self.bot_token == None:
            raise APIError("This function needs a bot token, please check the documentation! https://daw.readthedocs.io/")
        request = requests.get(f"https://discord.com/api/v9/users/{user_id}/", headers={"Authorization": f"Bot {self.bot_token}"})
        if request.status_code == 200:
            response = request.json()
            return response
        else:
            raise APIError(f"Something failed. Server response: {request.status_code}")


    def get_user_guilds(self):
        """
        Gets user guilds
        Guilds scope required
        """
        request = requests.get(f"https://discord.com/api/v9/@me/guilds", headers={"Authorization": f"Bearer {self.token}"})
        if request.status_code == 200:
            response = request.json()
            return response
        else:
            raise APIError(f"Something failed. Server response: {request.status_code}")
        

    def get_user_connections(self):
        """
        Gets user guilds
        Connections scope required
        """
        request = requests.get(f"https://discord.com/api/v9/@me/connections", headers={"Authorization": f"Bearer {self.token}"})
        if request.status_code == 200:
            response = request.json()
            return response
        else:
            raise APIError(f"Something failed. Server response: {request.status_code}")
        
        

    



        
