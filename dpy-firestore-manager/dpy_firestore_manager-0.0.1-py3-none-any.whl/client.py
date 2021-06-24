import os
from dotenv import load_dotenv
import firebase_admin
from firebase_admin import credentials
from .managers import DatabaseManager

class Client:

  """
  Main class for interacting with your Firestore

  Attributes:
    db (DatabaseManager): manages database
  """

  def __init__(self):

    load_dotenv()
    cred = credentials.Certificate({
      "type": "service_account",
      "project_id": os.getenv('PROJECT_ID'),
      "private_key_id": os.getenv('PRIVATE_KEY_ID'),
      "private_key": os.getenv('PRIVATE_KEY'),
      "client_email": os.getenv('CLIENT_EMAIL'),
      "client_id": os.getenv('CLIENT_ID'),
      "auth_uri": "https://accounts.google.com/o/oauth2/auth",
      "token_uri": "https://oauth2.googleapis.com/token",
      "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
      "client_x509_cert_url": os.getenv('CLIENT_X509_CERT_URL')
    })
    firebase_admin.initialize_app(cred)

    self.db = DatabaseManager()


  async def get_prefix(self, bot, message):

    """
    Gets guild prefix

    Args:
      bot (discord.Client): client
      message (discord.Message): message

    Returns:
      str: guild-unique prefix 
    """

    id = message.guild.id
    guild = await self.db.guilds.fetch(id)
    self.guild = guild
    self.prefix = guild.prefix
    return self.prefix