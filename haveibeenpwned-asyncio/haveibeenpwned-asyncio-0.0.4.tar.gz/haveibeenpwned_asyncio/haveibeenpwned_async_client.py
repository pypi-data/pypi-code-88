import asyncio
from hashlib import sha1
import os
from functools import lru_cache
from urllib.parse import quote_plus
from aiohttp_retry import RetryClient, ExponentialRetry
from haveibeenpwned_asyncio.constants import haveibeenpwned, hashing


class haveIbeenPwnedClient(object):
    def __init__(
        self, semaphore_max: int = 5,
            api_key: str = "",
            truncate_response: bool = True,
            retry_attempts=3
    ):
        self.semaphore_max = semaphore_max
        self.semaphore = asyncio.Semaphore(10)
        self.api_version = haveibeenpwned.API_VERSION.value
        self.base_url = f"{haveibeenpwned.BASE_URL.value}{self.api_version}"
        self.api_key = None if not api_key else api_key
        self.truncate_response: bool = truncate_response
        self.loop = asyncio.get_event_loop()
        self.retry_attempts = retry_attempts
        self.retry_options = ExponentialRetry(
            start_timeout=5,
            max_timeout=60,
            attempts=self.retry_attempts,
            statuses=[429]
        )

    def generate_url(self, endpoint, object):
        return f"{self.base_url}/{endpoint}/{quote_plus(object)}"

    async def prep_headers(self, header_obj: dict):
        if not self.api_key:
            header_obj.pop("hibp-api-key", None)
        else:
            header_obj["hibp-api-key"] = self.api_key
        return header_obj

    # async def handle_responses(self, responses, truncate_output=False):
    #     if not truncate_output:
    #
    #     else:
    #         return  responses

    async def aiohttp_client_get(self, url: str= "", obj: str = ""):

        await self.semaphore.acquire()
        url = url + f"?truncateResponse={self.truncate_response}"
        headers = await self.prep_headers(haveibeenpwned.HTTP_HEADER.value)

        try:
            async with RetryClient(raise_for_status=False, retry_options=self.retry_options) as client:
                async with client.get(url, headers=headers) as resp:
                    resp_tuple = obj, resp.status, await resp.text()
                    self.semaphore.release()
                    return resp_tuple
        except Exception as e:
            print(f"Error: {e}")
            return {"error": e}

        finally:
            self.semaphore.release()

    async def queue_all_requeusts(self, urls: list = []):
        asyncio_tasks = []
        for url in urls:
            asyncio_tasks.append(self.aiohttp_client_get(url=url[0], obj=url[1]))

        return asyncio_tasks

    async def gather_all_requests(self, asyncio_tasks: list = []):
        return await asyncio.gather(*asyncio_tasks)


class haveIbeenPwnedAccount(haveIbeenPwnedClient):
    def __init__(self, semaphore_max: int = 5, accounts: list = [], api_key: str = ""):
        self.semaphore_max = semaphore_max
        super().__init__(accounts, api_key)
        self.endpoint = haveibeenpwned.ACCOUNT_ENDPOINT.value
        self.accounts = accounts

    async def query_accounts(self):
        urls = []
        for account in self.accounts:
            urls.append(
                (self.generate_url(endpoint=self.endpoint, object=account), account)
            )
        responses = await self.gather_all_requests(
            await self.queue_all_requeusts(urls=urls)
        )
        return responses

    def query_accounts_sync(self):
        coroutine = self.query_accounts()
        return self.loop.run_until_complete(coroutine)

class haveIbeenPwnedPastes(haveIbeenPwnedAccount):
    def __init__(self, semaphore_max: int = 5, accounts: list = [], api_key: str = ""):
        super().__init__(accounts, api_key)
        self.api_key = api_key
        self.semaphore_max = semaphore_max
        self.endpoint = haveibeenpwned.PASTES_ENDPOINT.value
        self.accounts = accounts

        print(self.__dict__)

class haveIbeenPwnedPasswords(haveIbeenPwnedClient):
    def __init__(
        self, semaphore_max: int = 5, passwords: list = [], api_key: str = ""
    ):
        super().__init__(passwords, api_key)
        self.semaphore_max = semaphore_max
        self.endpoint = haveibeenpwned.PASSWORD_ENDPOINT.value
        self.passwords = passwords
        self.api_key = ""
        self.base_url = haveibeenpwned.PASSWORD_BASE_URL.value

    async def find_corresponding_hash(self, responses:list=[]):
        response_list = []
        for resp in responses:
            if resp[1] == 200:
                compare_hash = self.hibp_hash(self.generate_hash(resp[0]))
                response_list.append((resp[0], bool(True if compare_hash in resp[2] else False)))
            else:
                response_list.append(resp[0], False)
        return response_list

    @lru_cache
    def generate_hash(self, password):
        """
        Generates hash again for comparison

        LRU cache ensures that its only calculated the first time this is called

        uses lru_cache so only computed once
        """
        if isinstance(password, str):
            password = password.encode(hashing.ENCODING.value)
        return sha1(password).hexdigest()

    @lru_cache
    def hibp_hash(self, hash):
        """
        hibp returns hash without a prefix

        uses lru_cache so only computed once

        Also is uppercased
        Ex: 2DC183F740EE76F27B78EB39C8AD972A757
        """
        return hash[5:].upper()

    async def query_passwords(self):
        urls = []
        for password in self.passwords:
            hash = self.generate_hash(password)
            urls.append(
                (
                    self.generate_url(endpoint=self.endpoint, object=hash[:5]),
                    password,
                )
            )
        responses = await self.gather_all_requests(
            await self.queue_all_requeusts(urls=urls)
        )
        responses = await self.find_corresponding_hash(responses)
        return responses

    def query_passwords_sync(self):
        coroutine = self.query_passwords()
        return self.loop.run_until_complete(coroutine)

