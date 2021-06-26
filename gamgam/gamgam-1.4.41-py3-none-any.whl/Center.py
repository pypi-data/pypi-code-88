
# import Area
import os
import time as t

from pygame import *
from gamgam.GameObject import *

# Var Area
global isGameRun, Console, StandardColor, SceneNow, Scenes, Objects
isGameRun = True
SceneNow = 0
Scenes = []
object_level = 12
GameComponents = {}
GameObjects = [[]]
ObjectWaiting = []
ComponentWaiting = []

version = "1.4.41"

# Class Area
class Vector2:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __add__(self, value):
        return Vector2(self.x + value, self.y + value)

    def __sub__(self, value):
        return Vector2(self.x - value, self.y - value)

    def __mul__(self, value):
        return Vector2(self.x * value, self.y * value)

    def __truediv__(self, value):
        return Vector2(self.x / value, self.y / value)

    def __mod__(self, value):
        return Vector2(self.x % value, self.y % value)

    def __radd__(self, value):
        return Vector2(self.x + value, self.y + value)

    def __rsub__(self, value):
        return Vector2(self.x - value, self.y - value)

    def __rmul__(self, value):
        return Vector2(self.x * value, self.y * value)

    def __rtruediv__(self, value):
        return Vector2(self.x / value, self.y / value)

    def __rmod__(self, value):
        return Vector2(self.x % value, self.y % value)


class Color:
    def __init__(self, r: int = 0, g: int = 0, b: int = 0, is_standard: bool = False):
        if is_standard is False:
            self.is_standard = False
            self.color = (r, g, b)
        else:
            self.is_standard = True
            self.White = (255, 255, 255)
            self.Black = (0, 0, 0)
            self.Pink = (255, 0, 127)
            self.Purple = (255, 0, 221)
            self.Blue = (1, 0, 255)
            self.Green = (29, 219, 22)
            self.Yellow = (255, 228, 0)
            self.Orange = (255, 94, 0)
            self.Red = (255, 0, 0)

    def __add__(self, value):
        if self.is_standard is False:
            return Color(self.color[0] + value, self.color[1] + value, self.color[2] + value)

    def __sub__(self, value):
        if self.is_standard is False:
            return Color(self.color[0] - value, self.color[1] - value, self.color[2] - value)

    def __mul__(self, value):
        if self.is_standard is False:
            return Color(self.color[0] * value, self.color[1] * value, self.color[2] * value)

    def __truediv__(self, value):
        if self.is_standard is False:
            return Color(self.color[0] / value, self.color[1] / value, self.color[2] / value)

    def __mod__(self, value):
        if self.is_standard is False:
            return Color(self.color[0] % value, self.color[1] % value, self.color[2] % value)

    def __radd__(self, value):
        if self.is_standard is False:
            return Color(self.color[0] + value, self.color[1] + value, self.color[2] + value)

    def __rsub__(self, value):
        if self.is_standard is False:
            return Color(self.color[0] - value, self.color[1] - value, self.color[2] - value)

    def __rmul__(self, value):
        if self.is_standard is False:
            return Color(self.color[0] * value, self.color[1] * value, self.color[2] * value)

    def __rtruediv__(self, value):
        if self.is_standard is False:
            return Color(self.color[0] / value, self.color[1] / value, self.color[2] / value)

    def __rmod__(self, value):
        if self.is_standard is False:
            return Color(self.color[0] % value, self.color[1] % value, self.color[2] % value)

class GameComponent:
    def set(self):
        pass

    def reflect(self):
        pass

class Transform:
    def __init__(self, position: Vector2 = Vector2(), rotation: int = 0):
        self.position = position
        self.rotation = rotation

    def Translate(self, position: Vector2):
        self.position = position

    def Rotate(self, rotation: int):
        self.rotation = rotation

    def Move(self, position: Vector2):
        self.position = Vector2(self.position.x + position.x, self.position.y + position.y)

    def Turn(self, rotation: int):
        self.rotation += rotation


class Image:
    def __init__(self, image_path: str):
        self.img = image.load(image_path)
        self.path = image_path


