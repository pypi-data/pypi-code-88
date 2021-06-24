def assign(self, dict):

  keys = list(dict.keys())

  for key in keys:
    setattr(self, key, dict[key])