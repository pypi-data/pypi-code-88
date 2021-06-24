from dpy_firestore_manager.structures import Document
from dpy_firestore_manager.utilities import assign

class MemberManager(Document):

  """
  Manages a specific member doc of the members collection
    
  Path: db/guilds/{guild_id}/members/{member_id}

  Args:
    data (dict): field values of doc
    data.id (str): id of member doc 
  """

  def __init__(self, guild_id, data):

    super().__init__(f'guilds/{guild_id}/members/{data["id"]}')
    assign(self, data)

    self.guild_id = guild_id
      

  async def create(self, member):

    """
    Creates doc containing basic information

    Args:
      member (discord.Member): member to create
    """

    await self.update({"id": member.id, "name": member.name})


  async def update(self, data):

    """
    Updates doc

    Args:
      data (dictionary): field values to update
    """

    docRef = await self.reference()
    docRef.set(data, merge=True)