class InputManager:
    count = 0

    def __init__(self):
        if InputManager.count == 0:
            InputManager.count += 1
            self.mouse_position = Vector2(0, 0)
            self.mouse_movement = Vector2(0, 0)
            self.is_exit = False
            self.mouse_visible = True
            self.is_pressed = dict(
                MOUSE_LEFT=False,
                MOUSE_WHEEL=False,
                MOUSE_RIGHT=False,
                MOUSE_UP=False,
                MOUSE_DOWN=False,
                A=False,
                B=False,
                C=False,
                D=False,
                E=False,
                F=False,
                G=False,
                H=False,
                I=False,
                J=False,
                K=False,
                L=False,
                M=False,
                N=False,
                O=False,
                P=False,
                Q=False,
                R=False,
                S=False,
                T=False,
                U=False,
                V=False,
                W=False,
                X=False,
                Y=False,
                Z=False,
                NUM_0=False,
                NUM_1=False,
                NUM_2=False,
                NUM_3=False,
                NUM_4=False,
                NUM_5=False,
                NUM_6=False,
                NUM_7=False,
                NUM_8=False,
                NUM_9=False,
                BACK=False,
                TAB=False,
                CLEAR=False,
                ENTER=False,
                PAUSE=False,
                ESCAPE=False,
                SPACE=False,
                EXCLAIM=False,
                QUOTEDBL=False,
                HASH=False,
                DOLLAR=False,
                AMPERSAND=False,
                QUOTE=False,
                LEFTPAREN=False,
                RIGHTPAREN=False,
                ASTERISK=False,
                PLUS=False,
                COMMA=False,
                MINUS=False,
                PERIOD=False,
                SLASH=False,
                COLON=False,
                SEMICOLON=False,
                LESS=False,
                EQUALS=False,
                GREATER=False,
                QUESTION=False,
                AT=False,
                LEFTBRACKET=False,
                RIGHTBRACKET=False,
                BACKSLASH=False,
                CARET=False,
                UNDERSCORE=False,
                BACKQUOTE=False,
                DELETE=False,
                KEY_0=False,
                KEY_1=False,
                KEY_2=False,
                KEY_3=False,
                KEY_4=False,
                KEY_5=False,
                KEY_6=False,
                KEY_7=False,
                KEY_8=False,
                KEY_9=False,
                KEY_PERIOD=False,
                KEY_DIVIDE=False,
                KEY_MULTIPLY=False,
                KEY_MINUS=False,
                KEY_PLUS=False,
                KEY_ENTER=False,
                KEY_EQUALS=False,
                UP=False,
                DOWN=False,
                RIGHT=False,
                LEFT=False,
                INSERT=False,
                HOME=False,
                PAGEUP=False,
                PAGEDOWN=False,
                F1=False,
                F2=False,
                F3=False,
                F4=False,
                F5=False,
                F6=False,
                F7=False,
                F8=False,
                F9=False,
                F10=False,
                F11=False,
                F12=False,
                F13=False,
                F14=False,
                F15=False,
                NUMLOCK=False,
                CAPSLOCK=False,
                SCROLLOCK=False,
                RSHIFT=False,
                LSHIFT=False,
                RCTRL=False,
                LCTRL=False,
                RALT=False,
                LALT=False,
                RMETA=False,
                LMETA=False,
                LSUPER=False,
                RSUPER=False,
                MODE=False,
                HELP=False,
                PRINT=False,
                SYSREQ=False,
                BREAK=False,
                MENU=False,
                POWER=False,
                EURO=False
            )
            self.is_pressed_out = dict(
                MOUSE_LEFT=False,
                MOUSE_WHEEL=False,
                MOUSE_RIGHT=False,
                MOUSE_UP=False,
                MOUSE_DOWN=False,
                A=False,
                B=False,
                C=False,
                D=False,
                E=False,
                F=False,
                G=False,
                H=False,
                I=False,
                J=False,
                K=False,
                L=False,
                M=False,
                N=False,
                O=False,
                P=False,
                Q=False,
                R=False,
                S=False,
                T=False,
                U=False,
                V=False,
                W=False,
                X=False,
                Y=False,
                Z=False,
                NUM_0=False,
                NUM_1=False,
                NUM_2=False,
                NUM_3=False,
                NUM_4=False,
                NUM_5=False,
                NUM_6=False,
                NUM_7=False,
                NUM_8=False,
                NUM_9=False,
                BACK=False,
                TAB=False,
                CLEAR=False,
                ENTER=False,
                PAUSE=False,
                ESCAPE=False,
                SPACE=False,
                EXCLAIM=False,
                QUOTEDBL=False,
                HASH=False,
                DOLLAR=False,
                AMPERSAND=False,
                QUOTE=False,
                LEFTPAREN=False,
                RIGHTPAREN=False,
                ASTERISK=False,
                PLUS=False,
                COMMA=False,
                MINUS=False,
                PERIOD=False,
                SLASH=False,
                COLON=False,
                SEMICOLON=False,
                LESS=False,
                EQUALS=False,
                GREATER=False,
                QUESTION=False,
                AT=False,
                LEFTBRACKET=False,
                RIGHTBRACKET=False,
                BACKSLASH=False,
                CARET=False,
                UNDERSCORE=False,
                BACKQUOTE=False,
                DELETE=False,
                KEY_0=False,
                KEY_1=False,
                KEY_2=False,
                KEY_3=False,
                KEY_4=False,
                KEY_5=False,
                KEY_6=False,
                KEY_7=False,
                KEY_8=False,
                KEY_9=False,
                KEY_PERIOD=False,
                KEY_DIVIDE=False,
                KEY_MULTIPLY=False,
                KEY_MINUS=False,
                KEY_PLUS=False,
                KEY_ENTER=False,
                KEY_EQUALS=False,
                UP=False,
                DOWN=False,
                RIGHT=False,
                LEFT=False,
                INSERT=False,
                HOME=False,
                PAGEUP=False,
                PAGEDOWN=False,
                F1=False,
                F2=False,
                F3=False,
                F4=False,
                F5=False,
                F6=False,
                F7=False,
                F8=False,
                F9=False,
                F10=False,
                F11=False,
                F12=False,
                F13=False,
                F14=False,
                F15=False,
                NUMLOCK=False,
                CAPSLOCK=False,
                SCROLLOCK=False,
                RSHIFT=False,
                LSHIFT=False,
                RCTRL=False,
                LCTRL=False,
                RALT=False,
                LALT=False,
                RMETA=False,
                LMETA=False,
                LSUPER=False,
                RSUPER=False,
                MODE=False,
                HELP=False,
                PRINT=False,
                SYSREQ=False,
                BREAK=False,
                MENU=False,
                POWER=False,
                EURO=False
            )
            self.is_pressing = dict(
                MOUSE_LEFT=False,
                MOUSE_WHEEL=False,
                MOUSE_RIGHT=False,
                MOUSE_UP=False,
                MOUSE_DOWN=False,
                A=False,
                B=False,
                C=False,
                D=False,
                E=False,
                F=False,
                G=False,
                H=False,
                I=False,
                J=False,
                K=False,
                L=False,
                M=False,
                N=False,
                O=False,
                P=False,
                Q=False,
                R=False,
                S=False,
                T=False,
                U=False,
                V=False,
                W=False,
                X=False,
                Y=False,
                Z=False,
                NUM_0=False,
                NUM_1=False,
                NUM_2=False,
                NUM_3=False,
                NUM_4=False,
                NUM_5=False,
                NUM_6=False,
                NUM_7=False,
                NUM_8=False,
                NUM_9=False,
                BACK=False,
                TAB=False,
                CLEAR=False,
                ENTER=False,
                PAUSE=False,
                ESCAPE=False,
                SPACE=False,
                EXCLAIM=False,
                QUOTEDBL=False,
                HASH=False,
                DOLLAR=False,
                AMPERSAND=False,
                QUOTE=False,
                LEFTPAREN=False,
                RIGHTPAREN=False,
                ASTERISK=False,
                PLUS=False,
                COMMA=False,
                MINUS=False,
                PERIOD=False,
                SLASH=False,
                COLON=False,
                SEMICOLON=False,
                LESS=False,
                EQUALS=False,
                GREATER=False,
                QUESTION=False,
                AT=False,
                LEFTBRACKET=False,
                RIGHTBRACKET=False,
                BACKSLASH=False,
                CARET=False,
                UNDERSCORE=False,
                BACKQUOTE=False,
                DELETE=False,
                KEY_0=False,
                KEY_1=False,
                KEY_2=False,
                KEY_3=False,
                KEY_4=False,
                KEY_5=False,
                KEY_6=False,
                KEY_7=False,
                KEY_8=False,
                KEY_9=False,
                KEY_PERIOD=False,
                KEY_DIVIDE=False,
                KEY_MULTIPLY=False,
                KEY_MINUS=False,
                KEY_PLUS=False,
                KEY_ENTER=False,
                KEY_EQUALS=False,
                UP=False,
                DOWN=False,
                RIGHT=False,
                LEFT=False,
                INSERT=False,
                HOME=False,
                PAGEUP=False,
                PAGEDOWN=False,
                F1=False,
                F2=False,
                F3=False,
                F4=False,
                F5=False,
                F6=False,
                F7=False,
                F8=False,
                F9=False,
                F10=False,
                F11=False,
                F12=False,
                F13=False,
                F14=False,
                F15=False,
                NUMLOCK=False,
                CAPSLOCK=False,
                SCROLLOCK=False,
                RSHIFT=False,
                LSHIFT=False,
                RCTRL=False,
                LCTRL=False,
                RALT=False,
                LALT=False,
                RMETA=False,
                LMETA=False,
                LSUPER=False,
                RSUPER=False,
                MODE=False,
                HELP=False,
                PRINT=False,
                SYSREQ=False,
                BREAK=False,
                MENU=False,
                POWER=False,
                EURO=False
            )
        else:
            print("\033[31m" + "InputManager allow just one object." + "\033[0m")

    def GetKeyDown(self, keycode: str):
        if keycode == "ALL":
            pressed = []
            for i in self.is_pressed.keys():
                if self.is_pressed[i]:
                    pressed.append(i)
            return pressed
        return self.is_pressed[keycode]

    def GetKeyUp(self, keycode: str):
        if keycode == "ALL":
            pressed_out = []
            for i in self.is_pressed_out.keys():
                if self.is_pressed_out[i]:
                    pressed_out.append(i)
            return pressed_out
        return self.is_pressed_out[keycode]

    def GetKey(self, keycode: str):
        if keycode == "ALL":
            pressing = []
            for i in self.is_pressing.keys():
                if self.is_pressing[i]:
                    pressing.append(i)
            return pressing
        return self.is_pressing[keycode]

    def Press(self, keycode: str):
        if self.is_pressed[keycode] is not True:
            self.is_pressed[keycode] = True
            self.is_pressing[keycode] = True
            self.is_pressed_out[keycode] = False
        else:
            self.is_pressed[keycode] = False
            self.is_pressing[keycode] = True
            self.is_pressed_out[keycode] = False

    def PressOut(self, keycode: str):
        self.is_pressed[keycode] = False
        self.is_pressing[keycode] = False
        self.is_pressed_out[keycode] = True

    def Exit(self):
        self.is_exit = True

    def isExit(self):
        return self.is_exit

    def move(self, position: Vector2):
        mouse.set_pos(position.x, position.y)

    def init(self):
        for i in self.is_pressed.keys():
            if self.is_pressed[i] is True:
                if self.is_pressing[i] is True:
                    self.is_pressed[i] = False
        for i in self.is_pressed_out.keys():
            if self.is_pressed_out[i] is True:
                if (self.is_pressing[i] and self.is_pressed[i]) is False:
                    self.is_pressed_out[i] = False
        mouse.set_visible(self.mouse_visible);


