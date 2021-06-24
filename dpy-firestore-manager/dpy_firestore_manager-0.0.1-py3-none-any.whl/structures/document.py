from .database import Database

class Document(Database):

  """
  Document structure

  Args:
    path (str): absolute path leading to the document

  Attributes:
    path (str): absolute path leading to the document
  """
  
  def __init__(self, path):

    super().__init__()
    self.path = path


  async def reference(self):

    """
    Gets doc reference

    Returns:
      Firebase.docRef: reference to doc
    """
    
    return self.db.doc(f'{self.path}')


  async def data(self):

    """
    Gets doc field values

    Returns:
      dict: field values doc
    """

    docRef = await self.reference()
    doc = docRef.get()
    return doc.to_dict()