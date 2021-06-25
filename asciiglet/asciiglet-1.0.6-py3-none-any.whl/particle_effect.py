import math

import numpy as np

from .abstract_object import AbstractObject
from .vector import Vector
from .emitter import Emitter


class ParticleEffect(AbstractObject):
    def __init__(self):
        super().__init__()
        self._particle = None

        self._velocity = Vector.new(0, 0)
        self._acceleration = Vector.new(0.0, 0.0)

        self._rotation = 0
        self._rotation_acceleration = 0

    def __destroy__(self):
        self._particle = None
        super().__destroy__()

    @property
    def particle(self):
        return self._particle

    @particle.setter
    def particle(self, value):
        self._particle = value

    @property
    def velocity(self):
        return self._velocity

    @velocity.setter
    def velocity(self, value):
        self._velocity = value

    @property
    def acceleration(self):
        return self._acceleration

    @acceleration.setter
    def acceleration(self, value):
        self._acceleration = value

    @property
    def rotation(self):
        return self._rotation

    @rotation.setter
    def rotation(self, value):
        self._rotation = value

    @property
    def rotation_acceleration(self):
        return self._rotation_acceleration

    @rotation_acceleration.setter
    def rotation_acceleration(self, value):
        self._rotation_acceleration = value

    def apply(self, particle, environment, dt):
        pass


class GravityPE(ParticleEffect):
    bodies = []

    def __init__(self, weight=1.0):
        super().__init__()
        self.weight = weight
        GravityPE.bodies.append(self)

    def __destroy__(self):
        GravityPE.bodies.remove(self)
        super().__destroy__()

    def apply(self, particle, environment, dt):
        self.acceleration = np.array([0.0, 0.0])

        for g in GravityPE.bodies:
            dpos = g.particle.transform.pos - particle.transform.pos
            if dpos[0] == 0 and dpos[1] == 0:
                continue

            distance_squared = Vector.magnitude(dpos)
            attr = g.weight / distance_squared

            self.acceleration += dpos * attr * dt


class ChargedPE(ParticleEffect):
    bodies = []

    def __init__(self, weight=1.0, charges={}):
        super().__init__()
        self.weight = weight
        self.charges = charges

        ChargedPE.bodies.append(self)

    def __destroy__(self):
        ChargedPE.bodies.remove(self)
        super().__destroy__()

    def apply(self, particle, environment, dt):
        self.acceleration = np.array([0.0, 0.0])

        for c in ChargedPE.bodies:
            dpos = c.particle.transform.pos - particle.transform.pos
            if dpos[0] == 0 and dpos[1] == 0:
                continue

            distance_squared = Vector.magnitude(dpos)
            attr = 0
            for field, q1 in self.charges.items():
                q2 = 0
                if field in c.charges.keys():
                    q2 = c.charges[field]

                attr += -(q1 * q2) / (distance_squared * self.weight)

            self.acceleration += dpos * attr * dt


class DissipatePE(ParticleEffect):
    def __init__(
        self,
        sprites="@ao*.",
        amount=None,
        max_amount=1,
        loss=0.0,
        loss_perc=0.0
    ):
        super().__init__()

        self.sprites = sprites

        if amount is None:
            amount = max_amount

        self.amount = amount
        self.max_amount = max_amount

        self.loss = loss
        self.loss_perc = loss_perc

    def apply(self, particle, environment, dt):
        self.amount -= self.loss * dt
        self.amount -= self.amount * self.loss_perc * dt

        if self.amount <= 0.0:
            particle.destroy()
            return

        perc_left = self.amount / self.max_amount

        symbol_pos = len(self.sprites) - math.ceil(
            len(self.sprites) * perc_left
        )

        sprite_symbol = self.sprites[symbol_pos]

        particle.sprite.set_sprite(sprite_symbol)


class EmitPE(ParticleEffect):
    def __init__(self, particles):
        super().__init__()
        self.particles = particles

    def apply(self, particle, environment, dt):
        for particle in self.particles(self):
            environment.particles.append(particle)


class SpawnEmitterPE(ParticleEffect):
    def __init__(
        self,
        particles,
        cooldown=1,
        to_live=-1
    ):
        super().__init__()
        self.particles = particles

        self.cooldown = cooldown
        self.to_live = to_live

    def apply(self, particle, environment, dt):
        t = particle.transform.copy()
        e = Emitter(
            transform=t,
            particles=self.particles,
            cooldown=self.cooldown,
            to_live=self.to_live
        )
        environment.particles.append(e)


class PEWrapper(ParticleEffect):
    def __init__(self, effect):
        self.effect = effect
        super().__init__()

    def __destroy__(self):
        self.effect = None
        super().__destroy__()

    @ParticleEffect.particle.setter
    def particle(self, value):
        self._particle = value
        self.effect.particle = value

    @ParticleEffect.velocity.getter
    def velocity(self):
        return self.effect.velocity

    @ParticleEffect.acceleration.getter
    def acceleration(self):
        return self.effect.acceleration

    @ParticleEffect.rotation.getter
    def rotation(self):
        return self.effect.rotation

    @ParticleEffect.rotation_acceleration.getter
    def rotation_acceleration(self):
        return self.effect.rotation_acceleration