class ProjectConsole:
    count = 0

    def __init__(self):
        if ProjectConsole.count == 0:
            ProjectConsole.count += 1
        else:
            print("\033[31m" + "ProjectConsole allow just one object." + "\033[0m")

    @staticmethod
    def Log(data):
        Type = type(data)
        if Type == Vector2:
            print(f"({data.x}, {data.y})")
        elif Type == Image:
            print(f"{data.path}")
        elif Type == Color:
            print(f"{data.color}")
        elif Type == Transform:
            print(f"position: ({data.position.x}, {data.position.y}), rotation: {data.rotation}")
        elif Type == ProjectConsole:
            print(f"Console")
        else:
            try:
                print(f"{data.type} Object: name - {data.name}, id - {data.id}")
            except:
                print(data)

    @staticmethod
    def Warn(data: str):
        self.Log("\033[31m" + data + "\033[0m")

    @staticmethod
    def Error(data: str):
        self.Log("\033[31m" + data + "\033[0m")
        finish()
        exit(1)

class Effect:
    def __init__(self, path):
        self.sound = mixer.Sound(path)

class BackGround:
    def __init__(self, path):
        self.sound = path

class GameSoundManager:
    count = 0
    def __init__(self):
        if GameSoundManager.count == 0:
            self.effect = {}
            self.background = {}
            GameSoundManager.count += 1
        else:
            Console.Error("GameSoundManager allow just one object.")
    def load_effect(self, name: str, effect: Effect):
        self.effect[name] = effect
    def load_background(self, name: str, background:BackGround):
        self.background[name] = background
    def shoot(self, name: str, loop:int = 0, max_time:int = 0, fade_ms:int = 0, volume:float = 0.5):
        if name in self.effect:
            self.effect[name].sound.set_volume(volume)
            self.effect[name].sound.play(loop, max_time, fade_ms)
        else:
            Console.Error("No Effect loaded")
    def play(self, name: str, loop:int = 0, start:int = 0, volume:float = 1.0):
        if name in self.background:
            mixer.music.set_volume(volume)
            mixer.music.load(self.background[name])
            mixer.music.play(loop, start)
        else:
            Console.Error("No BackGround loaded")
    def out(self, name: str, milliseconds:int = 0):
        if name in self.effect:
            if milliseconds == 0:
                self.effect[name].sound.stop()
            else:
                self.effect[name].sound.fadeout(milliseconds)
        else:
            Console.Error("No Effect loaded")
    def stop(self, name: str, milliseconds:int = 0):
        if name in self.background:
            if milliseconds == 0:
                mixer.music.stop()
            else:
                mixer.music.fadeout(milliseconds)
            
        else:
            Console.Error("No BackGround loaded")
    def get_volume(self, name:str):
        if name in self.effect:
            return self.effect[name].sound.get_volume()
        elif name in self.background:
            return mixer.music.get_volume()
        else:
            Console.Error("No Sound loaded")
    def pause(self, name):
        if name in self.background:
            mixer.music.pause()
        else:
            Console.Error("No BackGround loaded")

    def pause_out(self, name):
        if name in self.background:
            mixer.music.unpause()
        else:
            Console.Error("No BackGround loaded")
    def set_volume(self, name:str, milliseconds:int = 0):
        if name in self.effect:
            return self.effect[name].sound.set_volume(milliseconds)
        elif name in self.background:
            return mixer.music.set_volume(milliseconds)
        else:
            Console.Error("No Sound loaded")


