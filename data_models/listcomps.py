#!/usr/bin/env python


def test_listcomp_readability():
    symbols = '$€¥&£'

    # Use list comp to nuilf
    codes = [ord(symbol) for symbol in symbols]
    return codes
