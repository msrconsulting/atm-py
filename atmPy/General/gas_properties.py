import abc


class Gas(object):
    """
    Generic object defining different properties of gasses.

    Attributes
    ----------
    p:  float
        Pressure in mb.
    t:  float
        Temperature in degrees Celsius.
    """
    __metaclass__ = abc.ABCMeta

    def __init__(self, t=20, p=1013.25):
        self.t = t
        self.p = p

    def __str__(self):
        return "Gas object with T = " + str(self.t) + " and P = " + str(self.p) + "."

    @abc.abstractmethod
    def mu(self):
        return 0

    @abc.abstractmethod
    def l(self):
        return 0


class Air(Gas):
    def __init__(self, t=20.0, p=1013.25):
        super(Air, self).__init__(t, p)

    def mu(self):
        """
        The following function defines viscosity as a function of T in P-s.

        Parameters
        ---------
        T:temperature in degrees Celsius

        Returns
        -------
        Viscosity in P-s
        """

        # Make sure that the temperature is a float
        t = self.t + 273.15
        c = 120.0       # Sutherland's constant
        mu0 = 18.27e-6  # Reference viscocity
        t0 = 291.15     # Reference temperature

        return (c+t0)/(c+t)*(t/t0)**1.5*mu0

    def l(self):
        """
        Determine the mean free path of air.

        Returns
        -------
        Mean free path of air in microns.
        """

        # Convert pressure to atmospheres
        patm = float(self.p)/1013.25
        l0 = 0.066  # Reference mean free path at 1 atm

        return l0/patm