import atmPy.General.gas_properties as gp
import atmPy.General.vapor_pressure as vp


class Air(gp.Gas):
    def __init__(self, t=20.0, p=1013.25, **kwargs):
        super(Air, self).__init__(t, p)

        self._Rd = 287.05
        self._Rv = 461.495
        self.e = 0


        if "ecal_meth" in kwargs:
            self._wvObj = kwargs.ecal_meth
        else:
            self._wvObj = vp.MurphyKoop()

        if "e" in kwargs:
            self.e = kwargs.e
        elif "rh" in kwargs:
            self.e = self._wvObj.ew(self.t) * kwargs.rh / 100
        else:
            self.e = 0

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

        c = 120.0  # Sutherland's constant
        mu0 = 18.27e-6  # Reference viscocity
        t0 = 291.15  # Reference temperature

        return (c + t0) / (c + self.t) * (self.t / t0) ** 1.5 * mu0

    def l(self):
        """
        Determine the mean free path of air.

        Returns
        -------
        Mean free path of air in microns.
        """

        # Convert pressure to atmospheres
        patm = float(self.p) / 1013.25
        l0 = 0.066  # Reference mean free path at 1 atm

        return l0 / patm

    def rho(self):

        # Convert pressure to Pascals before calculating the density
        return self.p*100 / (self._Rd * self.t) + self.e*100/(self._Rv * self.t)
