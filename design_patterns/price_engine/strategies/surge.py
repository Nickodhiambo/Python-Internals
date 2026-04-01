#!/usr/bin/env python

"""
Provides surge strategies which compute price based on surge
Surge strategies do not take into account vehicle tier
They take ride information and return a multiplier
"""
from data.data import RideRequest

def no_surge(ride: RideRequest) -> float:
    return 1.0

def time_based_surge(ride: RideRequest) -> float:
    """Peak hrs are btn 7-9 AM and 5-8 PM get 1.5 multiplier"""
    hour = ride.requested_at.hour
    if 7 <= hour <= 9 or 17 <= hour <= 20:
        return 1.5
    return 1.0

def demand_based_surge(ride: RideRequest) -> int:
    """ Simulates a real demand. In product we would query a live demand service"""
    if ride.distance_km < 3:
        return 2.0 # Short inner city trips have high demand
    elif ride.distance_km < 10:
        return 1.4
    return 1.0
