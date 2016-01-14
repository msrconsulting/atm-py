def d50(n, rhop, q, gas, dj):
    """
    Find the impactor cutpoint.

    Parameters
    ----------
    N:      int
            number of jets
    rhop:   float
            particle density in kg/m^3
    Q:      float
            volumetric flow rate in lpm
    gas:    Gas object
            gas object that utilize a child of the Gas class.
    dj:     int
            jet diameter in meters

    Returns
    -------
    Impactor cutpoint in microns.

    Notes
    ------
    Calculations are those of Hinds (1999)

    """

    # Convert the volumetric flow rate into m^3/s
    q = float(q)/60*1000/100**3

    # From Hinds, this is the Stoke's number for the 50% collections
    # efficiency (Table 5.4)
    stk50 = 0.24

    # Equation 5.29 in Hinds (1999)
    d50cc = sqrt(9*gas.mu()*pi*n*dj**3*stk50/(4.0*float(rhop)*q))

    f = lambda x: (d50cc/float(x))**2-cc(float(x*1e-6), gas)

    # Find the D50 of the impactor
    return fsolve(f, 0.1)