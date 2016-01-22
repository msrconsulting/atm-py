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
        self.t = t + 273.15
        self.p = p

    def __str__(self):
        return "Gas object with T = " + str(self.t) + " and P = " + str(self.p) + "."

    @abc.abstractmethod
    def mu(self):
        """
        Dynamic viscocity

        Returns
        --------
        float
            Viscocity of the specific gas at the current conditions in Pa*s
        """
        return 0

    @abc.abstractmethod
    def l(self):
        """
        Mean free path.

        Returns
        --------
        float
            Mean free path of gas in m.
        """
        return 0

    @abc.abstractmethod
    def rho(self):
        """
        Density of gas

        Returns
        -------
        float
            Density of gas in kg/m-3.
        """
        return 0