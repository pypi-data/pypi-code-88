import os

class Font:
    def __init__(self, path, cyr_small, cyr_capit, digits, chars=[], size_coef=1):
        self.path = path
        self.chars = chars
        self.size_coef = size_coef

        if cyr_small:
            for char in range(1072, 1104):
                self.chars.append(chr(char))
            self.chars.append('ё')
        if cyr_capit:
            for char in range(1040, 1072):
                self.chars.append(chr(char))
        if digits:
            for i in range(0, 10):
                self.chars.append(str(i))

    def isValid(self, string):
        chars = set(string)
        for char in string:
            if char not in self.chars:
                return False
        return True

    def __str__(self):
        result = self.path + '\n'
        for char in self.chars:
            result += char + ' '
        return result

dirname = os.path.dirname(__file__)
DIR = os.path.join(dirname, 'content')
f1=Font(os.path.join(DIR,'Lemon Tuesday.otf'),True,True,False,list('.,;:"()? '),0.7)
f2=Font(os.path.join(DIR,'ofont.ru_BetinaScriptCTT.ttf'),True,True,True,list('+.,;:"-%$[]()«»!?/ '),0.6)
f3=Font(os.path.join(DIR,'ofont.ru_Denistina.ttf'),True,True,True,list('+.,;-:"()«/»!? '),0.8)
f4=Font(os.path.join(DIR,'ofont.ru_Eskal.ttf'),True,True,True,list('+.,;-:"()/?! '),0.8)
f5=Font(os.path.join(DIR,'ofont.ru_Rozovii Chulok.ttf'),True,True,True,list('+.,;-:"()«/»!? '),0.7)
f6=Font(os.path.join(DIR,'ofont.ru_Shlapak Script.otf'),True,True,True,list('+.,;-:"()/!? Regular'),0.7)
f7=Font(os.path.join(DIR,'werner4.ttf'),True,True,False,list('+.,;:"()!? '),0.9)
f8=Font(os.path.join(DIR,'werner5.ttf'),True,False,False,list('+.,;:"()!? '),1.1)
f9=Font(os.path.join(DIR,'werner6.ttf'),True,True,False,list('.,;:"()!? '),1)
f10=Font(os.path.join(DIR,'werner7.ttf'),True,True,False,list('.,;:"()!? '),0.7)
f13=Font(os.path.join(DIR,'werner1.ttf'),True,False,True,list('.,;:"()/ '),0.8)
f14=Font(os.path.join(DIR,'werner13.ttf'),True,True,False,list('.,;:"()«»! '),1.2)
f15=Font(os.path.join(DIR,'werner14.ttf'),True,False,True,list(' %,./[]:;'),1.2)
f16=Font(os.path.join(DIR,'Antro_Vectra.otf'),False,False,True,list('+.,;-:"()[]! '),0.6)
f17=Font(os.path.join(DIR,'Jayadhira.ttf'),False,False,True,list(' +%,.-/()[]:;'),0.6)
f18=Font(os.path.join(DIR,'werner11.ttf'),True,True,False,list(' %,./[]:;'),1.2)
f19=Font(os.path.join(DIR,'werner15.ttf'),True,False,True,list('+.,;:"()! '),1.0)
f20=Font(os.path.join(DIR,'werner16.ttf'),True,False,True,list(' +%,./()[]:;'),1.1)
f21=Font(os.path.join(DIR,'werner17.ttf'),True,True,False,list(' +%,./()[]:;'),1.2)
f22=Font(os.path.join(DIR,'bimbo.regular.ttf'),True,True,False,list(' +%,.-/()[]:;'),0.7)
f23=Font(os.path.join(DIR,'amandasignature.ttf'),False,False,True,list(' +%,.-/()[]:;'),0.6)
f25=Font(os.path.join(DIR,'mathilde.regular.otf'),False,False,True,list(' +%,.-/()[]:;'),1.1)
f27=Font(os.path.join(DIR,'werner2.ttf'),True,True,False,list(' ?!,.:;"()+[]'),1.1)
f28=Font(os.path.join(DIR,'werner3.ttf'),True,True,False,list(' ?!,.:;"()+[]'),1.1)
f31=Font(os.path.join(DIR,'werner20.ttf'),True,False,True,list(' %,./()[]:;'),1.3)
f24=Font(os.path.join(DIR,'werner21.ttf'),True,False,True,list(' %,./()[]:;'),1.3)
f33=Font(os.path.join(DIR,'werner22.ttf'),True,False,True,list('!%/,./()[]:;'),1.1)
f34=Font(os.path.join(DIR,'werner23.ttf'),True,False,True,list('!%/,./()[]:;'),1.0)
f35=Font(os.path.join(DIR,'werner31.ttf'),True,False,True,list('!%+,./"[]:;'),1.2)
f32=Font(os.path.join(DIR,'werner35.ttf'),True,False,True,list('!%+,./"[]:;'),1.2)
f39=Font(os.path.join(DIR,'werner36.ttf'),True,False,True,list('!%+,./"()[]:;'),1.2)
f40=Font(os.path.join(DIR,'werner37.ttf'),True,False,True,list('!%+,./"()[]:;'),1.2)
f41=Font(os.path.join(DIR,'werner10.ttf'),True,True,False,list(''),1.3)
f42=Font(os.path.join(DIR,'werner30.ttf'),True,True,False,list(''),1.3)
f=[f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f13,f14,f15,f16,f17,f18,f19,f20,f21,f22,f23,f24,f25,f27,f28,f31,f33,f32,f34,f35,f39,f40,f41,f42]