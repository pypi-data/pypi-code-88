from ttgtcanvas2 import WorldModel, Maze
import random

def init(world):
    nb_carrot = 0
    for x in range(2, 9):
        choice = random.randint(1,2)
        if choice == 1:
            world.add_object(x, 1, "carrot", 1)
            nb_carrot += 1
   
    
    world.add_repoter_goal("I counted {} carrots".format(nb_carrot))


def generate_maze():
    world =  WorldModel('./worlds/test.json', init)
    return Maze(world)