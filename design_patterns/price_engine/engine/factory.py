#!/usr/bin/env python
from strategies import (
        economy_fare, business_fare, luxury_fare)
from strategies import time_based_surge, demand_based_surge
from strategies import (
        no_discount, loyalty_discount, promo_codes)
from data import RideRequest
from engine import PricingEngine

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

