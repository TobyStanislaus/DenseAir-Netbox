from math import pi

def circleArea(r):
    if r<0:
        raise ValueError
    
    return pi*(r**2)