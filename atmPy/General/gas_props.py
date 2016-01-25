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

    @abc.abstractmethod
    def rho(self):
        return 0


