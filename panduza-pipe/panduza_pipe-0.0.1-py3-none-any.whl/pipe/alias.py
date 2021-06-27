


class Alias:
    """
    Static objects to store helper for tests
    """

    Data = {}
    ServerUrl = ""

    @staticmethod
    def GetUrl(alias):
        return Alias.Data[alias]

    @staticmethod
    def GetAliases():
        return Alias.Data.keys()

    @staticmethod
    def LoadServerUrl(url):
        Alias.ServerUrl = url

    @staticmethod
    def LoadAlias(alias):
        Alias.Data = alias

    @staticmethod
    def LoadAliasFromFile(filename):
        # Alias.Data = alias
        pass


