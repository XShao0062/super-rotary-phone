
# The input should be in three formats, namely, '12h20m30s' or '12:20:30' or '12 20 30'
# All formats are should be the string type 
from astropy.coordinates import Angle
from astropy import units as u

#import math
import re

#
def user_reminder():
    #ra_0 = '12h20m30.5s'
    #dec_0 = '12d16m45.3s'
    reminder = input("Please input ra and dec like '12h20m30s/12d20m30.3s' or '12:20:30' or '12 20 30'")    
    return reminder


def get_user_input(ra, dec):
    ra = '12h20m30.5s' #no matter ra 
    dec = '12d16m45.3s'
    #calculate the degree using Angle
    ra_ang = Angle(ra, unit='hourangle')
    ra_deg = ra_ang.degree

    dec_ang = Angle(dec, unit=u.deg)
    dec_deg = dec_ang.degree
    return deg_Ra, deg_Dec


if __name__ == "__main__":
    user_input = get_user_input()
    print("You entered:", user_input)
