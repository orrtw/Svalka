# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 13:16:57 2018

@author: Наталия 
"""
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import astropy.units as u 
from astropy.coordinates import SkyCoord 
from astroquery.vizier import Vizier

center_coords = SkyCoord('02h21m00s +57d07m42s')
vizier = Vizier(column_filters={'Bmag': '<13'}, row_limit=10000)
usno_sources = vizier.query_region(
        center_coords,
        width= 90*u.arcmin,
        height=90*u.arcmin,
        catalog='USNO-A2.0',
        )[0]
print(usno_sources)

ra= usno_sources['RAJ2000']._data
dec = usno_sources['DEJ2000']._data
x = np.vstack(((ra - ra.mean())*np.cos(dec/180*np.pi)+ra.mean(), dec)).T

plt.plot(*x.T, '*')
print(x)
