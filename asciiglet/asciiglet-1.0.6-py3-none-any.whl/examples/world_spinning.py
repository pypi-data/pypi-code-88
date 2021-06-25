from asciiglet import *

coeff = 2.0

environment = Environment(max_x=1024 * coeff, max_y=1024 * coeff, width=1024, height=1024)
environment.origin = environment.center

coords = [
    Vector.new(200.0, 200.0),
    Vector.new(1848.0, 1848.0),
    Vector.new(1024.0, 1024.0),
    Vector.new(612.0, 1024.0),
    Vector.new(1436.0, 1024.0)
]

colors = ["RED", "GREEN", "BLUE", "ORANGE", "CYAN"]

for i, c in enumerate(coords):
    t = Transform(pos=c, scale=Vector.new(10.0, 10.0))
    p = Particle(transform=t, sprite="*")

    p.sprite.color = colors[i]

    environment.particles.append(p)


def on_update(environment, dt):
    environment.transform.angle += 10.0 * dt
    return


if __name__ == "__main__":
    environment.run(on_update=on_update)
