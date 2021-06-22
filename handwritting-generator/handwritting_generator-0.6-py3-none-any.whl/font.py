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
f1=Font(os.path.join(DIR,'Lemon Tuesday.otf'),True,True,False,list('.,;:"()? '),0.8)
f2=Font(os.path.join(DIR,'ofont.ru_BetinaScriptCTT.ttf'),True,True,True,list('+.,;:"-%$[]()«»!?/ '),0.6)
f3=Font(os.path.join(DIR,'ofont.ru_Denistina.ttf'),True,True,True,list('+.,;-:"()«/»!? '))
f4=Font(os.path.join(DIR,'ofont.ru_Eskal.ttf'),True,True,True,list('+.,;-:"()/?! '))
f5=Font(os.path.join(DIR,'ofont.ru_Rozovii Chulok.ttf'),True,True,True,list('+.,;-:"()«/»!? '),0.7)
f6=Font(os.path.join(DIR,'ofont.ru_Shlapak Script.otf'),True,True,True,list('+.,;-:"()/!? '),0.8)
f7=Font(os.path.join(DIR,'Werner4-Regular.ttf'),True,True,False,list('+.,;:"()!? '),0.9)
f8=Font(os.path.join(DIR,'Werner5-Regular.ttf'),True,True,False,list('+.,;:"()!? '),1.1)
f9=Font(os.path.join(DIR,'Werner6-Regular.ttf'),True,True,False,list('.,;:"()!? '),1)
f10=Font(os.path.join(DIR,'Werner7-Regular.ttf'),True,True,False,list('.,;:"()!? '),0.7)
f11=Font(os.path.join(DIR,'Werner11-Regular.ttf'),True,True,False,list('.,;:"()«» '),1.3)
f13=Font(os.path.join(DIR,'Werner_dates-Regular.ttf'),True,False,True,list('.,;:"()/ '),0.8)
f14=Font(os.path.join(DIR,'Werner13-Regular.ttf'),True,True,False,list('.,;:"()«»! '),1.1)
f15=Font(os.path.join(DIR,'Werner14-Regular.ttf'),True,False,True,list(' %,./[]:;'),1.2)
f16=Font(os.path.join(DIR,'Antro_Vectra.otf'),False,False,True,list('+.,;-:"()[]! '),0.6)
f17=Font(os.path.join(DIR,'Jayadhira.ttf'),False,False,True,list(' +%,.-/()[]:;'),0.6)
f18=Font(os.path.join(DIR,'Werner11-Regular (1).ttf'),True,True,False,list(' %,./[]:;'),1.2)
f19=Font(os.path.join(DIR,'Werner15-Regular.ttf'),True,False,True,list('+.,;:"()! '),1.0)
f20=Font(os.path.join(DIR,'Werner16-Regular.ttf'),True,False,True,list(' +%,./()[]:;'),1.1)
f21=Font(os.path.join(DIR,'Werner17-Regular.ttf'),True,True,False,list(' +%,./()[]:;'),1.2)
f22=Font(os.path.join(DIR,'bimbo.regular.ttf'),True,True,False,list(' +%,.-/()[]:;'),0.7)
f23=Font(os.path.join(DIR,'amandasignature.ttf'),False,False,True,list(' +%,.-/()[]:;'),0.6)
f25=Font(os.path.join(DIR,'mathilde.regular.otf'),False,False,True,list(' +%,.-/()[]:;'),1.1)
f27=Font(os.path.join(DIR,'New_werner2-Regular.ttf'),True,True,False,list(' ?!,.:;"()+[]'),1.1)
f28=Font(os.path.join(DIR,'New_werner3-Regular.ttf'),True,True,False,list(' ?!,.:;"()+[]'),1.1)
f29=Font(os.path.join(DIR,'New_werner4-Regular.ttf'),False,True,True,list(' ?!,.:;/-+[]'),1.1)
f30=Font(os.path.join(DIR,'New_werner5-Regular.ttf'),False,True,True,list(' ?!,.:;/-+[]'),1.1)
f31=Font(os.path.join(DIR,'Werner20-Regular.ttf'),True,False,True,list(' %,./()[]:;'),1.3)
f32=Font(os.path.join(DIR,'Werner21-Regular.ttf'),True,False,True,list(' %,./()[]:;'),1.1)
f33=Font(os.path.join(DIR,'Werner22-Regular.ttf'),True,False,True,list('!%/,./()[]:;'),1.1)
f34=Font(os.path.join(DIR,'Werner23-Regular.ttf'),True,False,True,list('!%/,./()[]:;'),1.0)
f35=Font(os.path.join(DIR,'Werner31-Regular.ttf'),True,False,True,list('!%+,./"[]:;'),1.2)
f=[f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f13,f14,f15,f16,f17,f18,f19,f20,f21,f22,f23,f25,f27,f28,f29,f30,f31,f32,f33,f34,f35]