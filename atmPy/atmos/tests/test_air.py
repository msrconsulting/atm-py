import atmPy.atmos.air as air

from numpy import abs


class TestAir(object):
    def __init__(self):
        self.a = air.Air()

        self.mu_vals = {'T': [-5, 0, 10, 15, 25],
                        'mu': [1.7105007E-5, 1.7362065e-5, 1.7869785E-5, 1.8120528E-5, 1.861598E-5]
                        }

        self.rho_vals = {'T': [0, 0, 0, 0,
                               0, 0, 0, 0,
                               0, 0, 0, 0,
                               25, 25, 25, 25,
                               25, 25, 25, 25,
                               25, 25, 25, 25],
                         'P': [200, 200, 200, 200,
                               800, 800, 800, 800,
                               1000, 1000, 1000, 1000,
                               200, 200, 200, 200,
                               800, 800, 800, 800,
                               1000, 1000, 1000, 1000],
                         'RH': [25, 50, 75, 90,
                                25, 50, 75, 90,
                                25, 50, 75, 90,
                                25, 50, 75, 90,
                                25, 50, 75, 90,
                                25, 50, 75, 90],
                         'rho': [0.254, 0.254, 0.253, 0.252,
                                 1.020, 1.019, 1.018, 1.018,
                                 1.275, 1.274, 1.273, 1.273,
                                 0.230, 0.227, 0.223, 0.221,
                                 0.931, 0.928, 0.924, 0.922,
                                 1.165, 1.161, 1.158, 1.156
                                 ]
                         }

    def test_muvals(self):
        print('========= Testing Dynamic Viscocity Calculations =========')
        print('   T       mu   ')
        print('======= ========')

        for e, i in enumerate(self.mu_vals['T']):
            yield self.check_mu, i, self.mu_vals['mu'][e], 1e-3

    def test_rhos(self):
        print('========= Testing Density Calculations =========')
        print('   T       P       RH       rho   ')
        print('======= ======= ======== =========')

        for e, i in enumerate(self.rho_vals['rho']):
            yield self.check_rho, {'T': self.rho_vals['T'][e],
                                   'P': self.rho_vals['P'][e],
                                   'RH': self.rho_vals['RH'][e]}, i, 0.2

    @staticmethod
    def check_mu(t, val, tol):
        a = air.Air(t, 850)
        print(a.t, a.mu(), abs((val - a.mu()) / val))
        assert abs((val - a.mu()) / val) < tol

    @staticmethod
    def check_rho(atm, val, tol):
        kwargs = {"rh": atm['RH']}
        a = air.Air(atm['T'], atm['P'], **kwargs)
        print(a.t, a.p, atm['RH'], val, a.rho(), abs((val - a.rho()) / val))
        assert abs((val - a.rho()) / val) < tol

    @staticmethod
    def test_mfp():
        """
        Test the calculation of the mean free path against the standard using the
        mean free path at standard conditions (0.066 um; from Hand 1999, p 21)

        """

        p = [100, 500, 800, 1000]

        print('')
        print('========= Testing MEAN FREE PATH Calculations =========')
        print('   P       mfp       mfp       r   ')
        print('======= ========= ========= =======')

        for i in p:
            ltest = 0.066 / i * 1013.25 / 1e6
            a = air.Air(20, i)

            print(i, a.l(), ltest, abs(ltest - a.l()) / ltest)
            assert abs(ltest - a.l()) / ltest < 0.01

        print(' ')
