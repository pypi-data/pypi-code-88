#!/usr/bin/env python3
# coding: utf-8

from math import *
from zencad import *


def spring(
        segments_count,
        wall,
        height,
        width,
        segment_length
):
    def create_segment():
        main_length = segment_length / 2 + wall
        main_width = width / 2 - main_length / 2
        result = box(main_width, main_length, height)
        result += cylinder(main_length / 2, height).right(main_width).forw(main_length / 2)
        result -= box(main_width * 2, main_length - wall * 2, height).forw(wall).left(main_width)
        result -= cylinder(main_length / 2 - wall, height).right(main_width).forw(main_length / 2)
        result += result.rotateZ(pi).forw(segment_length + wall)
        result = unify(result)
        return result

    segment = create_segment()
    result = union(
        [segment.forw(i * segment_length)
         for i in range(segments_count)]
    )
    tail = box(width / 2, wall, height)
    result += tail.left(width / 2)
    result += tail.forw(segments_count * segment_length)
    return result


if __name__ == "__main__":
    
    wall=2.4
    result = spring(
        segments_count=5,
        wall=wall,
        height=wall * 2,
        width=wall * 8,
        segment_length=wall * 4
    )

    disp(result)

    show()
