class check:
    def __init__(self,words):
        self.words = words
    def find(self):
        swear = ["fuck","bitch","asshole"] #these are not meant as hate words
        for word in self.words:
            word = word.lower()
            if word in swear:
                return True
        return False