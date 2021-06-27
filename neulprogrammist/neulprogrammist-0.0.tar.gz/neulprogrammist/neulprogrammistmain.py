lib = "neulprogrammist"
import math
import random
class students:
    def __init__(self, fullname, grades, scores):
        self.fullname = fullname
        self.grades = grades
        self.scores = scores

std1 = students("None", [4397214926], 100)
#random
def randomint(number1, number2):
    num = random.randint(number1, number2)
    print(num)
def randomrange(num1, num2):
    dumber = random.randrange(num1, num2)   
    print(dumber)
#math    
def kvadrat(number, count):
    print(number**count)
#type change    
def setfloat(argument):
    print(float(argument))
def setint(argument):
    print(int(argument))
def setstr(argument):
    print(str(argument))             
def setbool(argument):
    print(bool(argument))     
def setset(argument):
    print(set(argument))
def settuple(argument):
    print(tuple(argument))
#analog for    
def loop(argument, count):
    for argument in count:
        print(argument)
def help():
    print("Help for functions and classes: Functions: randomint(number1, number2) randomrange(num1, num2)  kvadrat(number, count) type change functions setfloat(argument) setint(argument) setstr(argument) and more Loop: loop(argument, count)Classes: students")
def youtube():
    print("Library creator youtube channel https://www.youtube.com/channel/UCfS1tlFYSWhlFMzdryW56Ng")
def discord():
    print("Library creator discord server https://discord.gg/2frhEHRVad")        
            
#paint
class paint:
    def __init__(self,brushsize,classicafication, paintobject):
        self.brushsize = brushsize
        self.classification = classicafication
        self.paintobject = paintobject
po1 = paint(155,"object", "people")       
def painttheobject( classicafication,object):
    if object == "people" and classicafication == "alive":
        print("👨‍💼")
    else:
        print("Name error! painttheobject() argument is not defined! painttheobject() arguments classification - alive obhect - people")    
            
   

