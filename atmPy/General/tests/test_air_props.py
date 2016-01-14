import unittest
import atmPy.General.gas_properties as gas


class TestAirProps(unittest.TestCase):

    def test_t(self):
        self.assertEqual(self.t, self.air.t)

    def test_p(self):
        self.assertEqual(self.p, self.air.p)

    def setUp(self):
        self.t = 25
        self.p = 845
        self.air = gas.Air(self.t,self.p)

if __name__ == '__main__':
    unittest.main()