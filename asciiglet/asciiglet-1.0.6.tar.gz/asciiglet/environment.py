import pyglet

from .transform import Transform
from .vector import Vector


class Environment:
    def __init__(self, max_x=1024, max_y=720, width=1024, height=720):
        self.window = self.create_window(width=width, height=height)

        scale_x = width / max_x
        scale_y = height / max_y

        self.center = Vector.new(max_x * 0.5, max_y * 0.5)
        self.origin = Vector.new(0.0, 0.0)

        self.transform = Transform(scale=Vector.new(scale_x, scale_y))

        self.event_loop = self.create_event_loop()

        self.particles = []

        self.halt_after = -1
        self.iteration = 0

        self.on_update = None

    def create_event_loop(self, *args, **kwargs):
        e = pyglet.app.EventLoop(*args, **kwargs)

        @e.event
        def on_window_close(window):
            if window == self.window:
                e.exit()
                return pyglet.event.EVENT_HANDLED

        return e

    def create_window(self, *args, **kwargs):
        w = pyglet.window.Window(*args, **kwargs)

        @w.event
        def on_draw():
            self.draw(w)

        return w

    def run(self, halt_after=-1, on_update=None):
        """
        while True:
            dt = pyglet.clock.tick()

            for window in pyglet.app.windows:
                window.switch_to()
                window.dispatch_events()
                window.dispatch_event('on_draw')
                window.flip()

            for particle in self.particles:
                particle.update(dt)
        """
        def u(dt, interval):
            self.iteration += 1
            if self.halt_after > 0 and self.iteration > self.halt_after:
                print("HALTING")
                self.window.close()
                self.event_loop.exit()
                pyglet.clock.unschedule(u)
                return

            self.update(dt)

        self.halt_after = halt_after

        self.on_update = on_update

        pyglet.clock.schedule(u, .05)
        pyglet.app.run()

    def update(self, dt):
        if self.on_update is not None:
            self.on_update(self, dt)

        for particle in self.particles:
            particle.update(self, dt)
            if particle.destroying:
                self.particles.remove(particle)

    def draw(self, window):
        window.clear()
        pyglet.gl.glLoadIdentity()

        for particle in self.particles:
            particle.draw(self, self.iteration)