class TimeManager:
    count = 0
    def __init__(self):
        if TimeManager.count == 0:
            self.deltaTime = 0
            self.invokeFunctions = []
            self.fps = 0
            self.last_count = 0
            self.stopwatch = 0
            TimeManager.count += 1
        else:
            Console.Error("TimeManager allow just one object.")

    def init(self):
        if self.last_count == 0:
            self.last_count = t.time()
        if (t.time() - self.last_count) >= 1:
            self.deltaTime = 1 / self.fps
            self.last_count = t.time()
            self.fps = 0
        for i in self.invokeFunctions:
            if (t.time() - i[1]) >= i[2]:
                i[0]()
                i[1] = t.time()

    def plus_count(self):
        self.fps += 1

    def invoke(self,function, condition = True, delay:int = 1):
        if condition:
            self.invokeFunctions.append([function, t.time(), delay])

    def quit(self, function):
        delete = []
        for i in range(len(self.invokeFunctions)):
            if function == self.invokeFunctions[i][0]:
                delete.append(i)
        for i in delete:
            del self.invokeFunctions[i]

    def start(self):
        self.stopwatch = t.time()

    def stop(self):
        if self.stopwatch == 0:
            return None
        else:
            returning = t.time() - self.stopwatch
            self.stopwatch = 0
            return returning


global Input, Console, StandardColor, default_icon, SoundManager, Time, fps_limit
Input = InputManager()
Console = ProjectConsole()
StandardColor = Color(is_standard=True)
SoundManager = GameSoundManager()
Time = TimeManager()
default_icon = Image(os.path.dirname(os.path.realpath(__file__)) + "\\Default_Icon.PNG")


class PlayScreen:
    def __init__(self, size: Vector2, type: int = FULLSCREEN | HWSURFACE | DOUBLEBUF,
                 background_color: Color = StandardColor.White,
                 project_name: str = "GAMPY_GAME",
                 background: Image = None,
                 icon: Image = default_icon
                 ):
        self.size = (int(size.x), int(size.y))
        self.icon = icon
        self.type = type
        self.project_name = project_name
        self.background = background
        self.color = background_color


# Function Area
def add(data: Vector2, data2: Vector2):
    return Vector2(data.x + data2.x, data.y + data2.y)


def run(fps: int = 60):
    global isGameRun, NowCamera, Objects, fps_limit
    fps_limit = fps
    Console.Log(f"GamGam {version} by Coder-Jang")
    if len(Scenes) <= 0:
        Console.Error("There are no scenes.")
    Now = SceneNow
    isGameRun = True
    clock = time.Clock()
    display.init()
    screen = Scenes[Now]
    display.set_caption(screen.project_name)
    if screen.icon == default_icon:
        display.set_icon(
            Image(os.path.dirname(os.path.realpath(__file__)) + "\\Default_Icon.PNG").img)
    else:
        display.set_icon(screen.icon.img)
    display.set_icon(screen.icon.img)
    if screen.type is not None:
        Screen = display.set_mode(screen.size, screen.type)
    else:
        Screen = display.set_mode(screen.size)
    if screen.background is not None:
        Screen.blit(screen.background.img, (0, 0))
    for i in GameComponents.values():
        i.set()
    for i in GameObjects[Now]:
        i.Start()
    while isGameRun:
        clock.tick(fps_limit)
        Time.init()
        Time.plus_count()
        game_object_init()
        Objects = GameObjects[SceneNow]
        for gameEvent in event.get():
            if gameEvent.type == QUIT:
                Input.Exit()
            if gameEvent.type == KEYDOWN:
                KEYPRESSEVENT(gameEvent)
            if gameEvent.type == KEYUP:
                KEYPRESSOUTEVENT(gameEvent)
            if gameEvent.type == MOUSEBUTTONDOWN:
                if gameEvent.button == 1:
                    Input.Press("MOUSE_LEFT")
                if gameEvent.button == 2:
                    Input.Press("MOUSE_WHEEL")
                if gameEvent.button == 3:
                    Input.Press("MOUSE_RIGHT")
                if gameEvent.button == 4:
                    Input.Press("MOUSE_UP")
                if gameEvent.button == 5:
                    Input.Press("MOUSE_DOWN")
            if gameEvent.type == MOUSEBUTTONUP:
                if gameEvent.button == 1:
                    Input.PressOut("MOUSE_LEFT")
                if gameEvent.button == 2:
                    Input.PressOut("MOUSE_WHEEL")
                if gameEvent.button == 3:
                    Input.PressOut("MOUSE_RIGHT")
                if gameEvent.button == 4:
                    Input.PressOut("MOUSE_UP")
                if gameEvent.button == 5:
                    Input.PressOut("MOUSE_DOWN")
        Input.mouse_position = Vector2(mouse.get_pos()[0], mouse.get_pos()[1])
        Input.mouse_movement = Vector2(mouse.get_rel()[0], mouse.get_rel()[1])
        Screen.fill(screen.color)
        if screen.background is not None:
            Screen.blit(screen.background.img, (0, 0))
        for i in ObjectWaiting:
            i.Start()
            GameObjects[SceneNow].append(i)
        for i in ComponentWaiting:
            i.set()
            GameComponents[i.name] = i
        ObjectWaiting = []
        ComponentWaiting = []
        for i in GameComponents.values():
            i.reflect()
        for i in GameObjects[Now]:
            if i.type == "EmptyObject":
                i.Show()
                i.Update()
            else:
                i.Show()
                i.Update()
                Screen.blit(i.object, i.object_rect)
        display.update()
        if Input.isExit():
            finish()
        if Now != SceneNow:
            Now = SceneNow
            screen = Scenes[Now]
            display.init()
            display.set_caption(screen.project_name)
            if screen.icon == default_icon:
                display.set_icon(
                    Image(os.path.abspath(__file__)[0: len(os.path.abspath(__file__)) - 9] + "Default_Icon.PNG").img)
            else:
                display.set_icon(screen.icon.img)
            display.set_icon(screen.icon.img)
            if screen.type is not None:
                Screen = display.set_mode(screen.size, screen.type)
            else:
                Screen = display.set_mode(screen.size)
            if screen.background is not None:
                Screen.blit(screen.background.img, (0, 0))
            Screen.fill(screen.color)
            for i in GameObjects[Now]:
                i.Start()
        Input.init()
    display.quit()


