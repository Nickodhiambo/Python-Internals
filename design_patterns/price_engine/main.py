#!/usr/bin/env python

"""
Provides entry point for running price engine
"""
from data.data import RideRequest
from strategies import base, surge, discount
from engine.engine import PricingEngine
from datetime import datetime

if __name__ == '__main__':
	# Scenario 1: Economy ride, peak hour, loyal rider
	alice_ride = RideRequest(
    	rider_name   = "Alice",
    	distance_km  = 8.5,
    	duration_min = 22,
    	requested_at = datetime(2024, 1, 15, 8, 30),  # 8:30am — peak
    	trips  = 65,   # loyal rider
	)

	engine1 = PricingEngine(
    	base_fare_strategy = base.economy_fare,
    	surge_strategy     = surge.time_based_surge,
    	discount_strategy  = discount.loyalty_discount,
	)	
	engine1.explain(alice_ride)
