class self_messages():
    """Fix for discord self bots."""
    def __init__(self, token: str):
        """token: str - You need to put your token here, or else the script cannot access the API"""
        import requests

        self.token = token
        self.requests = requests

    def history(self, channel_id: int, limit: int=50):
        """
        Returns a list of json dicts

        channel_id: int - aquired with "message.channel.id"
        message_id: int - aquired with "message.id"
        limit: int - amount of messages to return
        """

        url = f"https://discord.com/api/v9/channels/{str(channel_id)}/messages?limit="+str(limit)
        headers = {
            'accept': '*/*',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9002 Chrome/83.0.4103.122 Electron/9.3.5 Safari/537.36',
            'authorization': self.token
        }
        data = self.requests.get(url, headers=headers)
        print("[debug] "+str(data.status_code))
        data = data.json()
        messages = []
        for item in data:
            messages.append(item)
        return messages

    def content(self, channel_id: int, message_id: int, limit: int=15):
        """
        Return the content of a message from discord, assuming your account has access to the channel.

        channel_id: int - aquired with "message.channel.id"
        message_id: int - aquired with "message.id"
        limit: int - how many messages back to search for the original message (max 100 i think).
        """
        url = f"https://discord.com/api/v9/channels/{str(channel_id)}/messages?limit="+str(limit)
        headers = {
            'accept': '*/*',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9002 Chrome/83.0.4103.122 Electron/9.3.5 Safari/537.36',
            'authorization': self.token
        }
        data = self.requests.get(url, headers=headers)
        print("[debug] "+str(data.status_code))
        data = data.json()
        for item in data:
            if item['id'] == str(message_id):
                return item['content']
        return None