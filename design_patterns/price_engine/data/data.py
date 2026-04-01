#!/usr/bin/env python

"""
Provides the data structure for a ride request
"""

from dataclasses import dataclass
from datetime import datetime

@dataclass
class RideRequest:
    rider_name: str
    distance_km: float
    duration_min: int
    requested_at: datetime
    trips: int
    promo_code: str | None = None
