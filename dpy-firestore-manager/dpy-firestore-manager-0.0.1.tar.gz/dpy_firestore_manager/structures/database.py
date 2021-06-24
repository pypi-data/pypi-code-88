from firebase_admin import firestore

class Database:

  """
  Database structure

  Attributes:
    db (Firestore.client): access Firestore
  """

  def __init__(self):

    self.db = firestore.client()