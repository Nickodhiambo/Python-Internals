#!/usr/bin/env python
"""
Provides discount strategies which are applied after base and surge to determine the final price
Take a ride request and price and applies discount if any
"""

from data.data import RideRequest

def no_discount(ride: RideRequest, price: float) -> float:
    return price

def loyalty_discount(ride: RideRequest, price: float) -> float:
    """Determined by the number of previous trips made
    10% off if prev trips >= 50
    5% off if prev trips >= 20
    """
    if ride.trips >= 50:
        return price * 0.9
    if ride.trips >= 20:
        return price * 0.95
    return price

def promo_codes(ride: RideRequest, price: float) -> float:
    """discounts a flat KES 100 or 50 with valid promo codes"""
    valid_codes = {'WELCOME100', 'JAMHURI100' 'BOLT50'}
    if ride.promo_code in valid_codes:
        discount = 100 if '100' in ride.promo_code else 50
        return max(0, price - discount)
    return price
