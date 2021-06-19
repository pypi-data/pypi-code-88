import aiohttp

class disbotlist():
  def __init__(self,client,token):
    self.client = client
    self.token = token
  
  async def serverCountPost(self):
    async with aiohttp.ClientSession() as session:
        res = await session.post(url="https://disbots.xyz/api/bots/stats",headers={'serverCount': str(len(self.client.guilds)),'Content-Type': 'application/json', 'Authorization': str(self.token)})
        return await res.json()
  
  async def hasVoted(self,id):
    async with aiohttp.ClientSession(headers={"Authorization": self.token}) as session:
      async with session.get(f"https://disbots.xyz/api/bots/check/{id}") as res:
        return await res.json()
  
  async def search(self,id):
    async with aiohttp.ClientSession() as session:
        async with session.get(f"https://disbots.xyz/api/bots/{id}") as res:
          return await res.json()
