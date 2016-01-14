
from math import exp

def cc(d, gas):
    """
    Calculate Cunningham correction factor.

    Parameters
    -----------
    d:      float
            Particle diameter in nanometers.
    gas:    Gas object
            gas object from the atmosphere package

    Returns
    --------
    Cunningham correction factor as a function of diameter and mean free path.

    Notes
    -------
    This is from Hinds (1999); p49, eq 3.20
    """

    # Convert diameter to microns.
    d = float(d)*1e-3
    # Get the mean free path
    try:

        mfp = gas.l()
        return (1.05*exp(-0.39*d/mfp)+2.34)*mfp/d+1

    except AttributeError:
        print('Invalid type entered for "gas".  Should be of type atmosphere.gas".')
        return 0


def kn(dp, gas):
    """
    Calculate the Knudsen number of a particle.

    The Knudsen number determines the appropriateness of the continuum assumption.  If Kn >~1, then the continuum
    assumption is not appropriate for the problem solution.

    Parameters
    ----------
    dp:     float
            particle diameter in nm
    gas:    gas object
            Gas object used to determine the mean free path of the gas.

    Returns
    -------
    float
        Knudsen number

    """
    return 2*gas.l/dp