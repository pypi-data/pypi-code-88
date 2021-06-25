import random

import numpy as np

from asciiglet import *


random.seed(42)


environment = Environment(max_x=1024, max_y=720, width=1024, height=720)

p1 = Particle(
    transform=Transform(
        pos=Vector.new(500.0, 350.0),
        scale=Vector.new(3.0, 3.0)
    )
)
p1.add_effect(GravityPE(weight=3.0))
p1.velocity = np.array([10.0, 0.0])
p1.sprite.color = "GREEN"

p2 = Particle(
    transform=Transform(
        pos=Vector.new(500.0, 250.0),
        scale=Vector.new(5.0, 5.0)
    )
)
p2.add_effect(GravityPE(weight=5.0))
p2.transform.face(p1.transform)
p2.sprite.color = "PINK"

t3 = Transform(pos=Vector.new(300.0, 450.0))
p3 = Particle(transform=t3, sprite=")o>")
p3.sprite.color = "WHITE"
p3.velocity = Vector.new(15.0, 0.0)
p3.acceleration = Vector.new(-0.1, 0.0)
p3.add_effect(GravityPE(weight=1.0))
p3.add_effect(FaceMovementPE(turn_speed=10))


def get_smoke(emitter):
    vx = 10 - random.uniform(0.0, 8.0)
    vy = random.uniform(-3.0, 3.0)

    vel = Vector.rotate(Vector.new(vx, vy), emitter.transform.parent.angle)

    size = random.uniform(0.2, 0.5)

    t = Transform(
        pos=np.copy(emitter.transform.pos), scale=np.array([size, size])
    )
    t.pos -= emitter.transform.parent.forward() * 14

    s = Particle(transform=t)
    s.velocity = vel
    s.add_effect(DissipatePE(max_amount=1, loss=0.1))
    s.sprite.color = random.choice(["RED", "ORANGE", "YELLOW"])
    # s.add_effect(ConstantPE(velocity=Vector.new(vx, vy)))

    return [s]


e3 = Emitter(particles=get_smoke, cooldown=0.01)
e3.transform.setParent(t3)

environment.particles.extend([p1, p2, p3, e3])

if __name__ == "__main__":
    environment.run()
