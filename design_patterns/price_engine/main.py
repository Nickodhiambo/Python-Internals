#!/usr/bin/env python

"""
Provides entry point for running price engine
"""
from data import RideRequest
from engine import PricingEngine, get_pricing_engine
from datetime import datetime


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
