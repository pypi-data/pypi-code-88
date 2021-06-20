import numpy as np


def hh(t, I_ext):
    # Assume that the time is given in seconds, and convert it to
    # number of milliseconds
    t = 1000 * t
    dt = t[1] - t[0]

    # Conductances and reverse potentials for K, Na, R:
    E = [-12, 115, 10.613]
    g = [36, 120, 0.300]
    x = [0, 0, 1.000]

    # Initialize membrane voltage:
    V = np.zeros(len(t))
    V[0] = -10

    # Initialize currents due to the various ions:
    I = np.zeros((len(t), 3))

    # Alpha and beta variables:
    a = np.zeros(3)
    b = np.zeros(3)

    # Channel activations:
    gnmh = np.zeros((len(t), 3))

    # Perform numerical integration of the ODEs:
    for i in range(1, len(t)):

        a[0] = (10 - V[i - 1]) / (100 * (np.exp((10 - V[i - 1]) / 10) - 1))
        a[1] = (25 - V[i - 1]) / (10 * (np.exp((25 - V[i - 1]) / 10) - 1))
        a[2] = 0.07 * np.exp(-V[i - 1] / 20)

        b[0] = 0.125 * np.exp(-V[i - 1] / 80)
        b[1] = 4 * np.exp(-V[i - 1] / 18)
        b[2] = 1 / (np.exp((30 - V[i - 1]) / 10) + 1)

        tau = 1 / (a + b)
        x0 = a * tau

        x = (1 - dt / tau) * x + dt / tau * x0

        gnmh[i, 0] = g[0] * x[0] ** 4
        gnmh[i, 1] = g[1] * x[1] ** 3 * x[2]
        gnmh[i, 2] = g[2]

        # Update the ionic currents and membrane voltage:
        I[i] = gnmh[i] * (V[i - 1] - E)
        V[i] = V[i - 1] + dt * (I_ext[i] - np.sum(I[i]))

    return V, I


def hhr(t, I_ext):
    # Assume that the time is given in seconds, and convert it to
    # number of milliseconds
    t = 1000 * t
    dt = t[1] - t[0]

    # Conductances and reverse potentials for K, Na, R:
    E = [-12, 115, 10.613]
    g = [36, 120, 0.300]

    # Normalize capacitance to 1 microfarad:
    C = 1

    # Initialize membrane voltage:
    V = np.zeros(len(t))
    V[0] = -10

    # Initialize currents due to the various ions:
    I = np.zeros((len(t), 3))

    # Initialize W:
    W = np.zeros(len(t))

    # Determine the slope S of the Rinzel approximation (see [1]):
    h_0 = 0.07 / (0.07 + 1 / (np.exp(3) + 1))
    n_0 = 0.1 / (np.exp(1) - 1) / (0.1 / (np.exp(1) - 1) + 0.125)
    S = (1 - h_0) / n_0

    # Perform numerical integration of the ODEs:
    for i in range(1, len(t)):

        alpha_n = 0.01 * (10 - V[i - 1]) / (np.exp((10 - V[i - 1]) / 10) - 1)
        alpha_m = 0.1 * (25 - V[i - 1]) / (np.exp((25 - V[i - 1]) / 10) - 1)
        alpha_h = 0.07 * np.exp(-V[i - 1] / 20)

        beta_n = 0.125 * np.exp(-V[i - 1] / 80)
        beta_m = 4 * np.exp(-V[i - 1] / 18)
        beta_h = 1 / (np.exp((30 - V[i - 1]) / 10) + 1)

        n_infty = alpha_n / (alpha_n + beta_n)
        m_infty = alpha_m / (alpha_m + beta_m)
        h_infty = alpha_h / (alpha_h + beta_h)
        W_infty = S / (1 + S ** 2) * (n_infty + S * (1 - h_infty))

        tau_W = 1 + 5 * np.exp(-((V[i - 1] - 10) ** 2) / 55 ** 2)

        # Use exponential Euler numerical integration method to compute W:
        # Recall that for exponential Euler, if dy/dt=a-b*y,
        # y(t_k+1)=y_tk*D + a/b*(1-D), where D=exp(-b*dt)
        a = 3 * W_infty / tau_W
        b = 3 / tau_W
        D = np.exp(-b * dt)
        W[i] = W[i - 1] * D + (a / b) * (1 - D)

        # Update the ionic currents and membrane voltage:
        I[i, 0] = g[0] * (W[i - 1] / S) ** 4 * (V[i - 1] - E[0])
        I[i, 1] = g[1] * m_infty ** 3 * (1 - W[i - 1]) * (V[i - 1] - E[1])
        I[i, 2] = g[2] * (V[i - 1] - E[2])
        V[i] = V[i - 1] + dt / C * (I_ext[i] - np.sum(I[i]))

    return V, W


def hhw(t, I_ext):
    # Assume that the time is given in seconds, and convert it to
    # number of milliseconds
    t = 1000 * t
    dt = t[1] - t[0]
    # Conductances and reverse potentials for Na, K
    E = [55.0, -92.0]
    g = [1.0, 26.0]
    # Time constant for R
    tau_R = 1.9
    # Normalize capacitance to 1 microfarad:
    C = 1.2
    # Initialize membrane voltage:
    V = np.zeros(len(t))
    V[0] = -70.0
    # Initialize currents due to the various ions:
    I = np.zeros((len(t), 2))
    # Initialize W:
    R = np.zeros(len(t))
    R[0] = 0.088

    # Perform numerical integration of the ODEs:
    for i in range(1, len(t)):
        R_infty = 0.0135 * V[i - 1] + 1.03

        # Use exponential Euler numerical integration method to compute W:
        # Recall that for exponential Euler, if dy/dt=a-b*y,
        # y(t_k+1)=y_tk*D + a/b*(1-D), where D=exp(-b*dt)
        a = R_infty / tau_R
        b = 1 / tau_R
        D = np.exp(-b * dt)
        R[i] = R[i - 1] * D + (a / b) * (1 - D)

        # Update the ionic currents and membrane voltage:
        I[i] = (
            g
            * np.array(
                [(17.81 + 0.4771 * V[i - 1] + 0.003263 * V[i - 1] ** 2), R[i - 1]]
            )
            * (V[i - 1] - E)
        )
        V[i] = V[i - 1] + dt / C * (I_ext[i] - np.sum(I[i]))

    return V, R
