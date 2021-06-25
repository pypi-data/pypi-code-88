#!/usr/bin/env python3
# coding: utf-8

from math import *
from zencad import *
from screw import *


class ScrewBolt:
    _tech = 0.0001

    def __init__(
            self,
            screwStyle: ScrewStyle,
            friction: float,
            screw_radius: float,
            screw_length: float,
            wall: float
    ):
        cap_radius = screw_radius + screwStyle.depth + wall
        cap_sbtn_radius = cap_radius + friction * sqrt(2)

        self.bolt = self._create_bolt(
            screwStyle=screwStyle,
            screw_radius=screw_radius,
            screw_length=screw_length,
            cap_radius=cap_radius,
            wall=wall
        )

        self.cap_sbtn = cone(cap_sbtn_radius, 0, cap_sbtn_radius)
        self.cap_base_radius = cap_sbtn_radius + wall

        self.base_sbtn = self._create_base_sbtn(
            screwStyle=screwStyle,
            screw_radius=screw_radius,
            screw_length=screw_length
        )
        self.base_radius = screw_radius + screwStyle.depth + friction * sqrt(2) + wall
        self.base_length = friction + screw_length + friction + wall

    def _create_bolt(
            self,
            screwStyle: ScrewStyle,
            screw_radius: float,
            screw_length: float,
            cap_radius: float,
            wall: float
    ):
        height = screw_length + wall
        result = screwStyle.create_shape(screw_radius, height - self._tech)
        result = result.up(self._tech)
        screw_istn_radius = screw_radius + screwStyle.depth
        screw_sbtn = cylinder(screw_istn_radius, screw_istn_radius)
        screw_sbtn -= cone(screw_istn_radius, 0, screw_istn_radius)
        screw_sbtn = screw_sbtn.up(height - screwStyle.depth)
        result -= screw_sbtn
        cap_height = cap_radius - screw_radius
        result += cone(cap_radius, screw_radius, cap_height)
        sbtn_length = (cap_radius - wall) * sqrt(2)
        sbtn = box(sbtn_length, wall, sbtn_length, center=True)
        sbtn = sbtn.rotateY(pi / 4)
        result -= sbtn
        return result

    def _create_base_sbtn(
            self,
            screwStyle: ScrewStyle,
            screw_radius: float,
            screw_length: float
    ):
        base_sbtn_radius = screw_radius + friction * sqrt(2)
        base_sbtn_length = screw_length + friction * 2
        result = screwStyle.create_shape(base_sbtn_radius, base_sbtn_length-self._tech)
        result = result.up(self._tech)
        base_sbtn_cap_radius = base_sbtn_radius + screwStyle.depth + friction * sqrt(2)
        result += cone(base_sbtn_cap_radius, 0, base_sbtn_cap_radius)
        return result


if __name__ == "__main__":
    style = ScrewStyle()

    mask = halfspace().rotateX(pi / 2)

    wall = 2.4
    screw_radius = wall
    screw_length = wall * 5
    friction = 0.2

    bolt = ScrewBolt(
        screwStyle=style,
        friction=friction,
        screw_radius=screw_radius,
        screw_length=screw_length,
        wall=wall
    )

    disp(bolt.bolt ^ mask, Color(1, 0, 1))

    cap_base = cylinder(bolt.cap_base_radius, wall)
    cap_base -= bolt.cap_sbtn
    disp(cap_base ^ mask, Color(0, 1, 1))

    base = cylinder(bolt.base_radius, bolt.base_length)
    base -= bolt.base_sbtn.rotateZ(3.3)
    base = base.up(wall + friction)
    disp(base ^ mask, Color(1, 1, 0))

    show()
