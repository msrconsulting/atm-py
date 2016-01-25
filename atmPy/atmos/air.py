import atmPy.atmos.gas_props as gp
import atmPy.atmos.water as water


class Air(gp.Gas):
    def __init__(self, t=20.0, p=1013.25, **kwargs):
        super(Air, self).__init__(t, p)

        self._Rd = 287.05
        self._Rv = 461.495
        self.e = 0

        if "ecal_meth" in kwargs:
            self._wvObj = kwargs.ecal_meth
        else:
            self._wvObj = water.MurphyKoop()

        if "e" in kwargs:
            self.e = kwargs.e
        elif "rh" in kwargs:
            self.e = self._wvObj.ew(self.t) * kwargs['rh'] / 100
        else:
            self.e = 0

    def cal_e(self, rh):
        self.e = self._wvObj.ew(self.t) * rh / 100

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
        c = 120.0  # Sutherland's constant
        mu0 = 18.27e-6  # Reference viscocity
        t0 = 291.15  # Reference temperature

        return (c + t0) / (c + t) * (t / t0) ** 1.5 * mu0

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

        tk = self.t + 273.15
        return self.p * 100 / (self._Rd* tk) + self.e * 100 / (self._Rv * tk)
