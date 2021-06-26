from gamgam.Center import *
import os
import random
import time as t

def makeId():
    text = "abcdefghijklmnopqrxtuvwxyz"
    code = ""
    for i in range(object_level):
        if random.randrange(0, 6) <= 3:
            code += str(random.randrange(0, 10))
        else:
            if random.randrange(0, 2) == 0:
                code += text[random.randrange(0, len(text))].upper()
            else:
                code += text[random.randrange(0, len(text))].lower()
    for i in GameObjects[now_scene()]:
        if i.id == code:
            code = makeId()
    return code

class EmptyObject:
    def __init__(self, name: str, size: Vector2=Vector2(50,50), transforms:Transform=Transform(), order:int=1):
        self.name = name
        self.order = order
        self.id = makeId()
        self.size = size
        self.transform = transforms
        self.type = "EmptyObject"
        self.components = {}

    def Show(self):
        for i in self.components.values:
            i.reflect()

    def find_Component(self, Component_Name):
        for i in self.components.keys():
            if i == Component_Name:
                return self.components[i]
        return None
    
    def SetComponent(self, Component):
        Component.set(self.id)
        self.components[Component.component_name] = Component

    def Start(self):
        pass

    def Update(self):
        pass


    
        

class GameObject:
    def __init__(self, name: str, images: Image=Image(os.path.dirname(os.path.realpath(__file__)) + "\\Default_Icon.PNG"), size: Vector2=Vector2(50, 50),
                 transforms: Transform=Transform(), order: int=1):
        self.name = name
        self.order = order
        self.id = makeId()
        self.image = images
        self.size = size
        self.transform = transforms
        self.type = "GameObject"
        self.object = transform.rotate(self.image.img, self.transform.rotation)
        self.object = transform.scale(self.object, (int(self.size.x), int(self.size.y)))
        self.object_rect = self.object.get_rect()
        self.object_rect.center = (self.transform.position.x,
                                   self.transform.position.y)
        self.components = {}

    def Show(self):
        for i in self.components.values():
            i.reflect()
        self.object = transform.rotate(self.image.img, self.transform.rotation)
        self.object = transform.scale(self.object, (int(self.size.x), int(self.size.y)))
        self.object_rect = self.object.get_rect()
        self.object_rect.center = (self.transform.position.x,
                                   self.transform.position.y)

    def find_Component(self,Component_Name):
        for i in self.components.keys():
            if i == Component_Name:
                return self.components[i]
        return None
    
    def SetComponent(self, Component):
        Component.set(self.id)
        self.components[Component.component_name] = Component

    def Start(self):
        pass

    def Update(self):
        pass


class TextBox:
    def __init__(self, name: str, text_content: str="", text_size: int=8, text_font: str=None,
                 text_transform: Transform=Transform(),
                 text_color: Color=StandardColor.Black, anti_aliasing: bool=True
                 , order: int=1):
        self.name = name
        self.id = makeId()
        self.order = order
        self.content = text_content
        self.size = text_size
        self.font = text_font
        self.color = text_color
        self.anti_aliasing = anti_aliasing
        self.transform = text_transform
        self.type = "TextBox"
        self.fontObj = font.Font(self.font, self.size)
        self.object = self.fontObj.render(self.content, self.anti_aliasing, self.color)
        self.object_rect = self.object.get_rect()
        self.object_rect.center = (self.transform.position.x,
                                   self.transform.position.y)
        self.components = {}

    def Show(self):
        for i in self.components.values():
            i.reflect()
        self.fontObj = font.Font(self.font, self.size)
        self.object = self.fontObj.render(self.content, self.anti_aliasing, self.color)
        self.object_rect = self.object.get_rect()
        self.object_rect.center = (self.transform.position.x,
                                   self.transform.position.y)

    def find_Component(self, Component_Name):
        for i in self.components.keys():
            if i == Component_Name:
                return self.components[i]
        return None
    
    def SetComponent(self, Component):
        Component.set(self.id)
        self.components[Component.component_name] = Component

    def Start(self):
        pass

    def Update(self):
        pass


