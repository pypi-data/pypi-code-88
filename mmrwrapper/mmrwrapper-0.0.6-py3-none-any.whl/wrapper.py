import aiohttp
from datetime import datetime
from functools import wraps

import exceptions as err

class MyMMR:

    BASE_URL = "https://{region}.whatismymmr.com/api/v1/"
    REGIONS = ["na", "euw", "eune", "kr"]

    def __init__(self, region, headers):

        if region not in self.REGIONS:
            raise err.InvalidRegionError
            
        self._region = region

        self._headers = headers


    def exceptions(func):
        """
        Decorator translating status code into exceptions
        """
        @wraps(func)
        async def _exceptions(*args, **params):
            
            response = await func(*args, **params)

            if "error" not in response:
                return response

            if response['error']['code'] == 0:
                raise err.InteralServerError

            if response['error']['code'] == 1:
                raise err.DatabaseError

            if response['error']['code'] == 100:
                raise err.SummonerNotFoundError

            if response['error']['code'] == 101:
                raise err.NoRecentMMRError

            if response['error']['code'] == 200:
                raise err.MissingQueryError

            if response['error']['code'] == 9001:
                raise err.RateLimitError



        return _exceptions
        

    @exceptions
    async def getPlayerStats(self, summoner):
        
        return await self.fetch((self.BASE_URL + "summoner?name={summoner}").format(region=self._region, summoner=summoner))

    @exceptions
    async def getDistribution(self):

        return await self.fetch((self.BASE_URL + "distribution").format(region=self._region))


    async def getNormalStats(self, summoner):
        
        data = await self.getPlayerStats(summoner)

        return data["normal"]


    async def getRankedStats(self, summoner):
        
        data = await self.getPlayerStats(summoner)

        return data["ranked"]

    async def getAramStats(self, summoner):
        
        data = await self.getPlayerStats(summoner)

        return data["ARAM"]

    async def getNormalMMR(self, summoner):

        data = await self.getPlayerStats(summoner)

        if data["normal"]["avg"] is None:
            return f"There is currently no Data available for {summoner}"

        if data["normal"]["err"] is None:
            return f"{summoner}'s MMR is {data['normal']['avg']}" + f" - last Updated: {datetime.fromtimestamp(int(data['normal']['timestamp']))}" if data["normal"]["timestamp"] is not None else ""
        
        return f"{summoner}'s MMR is between {int(data['normal']['avg']) - int(data['normal']['err'])} and {int(data['normal']['avg']) + int(data['normal']['err'])} [{data['normal']['avg']}]" + f" - last Updated: {datetime.fromtimestamp(int(data['normal']['timestamp']))}" if data["normal"]["timestamp"] is not None else ""


    async def fetch(self, url):
        """
        Returns the result of the request of the url given in parameter
        """
        
        async with aiohttp.ClientSession() as session:

            try:
                response = await session.request("GET", url, headers=self._headers)
            except Exception as e:
                return None
        
        return await response.json()
