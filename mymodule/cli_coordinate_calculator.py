"""
This module is to transfer coordinates of sources with hms or dms unit to degree.
"""
# The input should be in three formats, namely, '12h20m30s' or '12:20:30' or '12 20 30'
# All formats are should be the string type 
from astropy.coordinates import Angle
from astropy import units as u

#import math
#import re # it seems it is not used

import argparse

# when just run `python3 mymodule/cli_coordinate_calculator`, 
# there would be a reminder for user to type in the right formats.
def get_user_input():
    """
    Manually input ra and dec

    Return 
    -------
    ra 
    dec
    """
    #ra_0 = '12h20m30.5s'
    #dec_0 = '12d16m45.3s'
    # remind and split ra and dec as well if in the form of '12h20m30s/12d20m30.3s'
    reminder = input("Please input ra and dec like '12h20m30s/12d20m30.3s' or '12:20:30' or '12 20 30'")
    ra, dec = reminder.split('/')
    return ra, dec

# Use module Angle from astropy.coordinates to do the calculation. 
def degree_cal(ra = '12h20m30.5s', dec = '12d16m45.3s'):
    """
    Parameters
    ------
    ra : string
    dec : string
    """
    # just move the default value to the above
    #ra = '12h20m30.5s' #no matter ra 
    #dec = '12d16m45.3s'
    #calculate the degree using Angle
    ra_ang = Angle(ra, unit='hourangle')
    ra_deg = ra_ang.degree

    dec_ang = Angle(dec, unit=u.deg)
    dec_deg = dec_ang.degree
    return ra_deg, dec_deg


def coorcal_parser():
    """
    Configure the argparse for cli_coordinate_calculator

    Returns
    -------
    parser : argparse.ArgumentParser
        The parser for cli_coordinate_calculator.
    """
    parser = argparse.ArgumentParser(prog='cli_coordinate_calculator', prefix_chars='-')
    parser.add_argument('--ra', dest = 'ra', type=str, default=None,
                        help="Central ra (degrees) for the simulation location")
    parser.add_argument('--dec', dest = 'dec', type=str, default=None,
                        help="Central dec (degrees) for the simulation location")
    parser.add_argument('--cite', action='store_true',
                        help="How to cite this work")
    return parser


if __name__ == "__main__":
    parser = coorcal_parser()
    options = parser.parse_args()
    # if ra/dec are not supplied the use a default value
    if None in [options.ra, options.dec]:
        ra, dec = get_user_input()
    else:
        ra = options.ra
        dec = options.dec

if options.cite:
    print("If you feel this work is useful, please cite @ https://github.com/XShao0062/super-rotary-phone.git")
else:
    calculated_coord = degree_cal(ra, dec)
    print("Your expected coordinate in degrees:", calculated_coord)
