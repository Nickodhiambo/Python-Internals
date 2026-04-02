#!/usr/bin/env python

"""
Provides entry point for running price engine
"""
from data.data import RideRequest
from strategies.base import (
        economy_fare, business_fare, luxury_fare)
from strategies.surge import (
        time_based_surge, demand_based_surge)
from strategies.discount import (
        no_discount, promo_codes, loyalty_discount)
from engine.engine import PricingEngine
from datetime import datetime

def get_pricing_engine(ride: RideRequest, tier: str) -> PricingEngine:
    """
    A factory function that assembles the right engine
    based on rider information and car tier and feeds it
    into price calculator
    """
    # base fares
    base_fares = {
            'economy': economy_fare,
            'business': business_fare,
            'luxury': luxury_fare
            }
    base = base_fares[tier]
    surge = time_based_surge if 7 <= ride.requested_at.hour\
            <= 9 or 17 <= ride.requested_at.hour <= 20\
            else demand_based_surge

    # Pick promo over loyalty
    if ride.promo_code:
        discount = promo_codes
    elif ride.trips >= 20:
        discount = loyalty_discount
    else:
        discount = no_discount

    return PricingEngine(
            base, surge, discount
            )

if __name__ == '__main__':
    alice_ride = RideRequest(
            rider_name   = "Alice",
            distance_km  = 8.5,
            duration_min = 22,
            requested_at = datetime(2024, 1, 15, 8, 30),  # 8:30am — peak
            trips  = 65,   # loyal rider
            )
    engine1 = get_pricing_engine(alice_ride, "economy")
    engine1.explain(alice_ride)
