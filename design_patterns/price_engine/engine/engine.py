#!/usr/bin/env python

"""
Takes an assembled strategy and computes price
"""
from typing import Callable
from data import RideRequest

# Type aliases for strategies
BaseStrategy = Callable[[RideRequest], float]
SurgeStrategy = Callable[[RideRequest], float]
DiscountStrategy = Callable[[RideRequest, float], float]

class PricingEngine:
    def __init__(self,
                 base_fare_strategy: BaseStrategy,
                 surge_strategy: SurgeStrategy,
                 discount_strategy: DiscountStrategy
                 ):
        self.base = base_fare_strategy
        self.surge = surge_strategy
        self.discount = discount_strategy

    def calculate(self, ride: RideRequest) -> dict:
        base = self.base(ride)
        surge = self.surge(ride)
        surged = base * surge
        final = self.discount(ride, surged)

        return {
                'rider': ride.rider_name,
                'base_price': base,
                'surge_factor': surge,
                'after_surge': round(surged, 2),
                'final_price': round(final, 2),
                'savings': round(surged - final, 2)
                }

    def explain(self, ride: RideRequest):
        result = self.calculate(ride)
        print(f"\n{'=' * 45}")
        print(f"Ride summary for {result['rider']}")
        print(f'\n{'=' * 45}')
        print(f"Base fare: KES {result['base_price']}")
        print(f"surge factor (X{result['surge_factor']}): KES{result['after_surge']}")
        print(f"Discount: -KES {result['savings']}")
        print(f"{'-' * 45}")
        print(f"Final price: KES {result['final_price']}")
        print(f"{'=' * 45}\n")
