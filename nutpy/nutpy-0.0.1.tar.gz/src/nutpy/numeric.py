import numpy as np
import cmath


def Rint(t1,alpha,beta,delta,Omega,omega):

    x = lambda t: (np.cos(Omega*t)*(np.sin(beta)*np.sin(omega*t))
                  + np.sin(Omega*t)*(np.cos(alpha)*np.sin(beta)*np.cos(omega*t)
                  + np.sin(alpha)*np.cos(beta)))

    y = lambda t: (np.cos(alpha)*np.cos(beta)
                  - np.sin(alpha)*np.sin(beta)*np.cos(omega*t))

    z = lambda t: (- np.sin(Omega*t)*(np.sin(beta)*np.sin(omega*t))
                  + np.cos(Omega*t)*(np.cos(alpha)*np.sin(beta)*np.cos(omega*t)
                  + np.sin(alpha)*np.cos(beta)))

    dx = lambda t: (- np.sin(Omega*t)*Omega*np.sin(beta)*np.sin(omega*t)
                   + np.cos(Omega*t)*(np.sin(beta)*np.cos(omega*t))*omega
                   + np.cos(Omega*t)*Omega*np.cos(alpha)*np.sin(beta)*np.cos(omega*t)
                   - np.sin(Omega*t)*np.cos(alpha)*np.sin(beta)*np.sin(omega*t)*omega
                   + np.cos(Omega*t)*Omega*np.sin(alpha)*np.cos(beta))

    dy = lambda t: np.sin(alpha)*np.sin(beta)*np.sin(omega*t)*omega

    dz = lambda t: (- np.cos(Omega*t)*Omega*(np.sin(beta)*np.sin(omega*t))
                   - np.sin(Omega*t)*(np.sin(beta)*np.cos(omega*t))*omega
                   - np.sin(Omega*t)*Omega*np.cos(alpha)*np.sin(beta)*np.cos(omega*t)
                   - np.cos(Omega*t)*np.cos(alpha)*np.sin(beta)*np.sin(omega*t)*omega
                   - np.sin(Omega*t)*Omega*np.sin(alpha)*np.cos(beta))

    dx_1 = dx(t1)/np.sqrt((dx(t1))**2+(dy(t1))**2+(dz(t1))**2)
    # dy_1 = dy(t1)/np.sqrt((dx(t1))**2+(dy(t1))**2+(dz(t1))**2)
    dz_1 = dz(t1)/np.sqrt((dx(t1))**2+(dy(t1))**2+(dz(t1))**2)
    
    # nx = y(t1)*dz_1-z(t1)*dy_1
    ny = -x(t1)*dz_1+z(t1)*dx_1
    # nz = x(t1)*dy_1-y(t1)*dx_1

    # xi_1 = x(t1)*np.cos(delta)-nx*np.sin(delta)
    yi_1 = y(t1)*np.cos(delta)-ny*np.sin(delta)
    # zi_1 = z(t1)*np.cos(delta)-nz*np.sin(delta)

    R = np.arccos(yi_1)

    return R