def KEYPRESSEVENT(gameEvent):
    if gameEvent.key == K_a:
        Input.Press("A")
    elif gameEvent.key == K_b:
        Input.Press("B")
    elif gameEvent.key == K_c:
        Input.Press("C")
    elif gameEvent.key == K_d:
        Input.Press("D")
    elif gameEvent.key == K_e:
        Input.Press("E")
    elif gameEvent.key == K_f:
        Input.Press("F")
    elif gameEvent.key == K_g:
        Input.Press("G")
    elif gameEvent.key == K_h:
        Input.Press("H")
    elif gameEvent.key == K_i:
        Input.Press("I")
    elif gameEvent.key == K_j:
        Input.Press("J")
    elif gameEvent.key == K_k:
        Input.Press("K")
    elif gameEvent.key == K_l:
        Input.Press("L")
    elif gameEvent.key == K_m:
        Input.Press("M")
    elif gameEvent.key == K_n:
        Input.Press("N")
    elif gameEvent.key == K_o:
        Input.Press("O")
    elif gameEvent.key == K_p:
        Input.Press("P")
    elif gameEvent.key == K_q:
        Input.Press("Q")
    elif gameEvent.key == K_r:
        Input.Press("R")
    elif gameEvent.key == K_s:
        Input.Press("S")
    elif gameEvent.key == K_t:
        Input.Press("T")
    elif gameEvent.key == K_u:
        Input.Press("U")
    elif gameEvent.key == K_v:
        Input.Press("V")
    elif gameEvent.key == K_w:
        Input.Press("W")
    elif gameEvent.key == K_x:
        Input.Press("X")
    elif gameEvent.key == K_y:
        Input.Press("Y")
    elif gameEvent.key == K_z:
        Input.Press("Z")
    elif gameEvent.key == K_0:
        Input.Press("NUM_0")
    elif gameEvent.key == K_1:
        Input.Press("NUM_1")
    elif gameEvent.key == K_2:
        Input.Press("NUM_2")
    elif gameEvent.key == K_3:
        Input.Press("NUM_3")
    elif gameEvent.key == K_4:
        Input.Press("NUM_4")
    elif gameEvent.key == K_5:
        Input.Press("NUM_5")
    elif gameEvent.key == K_6:
        Input.Press("NUM_6")
    elif gameEvent.key == K_7:
        Input.Press("NUM_7")
    elif gameEvent.key == K_8:
        Input.Press("NUM_8")
    elif gameEvent.key == K_9:
        Input.Press("NUM_9")
    elif gameEvent.key == K_BACKSPACE:
        Input.Press("BACK")
    elif gameEvent.key == K_TAB:
        Input.Press("TAB")
    elif gameEvent.key == K_CLEAR:
        Input.Press("CLEAR")
    elif gameEvent.key == K_CLEAR:
        Input.Press("CLEAR")
    elif gameEvent.key == K_RETURN:
        Input.Press("ENTER")
    elif gameEvent.key == K_PAUSE:
        Input.Press("PAUSE")
    elif gameEvent.key == K_ESCAPE:
        Input.Press("ESCAPE")
    elif gameEvent.key == K_SPACE:
        Input.Press("SPACE")
    elif gameEvent.key == K_EXCLAIM:
        Input.Press("EXCLAIM")
    elif gameEvent.key == K_QUOTEDBL:
        Input.Press("QUOTEDBL")
    elif gameEvent.key == K_HASH:
        Input.Press("HASH")
    elif gameEvent.key == K_DOLLAR:
        Input.Press("DOLLAR")
    elif gameEvent.key == K_QUOTE:
        Input.Press("QUOTE")
    elif gameEvent.key == K_LEFTPAREN:
        Input.Press("LEFTPAREN")
    elif gameEvent.key == K_RIGHTPAREN:
        Input.Press("RIGHTPAREN")
    elif gameEvent.key == K_ASTERISK:
        Input.Press("ASTERISK")
    elif gameEvent.key == K_PLUS:
        Input.Press("PLUS")
    elif gameEvent.key == K_COMMA:
        Input.Press("COMMA")
    elif gameEvent.key == K_MINUS:
        Input.Press("MINUS")
    elif gameEvent.key == K_PERIOD:
        Input.Press("PERIOD")
    elif gameEvent.key == K_SLASH:
        Input.Press("SLASH")
    elif gameEvent.key == K_COLON:
        Input.Press("COLON")
    elif gameEvent.key == K_SEMICOLON:
        Input.Press("SEMICOLON")
    elif gameEvent.key == K_LESS:
        Input.Press("LESS")
    elif gameEvent.key == K_EQUALS:
        Input.Press("EQUALS")
    elif gameEvent.key == K_GREATER:
        Input.Press("GREATER")
    elif gameEvent.key == K_QUESTION:
        Input.Press("QUESTION")
    elif gameEvent.key == K_AT:
        Input.Press("AT")
    elif gameEvent.key == K_LEFTBRACKET:
        Input.Press("LEFTBRACKET")
    elif gameEvent.key == K_RIGHTBRACKET:
        Input.Press("RIGHTBRACKET")
    elif gameEvent.key == K_BACKSLASH:
        Input.Press("BACKSLASH")
    elif gameEvent.key == K_CARET:
        Input.Press("CARET")
    elif gameEvent.key == K_UNDERSCORE:
        Input.Press("UNDERSCORE")
    elif gameEvent.key == K_BACKQUOTE:
        Input.Press("BACKQUOTE")
    elif gameEvent.key == K_DELETE:
        Input.Press("DELETE")
    elif gameEvent.key == K_KP0:
        Input.Press("KEY_0")
    elif gameEvent.key == K_KP1:
        Input.Press("KEY_1")
    elif gameEvent.key == K_KP2:
        Input.Press("KEY_2")
    elif gameEvent.key == K_KP3:
        Input.Press("KEY_3")
    elif gameEvent.key == K_KP4:
        Input.Press("KEY_4")
    elif gameEvent.key == K_KP5:
        Input.Press("KEY_5")
    elif gameEvent.key == K_KP6:
        Input.Press("KEY_6")
    elif gameEvent.key == K_KP7:
        Input.Press("KEY_7")
    elif gameEvent.key == K_KP8:
        Input.Press("KEY_8")
    elif gameEvent.key == K_KP9:
        Input.Press("KEY_9")
    elif gameEvent.key == K_KP_PERIOD:
        Input.Press("KEY_PERIOD")
    elif gameEvent.key == K_KP_DIVIDE:
        Input.Press("KEY_DIVIDE")
    elif gameEvent.key == K_KP_MINUS:
        Input.Press("KEY_MINUS")
    elif gameEvent.key == K_KP_PLUS:
        Input.Press("KEY_PLUS")
    elif gameEvent.key == K_KP_ENTER:
        Input.Press("KEY_ENTER")
    elif gameEvent.key == K_KP_EQUALS:
        Input.Press("KEY_EQUALS")
    elif gameEvent.key == K_UP:
        Input.Press("UP")
    elif gameEvent.key == K_DOWN:
        Input.Press("DOWN")
    elif gameEvent.key == K_LEFT:
        Input.Press("LEFT")
    elif gameEvent.key == K_RIGHT:
        Input.Press("RIGHT")
    elif gameEvent.key == K_INSERT:
        Input.Press("INSERT")
    elif gameEvent.key == K_HOME:
        Input.Press("HOME")
    elif gameEvent.key == K_PAGEUP:
        Input.Press("PAGEUP")
    elif gameEvent.key == K_PAGEDOWN:
        Input.Press("PAGEDOWN")
    elif gameEvent.key == K_F1:
        Input.Press("F1")
    elif gameEvent.key == K_F2:
        Input.Press("F2")
    elif gameEvent.key == K_F3:
        Input.Press("F3")
    elif gameEvent.key == K_F4:
        Input.Press("F4")
    elif gameEvent.key == K_F5:
        Input.Press("F5")
    elif gameEvent.key == K_F6:
        Input.Press("F6")
    elif gameEvent.key == K_F7:
        Input.Press("F7")
    elif gameEvent.key == K_F8:
        Input.Press("F8")
    elif gameEvent.key == K_F9:
        Input.Press("F9")
    elif gameEvent.key == K_F10:
        Input.Press("F10")
    elif gameEvent.key == K_F11:
        Input.Press("F11")
    elif gameEvent.key == K_F12:
        Input.Press("F12")
    elif gameEvent.key == K_F13:
        Input.Press("F13")
    elif gameEvent.key == K_F14:
        Input.Press("F14")
    elif gameEvent.key == K_F15:
        Input.Press("F15")
    elif gameEvent.key == K_NUMLOCK:
        Input.Press("NUMLOCK")
    elif gameEvent.key == K_CAPSLOCK:
        Input.Press("CAPSLOCK")
    elif gameEvent.key == K_SCROLLOCK:
        Input.Press("SCROLLOCK")
    elif gameEvent.key == K_RSHIFT:
        Input.Press("RSHIFT")
    elif gameEvent.key == K_LSHIFT:
        Input.Press("LSHIFT")
    elif gameEvent.key == K_RCTRL:
        Input.Press("RCTRL")
    elif gameEvent.key == K_LCTRL:
        Input.Press("LCTRL")
    elif gameEvent.key == K_RALT:
        Input.Press("RALT")
    elif gameEvent.key == K_LALT:
        Input.Press("LALT")
    elif gameEvent.key == K_RMETA:
        Input.Press("RMETA")
    elif gameEvent.key == K_LMETA:
        Input.Press("LMETA")
    elif gameEvent.key == K_LSUPER:
        Input.Press("LSUPER")
    elif gameEvent.key == K_RSUPER:
        Input.Press("RSUPER")
    elif gameEvent.key == K_MODE:
        Input.Press("MODE")
    elif gameEvent.key == K_HELP:
        Input.Press("HELP")
    elif gameEvent.key == K_PRINT:
        Input.Press("PRINT")
    elif gameEvent.key == K_SYSREQ:
        Input.Press("SYSREQ")
    elif gameEvent.key == K_BREAK:
        Input.Press("BREAK")
    elif gameEvent.key == K_MENU:
        Input.Press("MENU")
    elif gameEvent.key == K_POWER:
        Input.Press("POWER")
    elif gameEvent.key == K_EURO:
        Input.Press("EURO")


