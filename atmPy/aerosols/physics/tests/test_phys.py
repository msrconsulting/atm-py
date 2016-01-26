from atmPy.aerosols.physics import aerosol
from atmPy.atmos.air import Air


def test_cc():
    """
    Provides a basic check on the calculation of the slip correction factor.  Values are taken
    from Hand, 1999, Appendix A11
    """

    t = {'d': [0.001, 0.01, 0.1, 1, 10, 100],
         'cc': [224.332, 22.976, 2.928, 1.155, 1.015, 1.002]
         }

    a = Air()

    print(' ')
    print("Testing SLIP CORRECTION FACTOR at stp.")
    print('   D (um)       cc       cc   ')
    print('============ ======== ========')

    for i, e in enumerate(t['d']):
        cc = t['cc'][i]
        print(e, aerosol.cc(e * 1000, a), cc)
        assert (aerosol.cc(e * 1000, a) - cc) / cc < 0.001

    print('')
