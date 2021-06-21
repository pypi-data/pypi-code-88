class 动物:
  def __init__(self):
    print(1)

class 野生:
  def __init__(self, 数量):
    print(数量)

class 人(动物):
  def __init__(self):
    super().__init__()

class 狼(野生):
  def __init__(self):
    super().__init__(2)

人()
狼()