def KEYPRESSOUTEVENT(gameEvent):
    if gameEvent.key == K_a:
        Input.PressOut("A")
    elif gameEvent.key == K_b:
        Input.PressOut("B")
    elif gameEvent.key == K_c:
        Input.PressOut("C")
    elif gameEvent.key == K_d:
        Input.PressOut("D")
    elif gameEvent.key == K_e:
        Input.PressOut("E")
    elif gameEvent.key == K_f:
        Input.PressOut("F")
    elif gameEvent.key == K_g:
        Input.PressOut("G")
    elif gameEvent.key == K_h:
        Input.PressOut("H")
    elif gameEvent.key == K_i:
        Input.PressOut("I")
    elif gameEvent.key == K_j:
        Input.PressOut("J")
    elif gameEvent.key == K_k:
        Input.PressOut("K")
    elif gameEvent.key == K_l:
        Input.PressOut("L")
    elif gameEvent.key == K_m:
        Input.PressOut("M")
    elif gameEvent.key == K_n:
        Input.PressOut("N")
    elif gameEvent.key == K_o:
        Input.PressOut("O")
    elif gameEvent.key == K_p:
        Input.PressOut("P")
    elif gameEvent.key == K_q:
        Input.PressOut("Q")
    elif gameEvent.key == K_r:
        Input.PressOut("R")
    elif gameEvent.key == K_s:
        Input.PressOut("S")
    elif gameEvent.key == K_t:
        Input.PressOut("T")
    elif gameEvent.key == K_u:
        Input.PressOut("U")
    elif gameEvent.key == K_v:
        Input.PressOut("V")
    elif gameEvent.key == K_w:
        Input.PressOut("W")
    elif gameEvent.key == K_x:
        Input.PressOut("X")
    elif gameEvent.key == K_y:
        Input.PressOut("Y")
    elif gameEvent.key == K_z:
        Input.PressOut("Z")
    elif gameEvent.key == K_0:
        Input.PressOut("NUM_0")
    elif gameEvent.key == K_1:
        Input.PressOut("NUM_1")
    elif gameEvent.key == K_2:
        Input.PressOut("NUM_2")
    elif gameEvent.key == K_3:
        Input.PressOut("NUM_3")
    elif gameEvent.key == K_4:
        Input.PressOut("NUM_4")
    elif gameEvent.key == K_5:
        Input.PressOut("NUM_5")
    elif gameEvent.key == K_6:
        Input.PressOut("NUM_6")
    elif gameEvent.key == K_7:
        Input.PressOut("NUM_7")
    elif gameEvent.key == K_8:
        Input.PressOut("NUM_8")
    elif gameEvent.key == K_9:
        Input.PressOut("NUM_9")
    elif gameEvent.key == K_BACKSPACE:
        Input.PressOut("BACK")
    elif gameEvent.key == K_TAB:
        Input.PressOut("TAB")
    elif gameEvent.key == K_CLEAR:
        Input.PressOut("CLEAR")
    elif gameEvent.key == K_CLEAR:
        Input.PressOut("CLEAR")
    elif gameEvent.key == K_RETURN:
        Input.PressOut("ENTER")
    elif gameEvent.key == K_PAUSE:
        Input.PressOut("PAUSE")
    elif gameEvent.key == K_ESCAPE:
        Input.PressOut("ESCAPE")
    elif gameEvent.key == K_SPACE:
        Input.PressOut("SPACE")
    elif gameEvent.key == K_EXCLAIM:
        Input.PressOut("EXCLAIM")
    elif gameEvent.key == K_QUOTEDBL:
        Input.PressOut("QUOTEDBL")
    elif gameEvent.key == K_HASH:
        Input.PressOut("HASH")
    elif gameEvent.key == K_DOLLAR:
        Input.PressOut("DOLLAR")
    elif gameEvent.key == K_QUOTE:
        Input.PressOut("QUOTE")
    elif gameEvent.key == K_LEFTPAREN:
        Input.PressOut("LEFTPAREN")
    elif gameEvent.key == K_RIGHTPAREN:
        Input.PressOut("RIGHTPAREN")
    elif gameEvent.key == K_ASTERISK:
        Input.PressOut("ASTERISK")
    elif gameEvent.key == K_PLUS:
        Input.PressOut("PLUS")
    elif gameEvent.key == K_COMMA:
        Input.PressOut("COMMA")
    elif gameEvent.key == K_MINUS:
        Input.PressOut("MINUS")
    elif gameEvent.key == K_PERIOD:
        Input.PressOut("PERIOD")
    elif gameEvent.key == K_SLASH:
        Input.PressOut("SLASH")
    elif gameEvent.key == K_COLON:
        Input.PressOut("COLON")
    elif gameEvent.key == K_SEMICOLON:
        Input.PressOut("SEMICOLON")
    elif gameEvent.key == K_LESS:
        Input.PressOut("LESS")
    elif gameEvent.key == K_EQUALS:
        Input.PressOut("EQUALS")
    elif gameEvent.key == K_GREATER:
        Input.PressOut("GREATER")
    elif gameEvent.key == K_QUESTION:
        Input.PressOut("QUESTION")
    elif gameEvent.key == K_AT:
        Input.PressOut("AT")
    elif gameEvent.key == K_LEFTBRACKET:
        Input.PressOut("LEFTBRACKET")
    elif gameEvent.key == K_RIGHTBRACKET:
        Input.PressOut("RIGHTBRACKET")
    elif gameEvent.key == K_BACKSLASH:
        Input.PressOut("BACKSLASH")
    elif gameEvent.key == K_CARET:
        Input.PressOut("CARET")
    elif gameEvent.key == K_UNDERSCORE:
        Input.PressOut("UNDERSCORE")
    elif gameEvent.key == K_BACKQUOTE:
        Input.PressOut("BACKQUOTE")
    elif gameEvent.key == K_DELETE:
        Input.PressOut("DELETE")
    elif gameEvent.key == K_KP0:
        Input.PressOut("KEY_0")
    elif gameEvent.key == K_KP1:
        Input.PressOut("KEY_1")
    elif gameEvent.key == K_KP2:
        Input.PressOut("KEY_2")
    elif gameEvent.key == K_KP3:
        Input.PressOut("KEY_3")
    elif gameEvent.key == K_KP4:
        Input.PressOut("KEY_4")
    elif gameEvent.key == K_KP5:
        Input.PressOut("KEY_5")
    elif gameEvent.key == K_KP6:
        Input.PressOut("KEY_6")
    elif gameEvent.key == K_KP7:
        Input.PressOut("KEY_7")
    elif gameEvent.key == K_KP8:
        Input.PressOut("KEY_8")
    elif gameEvent.key == K_KP9:
        Input.PressOut("KEY_9")
    elif gameEvent.key == K_KP_PERIOD:
        Input.PressOut("KEY_PERIOD")
    elif gameEvent.key == K_KP_DIVIDE:
        Input.PressOut("KEY_DIVIDE")
    elif gameEvent.key == K_KP_MINUS:
        Input.PressOut("KEY_MINUS")
    elif gameEvent.key == K_KP_PLUS:
        Input.PressOut("KEY_PLUS")
    elif gameEvent.key == K_KP_ENTER:
        Input.PressOut("KEY_ENTER")
    elif gameEvent.key == K_KP_EQUALS:
        Input.PressOut("KEY_EQUALS")
    elif gameEvent.key == K_UP:
        Input.PressOut("UP")
    elif gameEvent.key == K_DOWN:
        Input.PressOut("DOWN")
    elif gameEvent.key == K_LEFT:
        Input.PressOut("LEFT")
    elif gameEvent.key == K_RIGHT:
        Input.PressOut("RIGHT")
    elif gameEvent.key == K_INSERT:
        Input.PressOut("INSERT")
    elif gameEvent.key == K_HOME:
        Input.PressOut("HOME")
    elif gameEvent.key == K_PAGEUP:
        Input.PressOut("PAGEUP")
    elif gameEvent.key == K_PAGEDOWN:
        Input.PressOut("PAGEDOWN")
    elif gameEvent.key == K_F1:
        Input.PressOut("F1")
    elif gameEvent.key == K_F2:
        Input.PressOut("F2")
    elif gameEvent.key == K_F3:
        Input.PressOut("F3")
    elif gameEvent.key == K_F4:
        Input.PressOut("F4")
    elif gameEvent.key == K_F5:
        Input.PressOut("F5")
    elif gameEvent.key == K_F6:
        Input.PressOut("F6")
    elif gameEvent.key == K_F7:
        Input.PressOut("F7")
    elif gameEvent.key == K_F8:
        Input.PressOut("F8")
    elif gameEvent.key == K_F9:
        Input.PressOut("F9")
    elif gameEvent.key == K_F10:
        Input.PressOut("F10")
    elif gameEvent.key == K_F11:
        Input.PressOut("F11")
    elif gameEvent.key == K_F12:
        Input.PressOut("F12")
    elif gameEvent.key == K_F13:
        Input.PressOut("F13")
    elif gameEvent.key == K_F14:
        Input.PressOut("F14")
    elif gameEvent.key == K_F15:
        Input.PressOut("F15")
    elif gameEvent.key == K_NUMLOCK:
        Input.PressOut("NUMLOCK")
    elif gameEvent.key == K_CAPSLOCK:
        Input.PressOut("CAPSLOCK")
    elif gameEvent.key == K_SCROLLOCK:
        Input.PressOut("SCROLLOCK")
    elif gameEvent.key == K_RSHIFT:
        Input.PressOut("RSHIFT")
    elif gameEvent.key == K_LSHIFT:
        Input.PressOut("LSHIFT")
    elif gameEvent.key == K_RCTRL:
        Input.PressOut("RCTRL")
    elif gameEvent.key == K_LCTRL:
        Input.PressOut("LCTRL")
    elif gameEvent.key == K_RALT:
        Input.PressOut("RALT")
    elif gameEvent.key == K_LALT:
        Input.PressOut("LALT")
    elif gameEvent.key == K_RMETA:
        Input.PressOut("RMETA")
    elif gameEvent.key == K_LMETA:
        Input.PressOut("LMETA")
    elif gameEvent.key == K_LSUPER:
        Input.PressOut("LSUPER")
    elif gameEvent.key == K_RSUPER:
        Input.PressOut("RSUPER")
    elif gameEvent.key == K_MODE:
        Input.PressOut("MODE")
    elif gameEvent.key == K_HELP:
        Input.PressOut("HELP")
    elif gameEvent.key == K_PRINT:
        Input.PressOut("PRINT")
    elif gameEvent.key == K_SYSREQ:
        Input.PressOut("SYSREQ")
    elif gameEvent.key == K_BREAK:
        Input.PressOut("BREAK")
    elif gameEvent.key == K_MENU:
        Input.PressOut("MENU")
    elif gameEvent.key == K_POWER:
        Input.PressOut("POWER")
    elif gameEvent.key == K_EURO:
        Input.PressOut("EURO")


