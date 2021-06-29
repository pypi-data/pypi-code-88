# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['manim_physics']

package_data = \
{'': ['*']}

install_requires = \
['manim>=0.6.0', 'pymunk>=6.0.0,<7.0.0']

entry_points = \
{'manim.plugins': ['manim_physics = manim_physics']}

setup_kwargs = {
    'name': 'manim-physics',
    'version': '0.1.1',
    'description': 'Support physics simulation',
    'long_description': '# manim-physics\nA physics simulation plugin based on Pymunk, with this plugin you could generate complicated physics scenes without struggling to use many updaters.\n\nContributed by **pdcxs** and **Matheart**\n\n## Installation\nFollow this guide: https://docs.manim.community/en/stable/installation/plugins.html?highlight=plugin\n\n## A simple Example \n\n```py\nclass TwoObjectsFalling(Scene):\n    def construct(self):\n        space = Space(dt = 1 / self.camera.frame_rate) \n        # space is the basic unit of simulation (just like scene)\n        # you can add rigid bodies, shapes and joints to it \n        # and then step them all forward together through time\n        self.add(space)\n\n        circle = Circle().shift(UP)\n        circle.set_fill(RED, 1)\n        circle.shift(DOWN + RIGHT)\n\n        circle.body = pymunk.Body() # add a rigid body to the circle\n        circle.body.position = \\\n            circle.get_center()[0], \\\n            circle.get_center()[1]\n        circle.shape = pymunk.Circle(\n            body = circle.body,\n            radius = circle.width / 2\n        ) # set the shape of the circle in pymunk\n        circle.shape.elasticity = 0.8\n        circle.shape.density = 1\n        circle.angle = 0\n\n        rect = Square().shift(UP)\n        rect.rotate(PI/4)\n        rect.set_fill(YELLOW_A, 1)\n        rect.shift(UP*2)\n        rect.scale(0.5)\n\n        rect.body = pymunk.Body()\n        rect.body.position = \\\n            rect.get_center()[0], \\\n            rect.get_center()[1]\n        rect.body.angle = PI / 4\n        rect.shape = pymunk.Poly.create_box(rect.body, (1, 1))\n        rect.shape.elasticity = 0.4\n        rect.shape.density = 2\n        rect.shape.friction = 0.8\n        rect.angle = PI / 4\n\n        ground = Rectangle(width = 8, height = 0.1, color = GREEN).set_fill(GREEN, 1)\n        ground.shift(3.5*DOWN)\n        ground.body = space.space.static_body \n        # static body means the object keeps static even after collision\n        ground.shape = pymunk.Segment(ground.body, (-4, -3.5), (4, -3.5), 0.1)\n        ground.shape.elasticity = 0.99\n        ground.shape.friction = 0.8\n        self.add(ground)\n\n        wall1 = Rectangle(width = 0.1, height = 7, color = GREEN).set_fill(GREEN, 1)\n        wall1.shift(3.95*LEFT)\n        wall1.body = space.space.static_body\n        wall1.shape = pymunk.Segment(wall1.body, (-4, -5), (-4, 5), 0.1)\n        wall1.shape.elasticity = 0.99\n        self.add(wall1)\n\n        wall2 = Rectangle(width = 0.1, height = 7, color = GREEN).set_fill(GREEN, 1)\n        wall2.shift(3.95*RIGHT) \n        wall2.body = space.space.static_body\n        wall2.shape = pymunk.Segment(wall2.body, (4, -5), (4, 5), 0.1)\n        wall2.shape.elasticity = 0.99\n        self.add(wall2)\n\n        self.play(\n            DrawBorderThenFill(circle),\n            DrawBorderThenFill(rect))\n        self.wait()\n\n        space.add_body(circle)\n        space.add_body(rect)\n        space.add_body(ground)\n        space.add_body(wall1)\n        space.add_body(wall2)\n\n        space.add_updater(step)\n        circle.add_updater(simulate)\n        rect.add_updater(simulate)\n        self.wait(10)\n        # during wait time, the circle and rect would move according to the simulate updater\n```\n\n## Other beautiful animations based on manim-physics\n',
    'author': 'Matheart',
    'author_email': 'waautomationwong@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