class Button:
    def __init__(self, name: str, button_text: TextBox=TextBox("NewButtonTextBox", "Button", 32),
                 text_scene:int = now_scene(),
                 button_size: Vector2=Vector2(300, 100), button_transform: Transform=Transform(),
                 button_image: Image=Image(os.path.dirname(os.path.realpath(__file__)) + "\\Default_Button.png")
                 , order: int=1):
        self.name = name
        self.id = makeId()
        self.order = order
        self.text_id = button_text.id
        define_GameObject(button_text, text_scene)
        self.image = button_image
        self.scene = text_scene
        self.size = button_size
        self.transform = button_transform
        self.type = "Button"
        self.isClicked = False
        self.isClicking = False
        GameObjects[text_scene][find_GameObject_Num(self.text_id, self.scene)].transform = self.transform
        GameObjects[text_scene][find_GameObject_Num(self.text_id, self.scene)].order = self.order - 1
        self.object = transform.rotate(self.image.img, self.transform.rotation)
        self.object = transform.scale(self.object, (int(self.size.x), int(self.size.y)))
        self.object_rect = self.object.get_rect()
        self.object_rect.center = (self.transform.position.x,
                                   self.transform.position.y)
        self.components = {}

    def Show(self):
        for i in self.components.values():
            i.reflect()
        if self.isClicked is True or self.isClicking is True:
            if not (self.transform.position.x - (self.size.x / 2) <= Input.mouse_position.x <= self.transform.position.x + (self.size.x / 2)):
                self.isClicked = False
                self.isClicking = False
            if not (self.transform.position.y - (self.size.y / 2) <= Input.mouse_position.y <= self.transform.position.y + (self.size.y / 2)):
                self.isClicked = False
                self.isClicking = False
            if Input.GetKeyUp("MOUSE_LEFT"):
                self.isClicked = False
                self.isClicking = False
            self.isClicked = False

        GameObjects[self.scene][find_GameObject_Num(self.text_id, self.scene)].transform = self.transform
        self.object = transform.rotate(self.image.img, self.transform.rotation)
        self.object = transform.scale(self.object, (int(self.size.x), int(self.size.y)))
        self.object_rect = self.object.get_rect()
        self.object_rect.center = (self.transform.position.x,
                                   self.transform.position.y)
        if Input.GetKey("MOUSE_LEFT") and self.isClicking is False:
            if self.transform.position.x - (self.size.x / 2) <= Input.mouse_position.x <= self.transform.position.x + (self.size.x / 2):
                if self.transform.position.y - (self.size.y / 2) <= Input.mouse_position.y <= self.transform.position.y + (self.size.y / 2):
                    self.isClicked = True
                    self.isClicking = True
        
    def find_Component(self, Component_Name):
        for i in self.components.keys():
            if i == Component_Name:
                return self.components[i]
        return None
    
    def SetComponent(self, Component):
        Component.set(self.id)
        self.components[Component.component_name] = Component

    def Start(self):
        pass

    def Update(self):
        pass