class TimedPE(PEWrapper):
    """
    Adds an *effect* after *time*.
    """

    def __init__(
        self,
        effect,
        time=1.0,
    ):
        super().__init__(effect)
        self.time = time

    def apply(self, particle, environment, dt):
        self.time -= dt
        if self.time < 0:
            particle.add_effect(self.effect)
            self.destroy()


class LastingPE(PEWrapper):
    """
    Trigger *effect* each tick, delete after *time*.

    If refresh_after is not None, whenever time runs out,
    effect will wait for refresh_after seconds, until starting again.
    Otherwise the effect is deleted upon running out of time.
    """

    def __init__(
        self,
        effect,
        time=None,
        max_time=1.0,
        refresh_after=None,
    ):
        super().__init__(effect)

        if time is None:
            time = max_time

        self.time = time
        self.max_time = max_time
        self.refresh_after = refresh_after
        self.max_refresh_after = refresh_after

    def __destroy__(self):
        self.effect.destroy()
        super().__destroy__()

    @ParticleEffect.particle.setter
    def particle(self, value):
        self._particle = value
        self.effect.particle = value

    def apply(self, particle, environment, dt):
        if self.time >= 0:
            self.effect.apply(particle, environment, dt)

            self.time -= dt

        if self.time < 0:
            if self.refresh_after is None:
                self.destroy()
                return

            self.refresh_after -= dt
            if self.refresh_after <= 0:
                self.refresh_after = self.max_refresh_after
                self.effect.apply(particle, environment, dt)
                self.time = self.max_time


class CooldownPE(PEWrapper):
    """
    Trigger *effect* every *time* seconds.
    """

    def __init__(
        self,
        effect,
        time=None,
        max_time=1.0,
    ):
        super().__init__(effect)

        if time is None:
            time = max_time

        self.time = time
        self.max_time = max_time

    def __destroy__(self):
        self.effect.destroy()
        super().__destroy__()

    def apply(self, particle, environment, dt):
        self.time -= dt
        if self.time < 0:
            self.effect.apply(particle, environment, dt)
            self.time = self.max_time


class FaceMovementPE(ParticleEffect):
    """
    Changes angle to face velocity.
    """

    def __init__(self, turn_speed=1.0):
        super().__init__()

        self.turn_speed = turn_speed

    def apply(self, particle, environment, dt):
        vel = particle.m_velocity

        if vel[0] != 0 or vel[1] != 0:
            angle = Vector.angleRotateTo(
                particle.transform.forward(), vel
            )

            # * 0.5 since we need the self.turn_speed window on both sides.
            if abs(angle) < self.turn_speed * dt * 0.5:
                particle.transform.angle += angle
                self.rotation = 0
                return

            self.rotation = angle * self.turn_speed * dt


class ForwardMovementPE(ParticleEffect):
    """
    Applied acceleration in the forward direction.
    """

    def __init__(self, forward_velocity=0.0, forward_acceleration=0.0):
        super().__init__()

        self.forward_velocity = forward_velocity
        self.forward_acceleration = forward_acceleration

    def apply(self, particle, environment, dt):
        self.velocity = particle.transform.forward() * self.forward_velocity
        self.acceleration = (
            particle.transform.forward() * self.forward_acceleration
        )


class FaceTransformPE(ParticleEffect):
    """
    Force to constantly face transform.
    """

    def __init__(self, transform, turn_speed=1.0):
        super().__init__()

        self.transform = transform
        self.turn_speed = turn_speed

    def apply(self, particle, environment, dt):
        target = self.transform.pos

        pos = particle.transform.pos

        if target[0] == pos[0] and target[1] == pos[1]:
            return

        angle = Vector.angleRotateTo(
            particle.transform.forward(), target - pos
        )

        # * 0.5 since we need the self.turn_speed window on both sides.
        if abs(angle) < self.turn_speed * dt * 0.5:
            particle.transform.angle += angle
            self.rotation = 0
            return

        self.rotation = angle * self.turn_speed * dt


class OnDestroyPE(PEWrapper):
    """
    Issues *effect* when particle is destroyed.
    """

    def __init__(
        self,
        effect,
    ):
        super().__init__(effect)
        self.dt = 0
        self.environment = None

    def __destroy__(self):
        self.effect.apply(self.particle, self.environment, self.dt)
        self.effect.destroy()
        self.environment = None
        super().__destroy__()

    def apply(self, particle, environment, dt):
        self.dt = dt
        self.environment = environment


