from typing import Generator


def iterate(
    x: float, alpha: float, num_iterations: int
) -> Generator[float, None, None]:
    x_prev = x
    for _ in range(num_iterations):
        x = alpha * x_prev * (1 - x_prev)
        yield x
        x_prev = x
