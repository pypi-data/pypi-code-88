import numpy as np
import scipy.sparse as sp

from ..constants import EPSILON_0, ETA_0

def compute_derivative_matrices(omega, shape, npml, mesh_step):
    """Construct sparse matrices applying finite-difference derivatives in 2D.

    Parameters
    ----------
    omega : float
        (Hertz) Angular frequency.
    shape : tuple of int
        Size (Nx, Ny) of the 2D domain.
    npml : tuple of int
        Number of PML layers in x and y.
    mesh_step : tuple of float
        (micron) Mesh step in x and y.
    
    Returns
    -------
    scipy.sparse matrix
        Matrices implementing the forward and backward derivatives along x and 
        y, respectively.
    """

    dx, dy = mesh_step

    # Construct derivate matrices without PML.
    Dxf = createDws('x', 'f', shape, dx)
    Dxb = createDws('x', 'b', shape, dx)
    Dyf = createDws('y', 'f', shape, dy)
    Dyb = createDws('y', 'b', shape, dy)

    # Make the S-matrices for PML.
    (Sxf, Sxb, Syf, Syb) = create_S_matrices(omega, shape, npml, mesh_step)

    # Apply PML to derivative matrices.
    Dxf = Sxf.dot(Dxf)
    Dxb = Sxb.dot(Dxb)
    Dyf = Syf.dot(Dyf)
    Dyb = Syb.dot(Dyb)

    return Dxf, Dxb, Dyf, Dyb

def createDws(component, direction, shape, dL):
    """Derivative matrices without PML.
    
    Parameters
    ----------
    component : str
        One of {'x', 'y'}.
    direction : str
        One of {'f', 'b'}.
    shape : tuple of int
        Size (Nx, Ny) of the 2D domain.
    dL : float
        Mesh step in the specified direction.
    """

    Nx, Ny = shape

    # special case, a 1D problem
    if component == 'x' and Nx == 1:
        return sp.csr_matrix((Ny, Ny))
    if component == 'y' and Ny == 1:
        return sp.csr_matrix((Nx, Nx))

    # select a `make_D` function based on the component and direction
    component_dir = component + direction
    if component_dir == 'xf':
        return make_Dxf(dL, shape)
    elif component_dir == 'xb':
        return make_Dxb(dL, shape)
    elif component_dir == 'yf':
        return make_Dyf(dL, shape)
    elif component_dir == 'yb':
        return make_Dyb(dL, shape)
    else:
        raise ValueError("Component %s and/or direction %s not recognized."%(
                            component, direction))

def make_Dxf(dL, shape):
    """ Forward derivative in x. """
    Nx, Ny = shape
    Dxf = sp.diags([-1, 1, 1], [0, 1, -Nx+1], shape=(Nx, Nx))
    Dxf = 1 / dL * sp.kron(Dxf, sp.eye(Ny))
    return Dxf

def make_Dxb(dL, shape):
    """ Backward derivative in x. """
    Nx, Ny = shape
    Dxb = sp.diags([1, -1, -1], [0, -1, Nx-1], shape=(Nx, Nx))
    Dxb = 1 / dL * sp.kron(Dxb, sp.eye(Ny))
    return Dxb

def make_Dyf(dL, shape):
    """ Forward derivative in y. """
    Nx, Ny = shape
    Dyf = sp.diags([-1, 1, 1], [0, 1, -Ny+1], shape=(Ny, Ny))
    Dyf = 1 / dL * sp.kron(sp.eye(Nx), Dyf)
    return Dyf

def make_Dyb(dL, shape):
    """ Backward derivative in y. """
    Nx, Ny = shape
    Dyb = sp.diags([1, -1, -1], [0, -1, Ny-1], shape=(Ny, Ny))
    Dyb = 1 / dL * sp.kron(sp.eye(Nx), Dyb)
    return Dyb

