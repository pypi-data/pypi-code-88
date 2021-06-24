from dpy_firestore_manager.structures import Collection
from .guild_manager import GuildManager

class GuildsManager(Collection):

  """
  Manages the guild docs of the guilds collection
    
  Path: db/guilds
  """
  
  def __init__(self):

    super().__init__('guilds')


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
      GuildManager: manages fetched guild
    """

    doc = await self.data(id)
    if (doc is None):
      return GuildManager({"id": id})
    else:
      return GuildManager(doc)