def Rext(t1,alpha,beta,delta,Omega,omega):

    x = lambda t: (np.cos(Omega*t)*(np.sin(beta)*np.sin(omega*t))
                  + np.sin(Omega*t)*(np.cos(alpha)*np.sin(beta)*np.cos(omega*t)
                  + np.sin(alpha)*np.cos(beta)))

    y = lambda t: (np.cos(alpha)*np.cos(beta)
                  - np.sin(alpha)*np.sin(beta)*np.cos(omega*t))

    z = lambda t: (- np.sin(Omega*t)*(np.sin(beta)*np.sin(omega*t))
                  + np.cos(Omega*t)*(np.cos(alpha)*np.sin(beta)*np.cos(omega*t)
                  + np.sin(alpha)*np.cos(beta)))

    dx = lambda t: (- np.sin(Omega*t)*Omega*np.sin(beta)*np.sin(omega*t)
                   + np.cos(Omega*t)*(np.sin(beta)*np.cos(omega*t))*omega
                   + np.cos(Omega*t)*Omega*np.cos(alpha)*np.sin(beta)*np.cos(omega*t)
                   - np.sin(Omega*t)*np.cos(alpha)*np.sin(beta)*np.sin(omega*t)*omega
                   + np.cos(Omega*t)*Omega*np.sin(alpha)*np.cos(beta))

    dy = lambda t: np.sin(alpha)*np.sin(beta)*np.sin(omega*t)*omega

    dz = lambda t: (- np.cos(Omega*t)*Omega*(np.sin(beta)*np.sin(omega*t))
                   - np.sin(Omega*t)*(np.sin(beta)*np.cos(omega*t))*omega
                   - np.sin(Omega*t)*Omega*np.cos(alpha)*np.sin(beta)*np.cos(omega*t)
                   - np.cos(Omega*t)*np.cos(alpha)*np.sin(beta)*np.sin(omega*t)*omega
                   - np.sin(Omega*t)*Omega*np.sin(alpha)*np.cos(beta))

    dx_1 = dx(t1)/np.sqrt((dx(t1))**2+(dy(t1))**2+(dz(t1))**2)
    # dy_1 = dy(t1)/np.sqrt((dx(t1))**2+(dy(t1))**2+(dz(t1))**2)
    dz_1 = dz(t1)/np.sqrt((dx(t1))**2+(dy(t1))**2+(dz(t1))**2)

    # nx = y(t1)*dz_1-z(t1)*dy_1
    ny = -x(t1)*dz_1+z(t1)*dx_1
    # nz = x(t1)*dy_1-y(t1)*dx_1

    # xe_1 = x(t1)*np.cos(delta)+nx*np.sin(delta)
    ye_1 = y(t1)*np.cos(delta)+ny*np.sin(delta)
    # ze_1 = z(t1)*np.cos(delta)+nz*np.sin(delta)

    R = np.arccos(ye_1)

    return R

def Thetaext(t1, alpha, beta, delta, Omega, omega):

    x = lambda t: (np.cos(Omega*t)*(np.sin(beta)*np.sin(omega*t))
                  + np.sin(Omega*t)*(np.cos(alpha)*np.sin(beta)*np.cos(omega*t)
                  + np.sin(alpha)*np.cos(beta)))

    y = lambda t: np.cos(alpha)*np.cos(beta)-np.sin(alpha)*np.sin(beta)*np.cos(omega*t)

    z = lambda t: (- np.sin(Omega*t)*(np.sin(beta)*np.sin(omega*t))
                  + np.cos(Omega*t)*(np.cos(alpha)*np.sin(beta)*np.cos(omega*t)
                  + np.sin(alpha)*np.cos(beta)))  

    dx = lambda t: (- np.sin(Omega*t)*Omega*np.sin(beta)*np.sin(omega*t)
                   + np.cos(Omega*t)*(np.sin(beta)*np.cos(omega*t))*omega
                   + np.cos(Omega*t)*Omega*np.cos(alpha)*np.sin(beta)*np.cos(omega*t)
                   - np.sin(Omega*t)*np.cos(alpha)*np.sin(beta)*np.sin(omega*t)*omega
                   + np.cos(Omega*t)*Omega*np.sin(alpha)*np.cos(beta))

    dy = lambda t: np.sin(alpha)*np.sin(beta)*np.sin(omega*t)*omega

    dz = lambda t: (- np.cos(Omega*t)*Omega*(np.sin(beta)*np.sin(omega*t))
                   - np.sin(Omega*t)*(np.sin(beta)*np.cos(omega*t))*omega
                   - np.sin(Omega*t)*Omega*np.cos(alpha)*np.sin(beta)*np.cos(omega*t)
                   - np.cos(Omega*t)*np.cos(alpha)*np.sin(beta)*np.sin(omega*t)*omega
                   - np.sin(Omega*t)*Omega*np.sin(alpha)*np.cos(beta))

    dx_1 = dx(t1)/np.sqrt((dx(t1))**2+(dy(t1))**2+(dz(t1))**2)
    dy_1 = dy(t1)/np.sqrt((dx(t1))**2+(dy(t1))**2+(dz(t1))**2)
    dz_1 = dz(t1)/np.sqrt((dx(t1))**2+(dy(t1))**2+(dz(t1))**2)

    nx = y(t1)*dz_1-z(t1)*dy_1
    ny = -x(t1)*dz_1+z(t1)*dx_1
    nz = x(t1)*dy_1-y(t1)*dx_1
    
    xe_1 = x(t1)*np.cos(delta)+nx*np.sin(delta)
    ye_1 = y(t1)*np.cos(delta)+ny*np.sin(delta)
    ze_1 = z(t1)*np.cos(delta)+nz*np.sin(delta)

    R = np.arccos(ye_1)
    
    #REVISE AND ADAPT
    if np.sign(xe_1)>=0:
        Theta = np.real(cmath.acos(ze_1/np.sin(R)))
    else:
        Theta = 2*np.pi-np.real(cmath.acos(ze_1/np.sin(R)))

    return Theta


