from abc import ABC
from typing import Optional, List

from cachetools import cached, TTLCache
from lgt_data.mongo_repository import UserBotCredentialsMongoRepository, UserMongoRepository, DedicatedBotRepository
from pydantic import BaseModel

from ..basejobs import BaseBackgroundJobData, BaseBackgroundJob

"""
User limits handling
"""
class UpdateUserDataUsageJobData(BaseBackgroundJobData, BaseModel):
    bot_name: Optional[str]
    dedicated_bot_id: Optional[str]
    filtered: bool

class UpdateUserDataUsageJob(BaseBackgroundJob, ABC):
    @cached(cache=TTLCache(maxsize=500, ttl=600))
    def get_user_ids(self, workspace) -> List[str]:
        bots = UserBotCredentialsMongoRepository().get_active_bots(workspace)
        return list(set([str(bot.user_id) for bot in bots]))

    @property
    def job_data_type(self) -> type:
        return UpdateUserDataUsageJobData

    @staticmethod
    def increment(user_id: str, filtered: bool):
        if filtered:
            UserMongoRepository().inc(user_id, leads_filtered=1, leads_proceeded=1)
            return

        UserMongoRepository().inc(user_id, leads_proceeded=1)

    def exec(self, data: UpdateUserDataUsageJobData):
        if data.dedicated_bot_id:
           bot = DedicatedBotRepository().get_by_id(data.dedicated_bot_id)
           self.increment(bot.user_id, data.filtered)
           return

        user_ids = self.get_user_ids(data.bot_name)
        for user_id in user_ids:
            self.increment(user_id, data.filtered)
