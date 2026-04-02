#!/usr/bin/env python

"""
Computes price based on a base fee + plus distance and
duration add-ons

Constitutes 3 base startegies
"""
from data.data import RideRequest
def economy_fare(ride: RideRequest) -> float:
    """ KES 50 + KES 30/KM + KES 2/MIN"""
    return 50 + ride.distance_km*30 + ride.duration_min*2

def business_fare(ride: RideRequest) -> float:
    """KES 100 + KES 55/KM + KES 4/MIN"""
    return 100 + ride.distance_km*55 + ride.duration_min*4

def luxury_fare(ride: RideRequest) -> float:
    """KES 200 + KES 100/KM + 10/MIN"""
    return 200 + ride.distance_km*100 + ride.duration_min*10