def create_S_matrices(omega, shape, npml, mesh_step):
    """Makes the 'S-matrices'. When dotted with derivative matrices, they add 
    PML. """

    # strip out some information needed
    Nx, Ny = shape
    dx, dy = mesh_step
    N = Nx * Ny
    x_range = [0, float(dx * Nx)]
    y_range = [0, float(dy * Ny)]
    Nx_pml, Ny_pml = npml    

    # Create the sfactor in each direction and for 'f' and 'b'
    s_vector_x_f = create_sfactor('f', omega, dx, Nx, Nx_pml)
    s_vector_x_b = create_sfactor('b', omega, dx, Nx, Nx_pml)
    s_vector_y_f = create_sfactor('f', omega, dy, Ny, Ny_pml)
    s_vector_y_b = create_sfactor('b', omega, dy, Ny, Ny_pml)

    # Fill the 2D space with layers of appropriate s-factors
    Sx_f_2D = np.zeros(shape, dtype=np.complex128)
    Sx_b_2D = np.zeros(shape, dtype=np.complex128)
    Sy_f_2D = np.zeros(shape, dtype=np.complex128)
    Sy_b_2D = np.zeros(shape, dtype=np.complex128)

    # Insert the cross sections into the S-grids (could be done more elegantly)
    for i in range(0, Ny):
        Sx_f_2D[:, i] = 1 / s_vector_x_f
        Sx_b_2D[:, i] = 1 / s_vector_x_b
    for i in range(0, Nx):
        Sy_f_2D[i, :] = 1 / s_vector_y_f
        Sy_b_2D[i, :] = 1 / s_vector_y_b

    # Reshape the 2D s-factors into a 1D s-vecay
    Sx_f_vec = Sx_f_2D.flatten()
    Sx_b_vec = Sx_b_2D.flatten()
    Sy_f_vec = Sy_f_2D.flatten()
    Sy_b_vec = Sy_b_2D.flatten()

    # Construct the 1D total s-vector into a diagonal matrix
    Sx_f = sp.spdiags(Sx_f_vec, 0, N, N)
    Sx_b = sp.spdiags(Sx_b_vec, 0, N, N)
    Sy_f = sp.spdiags(Sy_f_vec, 0, N, N)
    Sy_b = sp.spdiags(Sy_b_vec, 0, N, N)

    return Sx_f, Sx_b, Sy_f, Sy_b

def create_sfactor(direction, omega, dL, N, N_pml):
    """ Creates the S-factor cross section needed in the S-matrices """

    # For no PNL, this should just be identity matrix.
    if N_pml == 0:
        return np.ones(N, dtype=np.complex128)

    # Otherwise, get different profiles for forward and reverse derivatives.
    if direction == 'f':
        return create_sfactor_f(omega, dL, N, N_pml)
    elif direction == 'b':
        return create_sfactor_b(omega, dL, N, N_pml)
    else:
        raise ValueError("Direction value {} not recognized".format(direction))

def create_sfactor_f(omega, dL, N, N_pml):
    """ S-factor profile for forward derivative matrix """
    sfactor_array = np.ones(N, dtype=np.complex128)
    for i in range(N):
        if i <= N_pml:
            sfactor_array[i] = s_value(dL, (N_pml - i + 0.5)/N_pml, omega)
        elif i > N - N_pml:
            sfactor_array[i] = s_value(dL, (i - (N - N_pml) - 0.5)/N_pml, omega)
    return sfactor_array

def create_sfactor_b(omega, dL, N, N_pml):
    """ S-factor profile for backward derivative matrix """
    sfactor_array = np.ones(N, dtype=np.complex128)
    for i in range(N):
        if i <= N_pml:
            sfactor_array[i] = s_value(dL, (N_pml - i + 1)/N_pml, omega)
        elif i > N - N_pml:
            sfactor_array[i] = s_value(dL, (i - (N - N_pml) - 1)/N_pml, omega)
    return sfactor_array

def sig_w(dL, step, sorder=3):
    """ Fictional conductivity, note that these values might need tuning """
    sig_max = 0.8 * (sorder + 1) / (ETA_0 * dL)
    return sig_max * step**sorder

def s_value(dL, step, omega):
    """ S-value to use in the S-matrices """
    # print(step)
    return 1 - 1j * sig_w(dL, step) / (omega * EPSILON_0)