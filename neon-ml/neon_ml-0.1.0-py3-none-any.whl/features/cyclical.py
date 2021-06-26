import numpy as np


def cyclical_encoding_sin(x: np.ndarray, max_cycle: float) -> np.ndarray:
    """Apply cyclical transformation to numerical values.
    Args:
        x (np.ndarray): Array of numerical values to transform.
        max_cycle (float): Maximum value of the cyclical values.
    Returns:
        np.ndarray: Cyclically encoded values.
    """
    return np.sin(2 * np.pi * x / max_cycle)


def cyclical_encoding_cos(x: np.ndarray, max_cycle: float) -> np.ndarray:
    """Apply cyclical transformation to numerical values.
    Args:
        x (np.ndarray): Array of numerical values to transform.
        max_cycle (float): Maximum value of the cyclical values.
    Returns:
        np.ndarray: Cyclically encoded values.
    """
    return np.cos(2 * np.pi * x / max_cycle)
