from .guilds_manager import GuildsManager

class DatabaseManager:

  """
  Manages database
    
  Path: db

  Attributes:
    guild (GuildsManager): manages guild docs
  """

  def __init__(self):

    self.guilds = GuildsManager()