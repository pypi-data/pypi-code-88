import random

import numpy as np

from asciiglet import *


random.seed(42)


environment = Environment(max_x=1024, max_y=720, width=1024, height=720)


def get_blazetrail(pe):
    t = Transform(
        pos=np.copy(pe.particle.transform.pos),
        scale=Vector.new(0.4, 0.4),
    )
    p = Particle(transform=t)

    p.sprite.color = pe.particle.sprite.color

    p.add_effect(
        DissipatePE(loss=0.5, sprites="*")
    )

    p.acceleration[1] = random.uniform(-3.0, -5.0)

    return [p]


def get_trailblazer(pe):
    palettes = [
        ["RED", "ORANGE", "YELLOW"],
        ["BLUE", "GREEN", "CYAN"],
        ["RED", "PURPLE", "PINK"],
        ["GREEN", "YELLOW", "ORANGE"],
        ["RED", "PURPLE", "PINK", "WHITE"],
        ["PINK", "ORANGE", "WHITE", "BLUE"],
    ]
    palette = random.choice(palettes)

    particles = random.randrange(15, 30)

    angle_per_particle = 360.0 / particles

    angle = random.uniform(0.0, 360.0)

    explosion_particles = []

    for i in range(particles):
        t = Transform(
            pos=np.copy(pe.particle.transform.pos),
            scale=Vector.new(0.5, 0.5),
        )
        p = Particle(transform=t)

        p.transform.angle = angle

        noise = Vector.new(
            random.uniform(-5.0, 5.0), random.uniform(-5.0, 5.0)
        )

        p.velocity = p.transform.forward() * 10 + noise
        p.acceleration = p.transform.forward() * 10
        p.acceleration[1] = random.uniform(-3.0, -5.0)

        p.sprite.color = random.choice(palette)

        p.add_effect(
            DissipatePE(loss=0.35)
        )

        p.add_effect(
            CooldownPE(
                EmitPE(
                    particles=get_blazetrail,
                ),
                time=0.6,
            )
        )

        angle += angle_per_particle
        explosion_particles.append(p)

    return explosion_particles


def get_ball(pe):
    palettes = [
        ["RED", "ORANGE", "YELLOW"],
        ["BLUE", "GREEN", "CYAN"],
        ["RED", "PURPLE", "PINK"],
        ["GREEN", "YELLOW", "ORANGE"],
        ["RED", "PURPLE", "PINK", "WHITE"],
        ["PINK", "ORANGE", "WHITE", "BLUE"],
    ]
    palette = random.choice(palettes)

    particles = random.randrange(40, 60)

    angle_per_particle = 360.0 / particles

    angle = random.uniform(0.0, 360.0)

    explosion_particles = []

    for i in range(particles):
        t = Transform(
            pos=np.copy(pe.particle.transform.pos),
            scale=Vector.new(0.75, 0.75),
        )
        p = Particle(transform=t)

        p.transform.angle = angle

        noise = Vector.new(
            random.uniform(-5.0, 5.0), random.uniform(-5.0, 5.0)
        )

        p.velocity = p.transform.forward() * 10 + noise
        p.acceleration = p.transform.forward() * 10

        p.sprite.color = random.choice(palette)

        p.add_effect(
            DissipatePE(loss=0.2)
        )

        angle += angle_per_particle
        explosion_particles.append(p)

    return explosion_particles


def get_explosion(pe):
    expl_type = random.choice([get_ball, get_trailblazer])

    return expl_type(pe)


def get_trail(pe):
    trails = []

    amount = random.randrange(1, 3)

    for i in range(amount):
        scale = random.uniform(0.3, 0.4)

        t = Transform(
            pos=np.copy(pe.particle.transform.pos),
            scale=Vector.new(scale, scale),
        )
        p = Particle(transform=t)

        p.transform.pos -= pe.particle.transform.forward() * 12

        noise = Vector.new(
            random.uniform(-10.0, 10.0), random.uniform(-10.0, 10.0)
        )

        p.velocity = (pe.particle.transform.forward() * -24) + noise

        p.acceleration = Vector.new(
            random.uniform(-15.0, 15.0), random.uniform(-15.0, 15.0)
        )

        p.add_effect(
            DissipatePE(loss=0.5)
        )

        trails.append(p)

    return trails


def get_fireworks(emitter):
    launches = random.randrange(1, 6)
    amount = random.randrange(1, 7)

    fireworks = []

    launch_pads = []

    for i in range(launches):
        x = random.uniform(100.0, 900.0)
        y = -50.0
        launch_pads.append((x, y))

    for i in range(amount):
        launch_pad = random.choice(launch_pads)
        x = launch_pad[0]
        y = launch_pad[1]

        t = Transform(
            pos=Vector.new(x, y),
            scale=Vector.new(0.85, 0.85),
        )
        p = Particle(transform=t, sprite="---@>")

        p.sprite.set_anchor_x("right")

        p.sprite.color = random.choice([
            "RED",
            "ORANGE",
            "YELLOW",
            "GREEN",
            "CYAN",
            "BLUE",
            "PURPLE",
            "PINK",
            "WHITE"
        ])

        p.transform.angle = random.uniform(80.0, 100.0)

        p.rotation = random.uniform(-1.0, 1.0)
        p.rotation_acceleration = random.uniform(-1.0, 1.0)

        p.velocity = Vector.new(
            random.uniform(-5.0, 5.0),
            random.uniform(-5.0, 5.0)
        )

        p.add_effect(
            DissipatePE(
                sprites=["---@>", "--@>", "-@>", "@>"],
                loss=random.uniform(0.25, 0.35)
            )
        )

        p.add_effect(
            CooldownPE(
                EmitPE(
                    particles=get_trail,
                ),
                max_time=0.1,
            )
        )

        p.add_effect(
            OnDestroyPE(
                EmitPE(
                    particles=get_explosion,
                ),
            )
        )

        p.add_effect(
            ForwardMovementPE(
                forward_velocity=100.0,
                forward_acceleration=10.0
            )
        )

        fireworks.append(p)

    return fireworks


e = Emitter(particles=get_fireworks, cooldown=5)
environment.particles.append(e)

if __name__ == "__main__":
    environment.run()