class BoidPE(ParticleEffect):
    """
    Implementation of Boids.
    """
    boids = []

    def __init__(
        self,
        min_speed=20.0,
        max_speed=100.0,
        max_force=1000.0,
        limit_acceleration=40.0,
        perception=120.0,
        personal_space=30.0,
        introversion=1.5,
        propensity=40.0,
        bond=0.01,
        commitment=10.0,
        elusion=10.0,
        collision_space=10.0,
        attractors=[],
        colliders=[],
        on_collide=None,
    ):
        super().__init__()
        self.min_speed = min_speed
        self.max_speed = max_speed
        self.max_force = max_force

        self.limit_acceleration = limit_acceleration

        self.perception = perception
        self.personal_space = personal_space

        self.introversion = introversion
        self.propensity = propensity
        self.bond = bond

        self.commitment = commitment
        self.elusion = elusion

        self.collision_space = collision_space

        self.attractors = attractors
        self.colliders = colliders

        BoidPE.boids.append(self)

    def __destroy__(self):
        BoidPE.boids.remove(self)
        super().__destroy__()

    def apply(self, particle, environment, dt):
        self.acceleration = 0.0
        steering = Vector.new(0.0, 0.0)

        neighbors = self.get_seen(particle, BoidPE.boids)
        if len(neighbors) > 0:
            seperation = self.seperation(particle, neighbors)
            alignment = self.alignment(particle, neighbors)
            cohesion = self.cohesion(particle, neighbors)

            steering = seperation + alignment + cohesion

        colliders = self.get_seen(particle, self.colliders)
        if len(colliders) > 0:
            avoidance = self.avoidance(particle, self.colliders)

            steering += avoidance

        attractors = self.get_seen(particle, self.attractors)
        if len(attractors) > 0:
            attraction = self.attraction(particle, self.attractors)

            steering += attraction

        velocity = particle.velocity
        if velocity[0] == 0.0 and velocity[1] == 0.0:
            velocity = particle.transform.forward()

        speed = Vector.magnitude(particle.velocity)
        if speed < self.min_speed:
            self.acceleration += (
                Vector.scale_to_length(velocity, self.min_speed)
            ) * self.limit_acceleration * dt

        elif speed > self.max_speed:
            self.acceleration -= (
                Vector.scale_to_length(velocity, self.max_speed)
            ) * self.limit_acceleration * dt

        self.acceleration += steering * dt

    def get_seen(self, particle, particles):
        seen = []

        for other in particles:
            if particle == other:
                continue

            dist = Vector.magnitude(
                other.particle.transform.pos - particle.transform.pos
            )
            if dist < self.perception:
                seen.append(other)

        return seen

    def clamp_force(self, force):
        if 0 < Vector.magnitude(force) > self.max_force:
            force = Vector.scale_to_length(force, self.max_force)

        return force

    def seperation(self, particle, boids):
        steering = Vector.new(0.0, 0.0)

        for boid in boids:
            dist = Vector.magnitude(
                boid.particle.transform.pos - particle.transform.pos
            )
            if dist < self.personal_space:
                steering -= (
                    boid.particle.transform.pos - particle.transform.pos
                )

        return self.clamp_force(steering * self.introversion)

    def alignment(self, particle, boids):
        steering = Vector.new(0.0, 0.0)

        for boid in boids:
            steering += boid.particle.velocity

        steering /= len(BoidPE.boids)
        steering -= particle.velocity

        return self.clamp_force(steering * self.propensity)

    def cohesion(self, particle, boids):
        steering = Vector.new(0.0, 0.0)

        for boid in boids:
            steering += boid.particle.transform.pos

        steering /= len(BoidPE.boids)
        steering -= particle.transform.pos

        return self.clamp_force(steering * self.bond)

    def attraction(self, particle, attractors):
        steering = Vector.new(0.0, 0.0)

        closest = None
        closest_dist = -1.0

        for attr in attractors:
            dist = Vector.magnitude(
                attr.particle.transform.pos - particle.transform.pos
            )

            if closest is None or dist < closest_dist:
                closest = attr
                closest_dist = dist

        steering += (
            closest.particle.transform.pos - particle.transform.pos
        )

        return self.clamp_force(steering * self.commitment)

    def avoidance(self, particle, colliders):
        steering = Vector.new(0.0, 0.0)

        for col in colliders:
            dist = Vector.magnitude(
                col.particle.transform.pos - particle.transform.pos
            )
            if dist < self.collision_space:
                steering -= (
                    col.particle.transform.pos - particle.transform.pos
                )

        return self.clamp_force(steering * self.elusion)


"""
    TO-DO:
        Generalize these two to work with both speed and rotation.
"""


class ChangingRotationPE(ParticleEffect):
    def __init__(self, limit_speed=1.0):
        super().__init__()
        self.limit_speed = limit_speed

    def apply(self, particle, environment, dt):
        if abs(particle.rotation) > self.limit_speed:
            particle.rotation_acceleration *= -1


class DecelerationPE(ParticleEffect):
    def __init__(self, limit_speed=1.0, deceleration=2.0, smooth=None):
        super().__init__()
        self.limit_speed = limit_speed
        self.deceleration = deceleration
        self.smooth = smooth

    def apply(self, particle, environment, dt):
        speed = Vector.magnitude(particle.m_velocity)

        if speed > self.limit_speed:
            if self.smooth is not None:
                self.acceleration = self.smooth(
                    self.limit_speed, self.deceleration, speed
                )
            else:
                self.acceleration = -(
                    particle.velocity * self.deceleration
                ) * dt

            if speed < self.deceleration:
                particle.velocity = Vector.new(0.0, 0.0)
