from dpy_firestore_manager.structures import Document
from dpy_firestore_manager.utilities import assign
from .members_manager import MembersManager

class GuildManager(Document):

  """
  Manages a specific guild doc of the guilds collection
    
  Path: db/guilds/{guild_id}

  Args:
    data (dict): field values of doc
    data.id (str): id of guild doc 
  """

  def __init__(self, data):

    super().__init__(f'guilds/{data["id"]}')
    assign(self, data)

    self.members = MembersManager(self.id)


  async def create(self, guild):

    """
    Creates doc containing basic information

    Args:
      guild (discord.Guild): guild to create
    """

    await self.update({"id": guild.id, "name": guild.name})


  async def update(self, data):

    """
    Updates doc

    Args:
      data (dict): field values to update
    """

    docRef = await self.reference()
    docRef.set(data, merge=True)