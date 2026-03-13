#!/usr/bin/env python

def dict_comp():
    """
    Builds a dict from an iterable just like
    list comps
    """
    # an itetable: list of tuples
    country_codes = [
            (880, 'Bangladesh'),
            (55, 'Brazil'),
            (86, 'China'),
            (91, 'India'),
            (62, 'Indonesia'),
            (81, 'Japan'),
            (234, 'Nigeria'),
            (92, 'Pakistan'),
            (7, 'Russia'),
            (1, 'United States'),
            ]

    # Build a dict from iterable
    country_dials = {
            country: code for code, country in country_codes
            }

    # Build another dict from dict iterable
    country_dials_upper = {
            country.upper(): code for country, code in\
                    country_dials.items()
            }
    return country_dials, country_dials_upper
