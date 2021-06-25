import numpy as np

from asciiglet import *


environment = Environment()

hour_marks = 12

angle_per_hour = -360 / hour_marks

angle = 90

clock_origin = Vector.new(500.0, 375.0)


transforms = []


for i in range(hour_marks):
    pos = Vector.rotate(Vector.new(1.0, 0.0), angle)
    pos = clock_origin + pos * 200.0

    t = Transform(pos=pos)
    t_target = Transform(parent=t)
    t_target.name = str(angle)
    transforms.append(t_target)

    p = Particle(transform=t)

    angle += angle_per_hour
    environment.particles.append(p)


t = Transform(pos=clock_origin)
arrow = Particle(transform=t, sprite="@-------")

arrow.name = "Hour arrow."

arrow.transform.angle = 120

arrow.sprite.set_anchor_x("left")
arrow.sprite.offset = Vector.new(-5.0, 0.0)

rotation_time = 60.0
time_per_mark = rotation_time / hour_marks

for i in range(hour_marks):
    arrow.add_effect(
        TimedPE(
            LastingPE(
                FaceTransformPE(
                    transforms[i],
                    turn_speed=300.0
                ),
                max_time=2.0,
                refresh_after=rotation_time - 2.0
            ),
            time=time_per_mark * (i + 1)
        )
    )

environment.particles.append(arrow)

t = Transform(pos=clock_origin)
second = Particle(transform=t, sprite="o-----------------")

second.transform.angle = 90.0

second.name = "Second arrow."

second.sprite.set_anchor_x("left")
second.sprite.offset = Vector.new(-5.0, 2.0)

second.rotation = -360.0 * hour_marks / rotation_time

environment.particles.append(second)


if __name__ == "__main__":
    environment.run()
