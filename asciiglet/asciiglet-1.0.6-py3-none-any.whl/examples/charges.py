import random

from asciiglet import *


random.seed(42)


environment = Environment(max_x=1024, max_y=720, width=1024, height=720)

for i in range(30):
    x = random.uniform(0, 1024)
    y = random.uniform(0, 720)

    charge = random.uniform(-5.0, 5.0)

    mass = random.uniform(0.25, 1.0)

    symbol = "+"
    color = "RED"
    if charge < 0:
        symbol = "-"
        color = "BLUE"
    elif charge == 0:
        symbol = "n"
        color = "WHITE"

    size = charge * mass * 2

    scale = Vector.new(size, size)

    p = Particle(
        sprite=symbol, transform=Transform(pos=Vector.new(x, y), scale=scale)
    )
    p.sprite.color = color
    p.add_effect(ChargedPE(weight=mass, charges={"electricity": charge}))

    environment.particles.append(p)

if __name__ == "__main__":
    environment.run()
