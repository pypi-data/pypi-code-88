from dpy_firestore_manager.structures import Collection
from .member_manager import MemberManager

class MembersManager(Collection):

  """
  Manages the member docs of a specific guild members collection
    
  Path: db/guilds/{guild_id}/members

  Args:
    guild_id (str): guild id of members collection
  """

  def __init__(self, guild_id):
    
    super().__init__(f'guilds/{guild_id}/members')
    self.guild_id = guild_id


  async def get(self, id = None):

    """
    Gets field values of doc, gets all docs if no id is passed

    Args:
      id (str, optional): id of doc to get

    Returns:
      dict: field values of doc
    """

    doc = await self.data(id)
    return doc


  async def post(self, data):

    """
    Posts field values of doc

    Args:
      data (dict): field values to update
      data.id (str): id of doc to update

    Returns:
      dict: updated field values of doc
    """

    docRef = await self.reference(data.get("id"))
    docRef.set(data, merge=True)
    return data


  async def delete(self, id):

    """
    Deletes doc

    Args:
      id (str): id of doc to delete

    Returns:
      dict: field values of deleted doc
    """

    docRef = await self.reference(id)
    doc = await self.data(id)
    docRef.delete()
    return doc


  async def fetch(self, id):

    """
    Fetches doc, fetches a pseudo doc if doc does not exist

    Args:
      id (str): id of doc to fetch

    Returns:
      MemberManager: manages fetched member
    """

    doc = await self.data(id)
    if (doc is None):
      return MemberManager(self.guild_id, {"id": id})
    else:
      return MemberManager(self.guild_id, doc)
  