def finish():
    global isGameRun
    isGameRun = False


def define_GameObject(game_object, scene=SceneNow):
    if len(Scenes) <= scene:
        Console.Error("Scene is not defined.")
    if scene == SceneNow:
        ObjectWaiting.append(game_object)
    else:
        GameObjects[scene].append(game_object)


def define_NewScene(screen: PlayScreen):
    global SceneNow
    GameObjects.append([])
    Scenes.append(screen)

def define_GameComponent(component: GameComponent):
    ComponentWaiting.append(component)
    

def Go_Scene(num: int):
    global SceneNow
    if len(Scenes) <= num:
        Console.Error("Scene is not defined.")
    SceneNow = num


def Prev_Scene():
    global SceneNow
    if len(Scenes) <= SceneNow - 1:
        Console.Error("Scene is not defined.")
    if SceneNow - 1 < 0:
        Console.Error("Scene is not defined.")
    SceneNow -= 1


def Next_Scene():
    global SceneNow
    if len(Scenes) <= SceneNow + 1:
        Console.Error("Scene is not defined.")
    SceneNow += 1
    Console.Log(SceneNow)


def find_GameObject(game_object_name: str, scene:int = SceneNow):
    for i in GameObjects[scene]:
        if i.name == game_object_name:
            return i
    return None


