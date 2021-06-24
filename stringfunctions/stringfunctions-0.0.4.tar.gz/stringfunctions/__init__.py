import pywhatkit as kit


class StringFunction:
    def __init__(self):
        self.text = None
        
    def append(self, *args):
        res = ""
        for i in args:
            res = res+i
        self.text = self.text+res
        return self.text

    def delchars(self, *args):
        for i in args:
            self.text = self.text.replace(i, " ")
        return self.text

    def splitwords(self):
        self.text = self.text.split(" ")
        return self.text

    def lower(self):
        self.text = self.text.lower()
        return self.text

    def upper(self):
        self.text = self.text.upper()
        return self.text

    def camelcase(self):
        lst = []
        self.splitwords()
        for i in self.text:
            lst.append(i.title())
        self.text = "".join(lst)
        return self.text

    def writefile(self, filename):
        with open(converttosf(filename).append(".txt"), "w+") as f:
            f.write(self.text)


def converttosf(strvar):
    x = StringFunction()
    x.text = strvar
    return x


def converttostr(stringfunctionvar: StringFunction):
    x = stringfunctionvar.text
    return x


def libcredits():
    print("This library was made by Leonard W. please look at the GitHub repostiory for informations about this library (https://www.github.com/thanamesleo/stringfunctions)")


def toascii(file, output):
    kit.image_to_ascii_art(file, output)