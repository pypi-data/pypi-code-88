from abc import ABC

from lgt.common.python.slack_client.web_client import SlackWebClient
from lgt_data.mongo_repository import BotMongoRepository
from pydantic import BaseModel

from ..basejobs import BaseBackgroundJob, BaseBackgroundJobData

"""
Update bots statistics
"""
class BotStatsUpdateJobData(BaseBackgroundJobData, BaseModel):
    bot_name: str

class BotStatsUpdateJob(BaseBackgroundJob, ABC):
    @property
    def job_data_type(self) -> type:
        return BotStatsUpdateJobData

    def exec(self, data: BotStatsUpdateJobData):
        bots_rep = BotMongoRepository()
        bot = bots_rep.get_by_id(data.bot_name)

        client = SlackWebClient(bot.token, bot.cookies)
        channels = client.channels_list()['channels']
        bot.connected_channels = sum(1 for channel in channels if channel['is_member'])
        bot.channels = len(channels)
        bots_rep.add_or_update(bot)