def find_GameObject(game_object_id: str, scene:int = SceneNow):
    for i in GameObjects[scene]:
        if i.id == game_object_id:
            return i
    return None


def set_GameObject(game_object_id, game_object, scene:int = SceneNow):
    for i in range(len(GameObjects[scene])):
        if GameObjects[scene][i].id == game_object_id:
            GameObjects[scene][i] = game_object
    return None


def find_GameObjects(game_object_name: str, scene:int = SceneNow):
    re_game_object = []
    for i in GameObjects[scene]:
        if i.name == game_object_name:
            re_game_object.append(i)
    return re_game_object


def find_GameObjects(game_object_id: str, scene:int = SceneNow):
    re_game_object = []
    for i in GameObjects[scene]:
        if i.id == game_object_id:
            re_game_object.append(i)
    return re_game_object

def find_GameObject_Num(game_object_id: str, scene:int = SceneNow):
    num = 0
    for i in range(len(GameObjects[scene])):
        if GameObjects[scene][i].id == game_object_id:
            num += 1
    return num

def now_scene():
    return SceneNow


def is_there_scene(num: int):
    if len(Scenes) <= num:
        return False
    if num < 0:
        return False
    return True


def game_object_init():
    for i in range(len(GameObjects)):
        GameObjects[i] = sorted(GameObjects[i], key=lambda x: x.order, reverse=True)

def change_fps_limit(fps:int):
    global fps_limit
    fps_limit = fps