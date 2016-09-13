import atmPy.atmos.water as water


class TestWater(object):
    def __init__(self):
        self.T = range(-40, 40, 20)

        self.RH = range(25, 100, 25)

        # Dewpoint caluclations are from Brian McNoldy's dewpoint calcuator at
        # http://andrew.rsmas.miami.edu/bmcnoldy/Humidity.html
        self.tde = [[-52.52, -35.02, -17.72, -0.64, 16.25],
                    [-46.46, -27.77, -9.2, 9.26, 27.60],
                    [-42.73, -23.29, -3.9, 15.43, 34.72]
                    ]

    def test_td(self):
        print('')
        print('========= Testing Dewpoint Calculations =========')
        print('   T       RH       td       tde   ')
        print('======= ======== ======== =========')

        for e1, t in enumerate(self.T):
            for e2, rh in enumerate(self.RH):
                yield self.check_td, t, rh, self.tde[e2][e1]

    @staticmethod
    def check_td(t, rh, tdexpected):
        # Just a sanity check - use MK
        emk = water.MurphyKoop()
        td = emk.dew_point(t, rh)
        print(t, rh, td, tdexpected)
        assert abs(td - tdexpected) < 1
