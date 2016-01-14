from atmPy import constants
from scipy.optimize import fsolve
from math import pi, exp, log10, sqrt, log


def z(d, gas, n):
    """
    Calculate electric mobility of particle with diameter D.

    Parameters
    -----------
    d:      float
            diameter in nm
    gas:    object of type gas
            Object that defines the gas calculations
    n:      int
            number of charges

    Returns
    ---------
    Electrical mobility in m2/V*s as defined in Hinds (1999), p. 322, eq. 15.21.
    """

    try:
        return n * constants.e * cc(d, gas) / (3 * pi * gas.mu() * d * 1e-9)
    except AttributeError:
        print('Incorrect type selected for attribute "gas".')
        return 0


def z2d(zin, gas, n=1):
    """
    Retrieve particle diameter from the electrical mobility

    Call this using a roots or fsolve function.

    Parameters
    -----------
    gas:    gas object
            Gas object defining properties of variables related to gases
    zin:    float
            Electrical mobility in m2/Vs
    n:      float, optional, default = 1
            Number of charges

    Returns
    -------
    Diameter of particle in nanometers.
    """

    # Inline function use with fsolve
    f = lambda d: d * 1e-9 - n * constants.e * cc(d, gas) / (3 * pi * gas.mu() * zin)
    d0 = 1e-9
    return fsolve(f, d0)[0]
