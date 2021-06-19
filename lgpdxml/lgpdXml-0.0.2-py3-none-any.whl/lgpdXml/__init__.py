class lgpdXml:
    def __init__(self,text):
        self.text = text

    def find(self,tagIni,tagEnd):
        ini = 0
        end = 0
        val = []
        for x in range(self.text.count(tagIni)):
            if  x == 0:
                ini = self.text.find(tagIni) + len(tagIni)
                end = self.text.find(tagEnd,ini)
            else:
                ini = self.text.find(tagIni,ini) + len(tagIni)
                end = self.text.find(tagEnd,ini)
            val.append(self.text[ini:end])
        if len(val) > 1:
            return val
        else:
            return val[0]

    def replace(self,tagIni,value,tagEnd,text):
        return self.text.replace(tagIni+value+tagEnd,tagIni+text+tagEnd)