class InputField:
    def __init__(self, name: str, input_text: TextBox=TextBox("NewInputFiledTextBox", "", 32),
                 text_scene:int = now_scene(),
                 input_size: Vector2=Vector2(300, 100), input_transform: Transform=Transform(),
                 input_image: Image=Image(os.path.dirname(os.path.realpath(__file__)) + "\\Default_Button.PNG")
                 , order: int=1):
        self.name = name
        self.order = order
        self.id = makeId()
        self.transform = input_transform
        define_GameObject(input_text, text_scene)
        self.scene = text_scene
        self.text = input_text.content
        self.text_id = input_text.id
        self.size = input_size
        self.image = input_image
        self.type = "InputFiled"
        self.isClicked = False
        GameObjects[text_scene][find_GameObject_Num(self.text_id, self.scene)].content = self.text
        GameObjects[text_scene][find_GameObject_Num(self.text_id, self.scene)].transform = self.transform
        GameObjects[text_scene][find_GameObject_Num(self.text_id, self.scene)].order = self.order - 1
        self.object = transform.rotate(self.image.img, self.transform.rotation)
        self.object = transform.scale(self.object, (int(self.size.x), int(self.size.y)))
        self.object_rect = self.object.get_rect()
        self.object_rect.center = (self.transform.position.x,
                                   self.transform.position.y)
        self.components = {}

    def Show(self):
        for i in self.components.values():
            i.reflect()
        GameObjects[self.scene][find_GameObject_Num(self.text_id, self.scene)].content = self.text
        GameObjects[self.scene][find_GameObject_Num(self.text_id, self.scene)].transform = self.transform
        GameObjects[self.scene][find_GameObject_Num(self.text_id, self.scene)].order = self.order - 1
        self.object = transform.rotate(self.image.img, self.transform.rotation)
        self.object = transform.scale(self.object, (int(self.size.x), int(self.size.y)))
        self.object_rect = self.object.get_rect()
        self.object_rect.center = (self.transform.position.x,
                                   self.transform.position.y)
        self.InputEvent()

    def find_Component(self, Component_Name):
        for i in self.components.keys():
            if i == Component_Name:
                return self.components[i]
        return None
    
    def SetComponent(self, Component):
        Component.set(self.id)
        self.components[Component.component_name] = Component

    def InputEvent(self):
        if Input.GetKey("MOUSE_LEFT"):
            if self.transform.position.x - (self.size.x / 2) <= Input.mouse_position.x <= self.transform.position.x + (self.size.x / 2):
                if self.transform.position.y - (self.size.y / 2) <= Input.mouse_position.y <= self.transform.position.y + (self.size.y / 2):
                    self.isClicked = True
        if self.isClicked:
            if Input.GetKeyUp("MOUSE_LEFT"):
                if not (self.transform.position.x - (self.size.x / 2) <= Input.mouse_position.x <= self.transform.position.x + (self.size.x / 2)):
                    self.isClicked = False
                if not (self.transform.position.y - (self.size.y / 2) <= Input.mouse_position.y <= self.transform.position.y + (self.size.y / 2)):
                    self.isClicked = False
                if self.isClicked is False:
                    return
            if Input.GetKey("LSHIFT") or Input.GetKey("RSHIFT"):
                if Input.GetKeyDown("A"):
                    self.text += "A"
                if Input.GetKeyDown("B"):
                    self.text += "B"
                if Input.GetKeyDown("C"):
                    self.text += "C"
                if Input.GetKeyDown("D"):
                    self.text += "D"
                if Input.GetKeyDown("E"):
                    self.text += "E"
                if Input.GetKeyDown("F"):
                    self.text += "F"
                if Input.GetKeyDown("G"):
                    self.text += "G"
                if Input.GetKeyDown("H"):
                    self.text += "H"
                if Input.GetKeyDown("I"):
                    self.text += "I"
                if Input.GetKeyDown("J"):
                    self.text += "J"
                if Input.GetKeyDown("G"):
                    self.text += "G"
                if Input.GetKeyDown("K"):
                    self.text += "K"
                if Input.GetKeyDown("L"):
                    self.text += "L"
                if Input.GetKeyDown("M"):
                    self.text += "M"
                if Input.GetKeyDown("N"):
                    self.text += "N"
                if Input.GetKeyDown("O"):
                    self.text += "O"
                if Input.GetKeyDown("P"):
                    self.text += "P"
                if Input.GetKeyDown("Q"):
                    self.text += "Q"
                if Input.GetKeyDown("R"):
                    self.text += "R"
                if Input.GetKeyDown("S"):
                    self.text += "S"
                if Input.GetKeyDown("T"):
                    self.text += "T"
                if Input.GetKeyDown("U"):
                    self.text += "U"
                if Input.GetKeyDown("V"):
                    self.text += "V"
                if Input.GetKeyDown("W"):
                    self.text += "W"
                if Input.GetKeyDown("X"):
                    self.text += "X"
                if Input.GetKeyDown("Y"):
                    self.text += "Y"
                if Input.GetKeyDown("Z"):
                    self.text += "Z"
            else:
                if Input.GetKeyDown("A"):
                    self.text += "a"
                if Input.GetKeyDown("B"):
                    self.text += "b"
                if Input.GetKeyDown("C"):
                    self.text += "c"
                if Input.GetKeyDown("D"):
                    self.text += "d"
                if Input.GetKeyDown("E"):
                    self.text += "e"
                if Input.GetKeyDown("F"):
                    self.text += "f"
                if Input.GetKeyDown("G"):
                    self.text += "g"
                if Input.GetKeyDown("H"):
                    self.text += "h"
                if Input.GetKeyDown("I"):
                    self.text += "i"
                if Input.GetKeyDown("J"):
                    self.text += "j"
                if Input.GetKeyDown("G"):
                    self.text += "g"
                if Input.GetKeyDown("K"):
                    self.text += "k"
                if Input.GetKeyDown("L"):
                    self.text += "l"
                if Input.GetKeyDown("M"):
                    self.text += "m"
                if Input.GetKeyDown("N"):
                    self.text += "n"
                if Input.GetKeyDown("O"):
                    self.text += "o"
                if Input.GetKeyDown("P"):
                    self.text += "p"
                if Input.GetKeyDown("Q"):
                    self.text += "q"
                if Input.GetKeyDown("R"):
                    self.text += "r"
                if Input.GetKeyDown("S"):
                    self.text += "s"
                if Input.GetKeyDown("T"):
                    self.text += "t"
                if Input.GetKeyDown("U"):
                    self.text += "u"
                if Input.GetKeyDown("V"):
                    self.text += "v"
                if Input.GetKeyDown("W"):
                    self.text += "w"
                if Input.GetKeyDown("X"):
                    self.text += "x"
                if Input.GetKeyDown("Y"):
                    self.text += "y"
                if Input.GetKeyDown("Z"):
                    self.text += "z"
            if Input.GetKeyDown("NUM_0"):
                self.text += "0"
            if Input.GetKeyDown("NUM_1"):
                self.text += "1"
            if Input.GetKeyDown("NUM_2"):
                self.text += "2"
            if Input.GetKeyDown("NUM_3"):
                self.text += "3"
            if Input.GetKeyDown("NUM_4"):
                self.text += "4"
            if Input.GetKeyDown("NUM_5"):
                self.text += "5"
            if Input.GetKeyDown("NUM_6"):
                self.text += "6"
            if Input.GetKeyDown("NUM_7"):
                self.text += "7"
            if Input.GetKeyDown("NUM_8"):
                self.text += "8"
            if Input.GetKeyDown("NUM_9"):
                self.text += "9"
            if Input.GetKeyDown("BACK"):
                self.text = self.text[0: len(self.text) - 1]
            if Input.GetKeyDown("SPACE"):
                self.text += " "

    def Start(self):
        pass

    def Update(self):
        pass