def Thetaint(t1, alpha, beta, delta, Omega, omega):
    
    x = lambda t: (np.cos(Omega*t)*(np.sin(beta)*np.sin(omega*t))
                  + np.sin(Omega*t)*(np.cos(alpha)*np.sin(beta)*np.cos(omega*t)
                  + np.sin(alpha)*np.cos(beta)))

    y = lambda t: (np.cos(alpha)*np.cos(beta)
                  - np.sin(alpha)*np.sin(beta)*np.cos(omega*t))

    z = lambda t: (- np.sin(Omega*t)*(np.sin(beta)*np.sin(omega*t))
                  + np.cos(Omega*t)*(np.cos(alpha)*np.sin(beta)*np.cos(omega*t)
                  + np.sin(alpha)*np.cos(beta)))

    dx = lambda t: (- np.sin(Omega*t)*Omega*np.sin(beta)*np.sin(omega*t)
                   + np.cos(Omega*t)*(np.sin(beta)*np.cos(omega*t))*omega
                   + np.cos(Omega*t)*Omega*np.cos(alpha)*np.sin(beta)*np.cos(omega*t)
                   - np.sin(Omega*t)*np.cos(alpha)*np.sin(beta)*np.sin(omega*t)*omega
                   + np.cos(Omega*t)*Omega*np.sin(alpha)*np.cos(beta))

    dy = lambda t: np.sin(alpha)*np.sin(beta)*np.sin(omega*t)*omega

    dz = lambda t: (- np.cos(Omega*t)*Omega*(np.sin(beta)*np.sin(omega*t))
                   - np.sin(Omega*t)*(np.sin(beta)*np.cos(omega*t))*omega
                   - np.sin(Omega*t)*Omega*np.cos(alpha)*np.sin(beta)*np.cos(omega*t)
                   - np.cos(Omega*t)*np.cos(alpha)*np.sin(beta)*np.sin(omega*t)*omega
                   - np.sin(Omega*t)*Omega*np.sin(alpha)*np.cos(beta))

    dx_1 = dx(t1)/np.sqrt((dx(t1))**2+(dy(t1))**2+(dz(t1))**2)
    dy_1 = dy(t1)/np.sqrt((dx(t1))**2+(dy(t1))**2+(dz(t1))**2)
    dz_1 = dz(t1)/np.sqrt((dx(t1))**2+(dy(t1))**2+(dz(t1))**2)
    
    nx = y(t1)*dz_1-z(t1)*dy_1
    ny = -x(t1)*dz_1+z(t1)*dx_1
    nz = x(t1)*dy_1-y(t1)*dx_1
    
    xi_1 = x(t1)*np.cos(delta)-nx*np.sin(delta)
    yi_1 = y(t1)*np.cos(delta)-ny*np.sin(delta)
    zi_1 = z(t1)*np.cos(delta)-nz*np.sin(delta)

    R = cmath.acos(yi_1)  
    if np.sign(xi_1)>=0:
        Theta = np.real(cmath.acos(zi_1/np.sin(R)))
    else:
        Theta = 2*np.pi-np.real(cmath.acos(zi_1/np.sin(R)))
    
    return Theta


def theta_ext_simple(alpha, beta, delta, r):
    """
    Computes exterior theta for negligible precession

    Parameters
    ----------
    alpha : float
        SLP parameter (rad)
    beta : float
        SLP parameter (rad)
    delta : float
        SLP parameter (rad)
    r : float
        Angle with precesion axis (rad)

    Returns
    -------
    theta_e : float
        Value of exterior theta
    
    """ 

    theta_e = np.real(cmath.acos((np.cos(beta - delta) - np.cos(alpha) * np.cos(r))/(np.sin(alpha) * np.sin(r))))

    return theta_e


def theta_int_simple(alpha, beta, delta, r):
    """
    Computes interior theta for negligible precession

    Parameters
    ----------
    alpha : float
        SLP parameter (rad)
    beta : float
        SLP parameter (rad)
    delta : float
        SLP parameter (rad)
    r : float
        Angle with precesion axis (rad)

    Returns
    -------
    theta_i : float
        Value of interior theta
    
    """ 

    theta_i = np.real(cmath.acos((np.cos(beta + delta) - np.cos(alpha) * np.cos(r))/(np.sin(alpha) * np.sin(r))))

    return theta_i