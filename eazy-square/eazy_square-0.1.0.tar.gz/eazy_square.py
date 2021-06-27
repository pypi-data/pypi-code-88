from colorama import Fore, Back, Style

class Square:
    def __init__(self, weight, height):
        self.weight = weight
        self.height = height
    
    def draw(self, size : int=1):
        for y in range(self.height*size):
            for x in range(self.weight*size):
                print("██", end='')
            print()