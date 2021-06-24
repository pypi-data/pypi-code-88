from .database import Database

class Collection(Database):

  """
  Collection structure

  Args:
    path (str): absolute path leading to the collection

  Attributes:
    path (str): absolute path leading to the collection
  """
  
  def __init__(self, path):

    super().__init__()
    self.path = path


  async def reference(self, id = None):

    """
    Gets doc reference, gets collection reference if no id is passed

    Args:
      id (str, optional): id of doc to get

    Returns:
      Firebase.docRef | Firebase.collectionRef: reference to doc
    """

    if (id is None):
      collectionRef = self.db.collection(f'{self.path}')
      return collectionRef
    else:
      docRef = self.db.document(f'{self.path}/{id}')
      return docRef


  async def data(self, id = None):

    """
    Gets doc field values, gets all doc from collection if no id is passed

    Args:
      id (str, optional): id of doc to get

    Returns:
      dict | Arr<dict>: field values doc
    """

    if (id is None):
      collectionRef = await self.reference()
      docs = collectionRef.stream()
      collection = []
      for doc in docs:
        data = doc.to_dict()
        collection.append(data)
      return collection
    else:
      docRef = await self.reference(id)
      _doc = docRef.get()
      doc = _doc.to_dict()
      return doc