class Component:
    def __init__(self):
        self.this_object = None
        self.component_name = "Component"

    def set(self, this_object):
        self.this_object = this_object

    def reflect(self):
        pass
    
class Collider(Component):
    def __init__(self):
        self.this_object = None
        self.is_crashed = False
        self.crashed_object = []
        self.crashed_direction = []
        self.component_name = "Collider"

    def set(self, this_object):
        self.this_object = this_object

    def reflect(self):
        if self.this_object is not None:
            paren = find_GameObject(self.this_object)
            self.crashed_object = []
            self.crashed_direction = []
            for i in GameObjects[now_scene()]:
                if i.type == "GameObject" or i.type == "EmptyObject":
                    if i != paren:
                        crash = False
                        direct = Vector2()
                        if i.transform.position.x - (i.size.x / 2) <= paren.transform.position.x + (paren.size.x / 2) <= i.transform.position.x + (i.size.x / 2):
                            if i.transform.position.y + (i.size.y / 2) >= paren.transform.position.y - (paren.size.y / 2) >= i.transform.position.y - (i.size.y / 2):
                                crash = True
                            elif i.transform.position.y - (i.size.y / 2) <= paren.transform.position.y + (paren.size.y / 2) <= i.transform.position.y + (i.size.y / 2):
                                crash = True
                        elif i.transform.position.x + (i.size.x / 2) >= paren.transform.position.x - (paren.size.x / 2) >= i.transform.position.x - (i.size.x / 2):
                            if i.transform.position.y + (i.size.y / 2) >= paren.transform.position.y - (paren.size.y / 2) >= i.transform.position.y - (i.size.y / 2):
                                crash = True
                            elif i.transform.position.y - (i.size.y / 2) <= paren.transform.position.y + (paren.size.y / 2) <= i.transform.position.y + (i.size.y / 2):
                                crash = True
                        if crash is True:
                            if i.transform.position.x > paren.transform.position.x:
                                direct.x = 1
                            elif i.transform.position.x < paren.transform.position.x:
                                direct.x = -1
                            elif i.transform.position.x == paren.transform.position.x:
                                direct.x = 0
                            if i.transform.position.y > paren.transform.position.y:
                                direct.y = 1
                            elif i.transform.position.y < paren.transform.position.y:
                                direct.y = -1
                            elif i.transform.position.y == paren.transform.position.y:
                                direct.y = 0
                            self.is_crashed = True
                            self.crashed_object.append(i)
                            self.crashed_direction.append(direct)
                                
            if len(self.crashed_object) <= 0:   
                self.is_crashed = False
                    
    def find_crashed_object(self, game_object):
        is_exist = False
        for i in self.crashed_object:
            if i == game_object:
                return i
        if is_exist is False:
            return None

    def find_crashed_object_direction(self, game_object):
        is_exist = False
        for i in range(0, len(self.crashed_object)):
            if self.crashed_object[i] == game_object:
                return self.crashed_direction[i]
        if is_exist is False:
            return None

