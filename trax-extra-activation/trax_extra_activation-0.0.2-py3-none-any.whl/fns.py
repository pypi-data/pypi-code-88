from trax import fastmath
from trax.fastmath import numpy as jnp
from trax.layers.assert_shape import assert_shape
from trax.layers.base import Fn, PureLayer


@assert_shape("...->...")
def HardShrink(lmbda: float = 0.5) -> PureLayer:
    return Fn(
        "HardShrink", lambda x: jnp.where(x < -lmbda, x, jnp.where(x > lmbda, x, 0))
    )


@assert_shape("...->...")
def HardSwish() -> PureLayer:
    return Fn(
        "HardSwish",
        lambda x: jnp.where(x <= -3, 0, jnp.where(x >= 3, x, x * (x + 3) / 6)),
    )


@assert_shape("...->...")
def LogSigmoid() -> PureLayer:
    return Fn("LogSigmoid", lambda x: jnp.log(1 / (1 + jnp.exp(-x))))


@assert_shape("...->...")
def Relu6() -> PureLayer:
    return Fn("Relu6", lambda x: jnp.clip(x, 0, 6))


@assert_shape("...->...")
def Celu(a: float = 1.0) -> PureLayer:
    return Fn(
        "Celu", lambda x: jnp.maximum(0, x) + jnp.minimum(0, a * jnp.exp(x / a) - 1)
    )


@assert_shape("...->...")
def Silu() -> PureLayer:
    return Fn("Silu", lambda x: x * fastmath.expit(x))


@assert_shape("...->...")
def Mish() -> PureLayer:
    return Fn("Mish", lambda x: x * jnp.tanh(jnp.logaddexp(x, 0.0)))


@assert_shape("...->...")
def SoftShrink(lmbda: float = 0.5) -> PureLayer:
    return Fn(
        "SoftShrink",
        lambda x: jnp.where(x < -lmbda, x + lmbda, jnp.where(x > lmbda, x - lmbda, 0)),
    )


@assert_shape("...->...")
def SoftSign() -> PureLayer:
    return Fn("SoftSign", lambda x: x / (1 + jnp.abs(x)))


@assert_shape("...->...")
def TanhShrink() -> PureLayer:
    return Fn("TanhShrink", lambda x: x - jnp.tanh(x))


@assert_shape("...->...")
def TanhExp() -> PureLayer:
    return Fn("TanhExp", lambda x: x * jnp.tanh(jnp.exp(x)))
