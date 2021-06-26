"""
MIT License

Copyright (c) 2021 Keef

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import requests
import random
from .enums import Enum
from .errors import *
BASE_URL_SEARCH = "https://g.tenor.com/v1/search"
BASE_URL_TRENDING = "https://g.tenor.com/v1/trending"
BASE_URL_RANDOM =  "https://g.tenor.com/v1/random"
BASE_URL_GIF = "https://g.tenor.com/v1/gifs?"
HEADERS = {'content-type': 'application/json'} 
API_KEY = "2SEYM2O49WBY"

class Tapi:
    """[Tenor api wrapper used to request gif's from the website]
        This was original made to be used with discord.py bot development
        Why? , Cause i felt like it
    """

    def __get_url_from_response(
        self , 
        response: dict , 
        limit: int , 
        mediafilter: str
    ) -> tuple[str]: 
        if response.get("code") == 5: 
            raise DoesNotExist("THE GIF ID OR NAME COULD NOT BE FOUND")

        __tenor_urls = [] 
        for index in range(limit): 
            url = response['results'][index]['media'][0][mediafilter]['url']
            __tenor_urls.append(url)

        return tuple(__tenor_urls)

    def tenor_search_request(
        self , *,
        query: str ,
        limit: int = 5 , 
        contentfilter: Enum = Enum.ContentFilter.OFF , 
        mediafilter: Enum = Enum.MediaFilter.GIF, 
        pos: int = 0 , 
        locale: Enum = Enum.LocaleMedia.EN_US
    ) -> tuple[str]:
        """[Request gif's from the tenor website starting from most popular gif's to least]

        Args:
            query (str): [The tag to be used to find the gif]
            limit (int, optional): [The amount of gif's that will be returned from tenor]. Defaults to 5.
            contentfilter (Enum, optional): [The gif format the gif's will be returned in]. Defaults to Enum.ContentFilter.OFF.
            mediafilter (Enum, optional): [The content safety of the gif]. Defaults to Enum.MediaFilter.GIF.
            pos (int, optional): [The position you want to start collection gif's from]. Defaults to 0.
            locale (Enum, optional): [The default language to interpret search string]. Defaults to Enum.LocaleMedia.EN_US.

        Returns:
            tuple[str]: [GIF URLS]
        """
        data = requests.get(
            url = "%s?q=%s&limit=%s&contentfilter=%s&mediafilter=%s&pos=%s&locale=%s&key=%s"
            % 
            (BASE_URL_SEARCH , query , limit , contentfilter , mediafilter , pos , locale , API_KEY) , 

            headers = HEADERS
        ).json()

        return self.__get_url_from_response(data , limit , mediafilter)

    def tenor_trending_request(
        self , *,
        limit: int = 5 , 
        contentfilter: Enum = Enum.ContentFilter.OFF , 
        mediafilter: Enum = Enum.MediaFilter.GIF, 
        locale: Enum = Enum.LocaleMedia.EN_US
    ) -> tuple[str]:
        """[Request trending gif's from the tenor website]

        Args:
            limit (int, optional): [The amount of gif's that will be returned from tenor]. Defaults to 5.
            contentfilter (Enum, optional): [The gif format the gif's will be returned in]. Defaults to Enum.ContentFilter.OFF.
            mediafilter (Enum, optional): [The content safety of the gif]. Defaults to Enum.MediaFilter.GIF.
            locale (Enum, optional): [The default language to interpret search string]. Defaults to Enum.LocaleMedia.EN_US

        Returns:
            tuple[str]: [GIF URLS]
        """
        data = requests.get(
            url = "%s?limit=%s&contentfilter=%s&mediafilter=%s&locale=%s&key=%s"
            % 
            (BASE_URL_TRENDING , limit , contentfilter , mediafilter , locale , API_KEY) , 

            headers = HEADERS
        ).json()

        return self.__get_url_from_response(data , limit , mediafilter)

    def custom_random_request(
        self , *,
        query: str ,
        limit: int = 5 , 
        pos: int = 5 ,
        contentfilter: Enum = Enum.ContentFilter.OFF , 
        mediafilter: Enum = Enum.MediaFilter.GIF, 
        locale: Enum = Enum.LocaleMedia.EN_US
    ) -> tuple[str]:
        """[Request random gif's from the tenor website with each call , When i say random i mean random]

        Args:
            query (str): [The tag to be used to find the gif]
            limit (int, optional): [The amount of gif's that will be returned from tenor]. Defaults to 5.
            contentfilter (Enum, optional): [The gif format the gif's will be returned in]. Defaults to Enum.ContentFilter.OFF.
            mediafilter (Enum, optional): [The content safety of the gif]. Defaults to Enum.MediaFilter.GIF.
            pos (int, optional): [The position you want to start collection gif's from]. Defaults to 0.
            locale (Enum, optional): [The default language to interpret search string]. Defaults to Enum.LocaleMedia.EN_US.

        Returns:
            tuple[str]: [GIF URLS]
        """
        pos = str(random.randint(0 , pos))
        data = requests.get(
            url = "%s?q=%s&limit=%s&contentfilter=%s&mediafilter=%s&pos=%s&locale=%s&key=%s"
            % 
            (BASE_URL_RANDOM , query , limit , contentfilter , mediafilter , pos , locale , API_KEY) , 

            headers = HEADERS
        ).json()

        return self.__get_url_from_response(data , limit , mediafilter)


    def tenor_random_request(
        self , *,
        query: str ,
        limit: int = 5 , 
        pos: int = 0 ,
        contentfilter: Enum = Enum.ContentFilter.OFF , 
        mediafilter: Enum = Enum.MediaFilter.GIF, 
        locale: Enum = Enum.LocaleMedia.EN_US
    ) -> tuple[str]:
        """[Request random gif's from the tenor , Would use tenor_gif_search]

        Args:
            query (str): [The tag to be used to find the gif]
            limit (int, optional): [The amount of gif's that will be returned from tenor]. Defaults to 5.
            contentfilter (Enum, optional): [The gif format the gif's will be returned in]. Defaults to Enum.ContentFilter.OFF.
            mediafilter (Enum, optional): [The content safety of the gif]. Defaults to Enum.MediaFilter.GIF.
            pos (int, optional): [The position you want to start collection gif's from]. Defaults to 0.
            locale (Enum, optional): [The default language to interpret search string]. Defaults to Enum.LocaleMedia.EN_US.

        Returns:
            tuple[str]: [GIF URLS]
        """
        data = requests.get(
            url = "%s?q=%s&limit=%s&contentfilter=%s&mediafilter=%s&pos=%s&locale=%s&key=%s"
            % 
            (BASE_URL_RANDOM , query , limit , contentfilter , mediafilter , pos , locale , API_KEY) , 

            headers = HEADERS
        ).json()

        return self.__get_url_from_response(data , limit , mediafilter)

    def tenor_gif_request(
        self , *,
        ids: int ,
        limit: int = 5 , 
        mediafilter: Enum = Enum.MediaFilter.GIF, 
    ) -> tuple[str]:
        """[Request a specific gif from the tenor website]

        Args:
            ids (int): [The gif id]
            limit (int, optional): [The amount of gif's that will be returned from tenor]. Defaults to 5.
            mediafilter (Enum, optional): [The content safety of the gif]. Defaults to Enum.MediaFilter.GIF.

        Returns:
            tuple[str]: [GIF URLS]
        """
        data = requests.get(
            url = "%s?ids=%s&limit=%s&mediafilter=%s&key=%s"
            % 
            (BASE_URL_GIF , ids , limit ,  mediafilter , API_KEY) , 

            headers = HEADERS
        ).json()
        return self.__get_url_from_response(data , limit , mediafilter)