class Animator(Component):
    def __init__(self):
        self.this_object = None
        self.component_name = "Animator"
        self.animation = {}
        self.animation_count = {}
        self.now = None
        self.wait = False

    def set(self, this_object):
        self.this_object = this_object

    def reflect(self):
        if self.now is not None:
            if not self.wait:
                self.animation_count[self.now][1] = t.time()
            if self.animation_count[self.now][0] >= len(self.animation[self.now]):
                self.animation_count[self.now][0] = 0
            if type(self.animation[self.now][self.animation_count[self.now][0]]) == int or type(self.animation[self.now][self.animation_count[self.now][0]]) == float:
                self.wait = True
                if t.time() - self.animation_count[self.now][1] >= self.animation[self.now][self.animation_count[self.now][0]]:
                    self.animation_count[self.now][0] += 1
                    self.wait = False
            elif type(self.animation[self.now][self.animation_count[self.now][0]]) == Image:
                find_GameObject(self.this_object).image = self.animation[self.now][self.animation_count[self.now][0]]
                self.animation_count[self.now][0] += 1

    def play(self, animation_name):
        if animation_name in self.animation:
            self.now = animation_name

    def stop(self):
        self.now = None
        for i in self.animation_count.keys():
            self.animation_count[i][0] = 0
            self.animation_count[i][1] = 0

    def add(self, animation_name, animation):
        self.animation[animation_name] = animation
        self.animation_count[animation_name] = [0, 0]


