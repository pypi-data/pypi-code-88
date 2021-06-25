import random

import numpy as np

from asciiglet import *


random.seed(42)


environment = Environment(max_x=1024, max_y=720, width=1024, height=720)


seaweed_amount = 20

lengths = [0] * seaweed_amount
for i in range(len(lengths)):
    lengths[i] = random.uniform(10.0, 30.0)


def get_seaweed(pe):
    t = Transform(
        pos=np.copy(pe.particle.transform.pos),
        scale=Vector.new(0.7, 0.7),
    )
    p = Particle(transform=t, sprite="~")

    p.transform.angle = random.uniform(85.0, 95.0)

    p.velocity = (
        pe.particle.transform.forward() * lengths[int(pe.particle.name)]
    )

    p.add_effect(DissipatePE(loss=0.5, sprites="~-"))

    p.sprite.color = "GREEN"

    return [p]


for i in range(seaweed_amount):
    x = random.uniform(0.0, 1000.0)
    y = random.uniform(0.0, 700.0)

    pos = Vector.new(x, y)

    t = Transform(pos=pos, scale=Vector.new(0.7, 0.7))
    p = Particle(transform=t, sprite="@~")

    p.name = str(i)

    p.sprite.anchor_x = 'left'
    p.sprite.color = "GREEN"

    p.transform.angle = 90.0

    deviation = random.uniform(3.0, 5.0)

    p.rotation = deviation
    p.rotation_acceleration = deviation

    p.add_effect(ChangingRotationPE(limit_speed=2 * deviation))

    p.add_effect(
        CooldownPE(
            EmitPE(get_seaweed),
            max_time=0.3,
        )
    )

    environment.particles.append(p)

for i in range(30):
    x = random.uniform(0.0, 200.0)
    y = random.uniform(250.0, 450.0)
    pos = Vector.new(x, y)

    t = Transform(pos=pos, scale=Vector.new(0.7, 0.7))
    p = Particle(transform=t, sprite="><>")

    p.sprite.color = "RED"

    p.transform.angle = 0

    p.add_effect(BoidPE())
    p.add_effect(FaceMovementPE(turn_speed=10.0))

    environment.particles.append(p)

for i in range(40):
    x = random.uniform(500.0, 700.0)
    y = random.uniform(250.0, 450.0)

    pos = Vector.new(x, y)

    t = Transform(pos=pos, scale=Vector.new(0.7, 0.7))
    p = Particle(transform=t, sprite="><>")

    p.sprite.color = "BLUE"

    p.transform.angle = 180

    p.add_effect(BoidPE())
    p.add_effect(FaceMovementPE(turn_speed=100.0))

    environment.particles.append(p)

if __name__ == "__main__":
    environment.run()
