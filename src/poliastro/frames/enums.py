"""Coordinate frames definitions.

"""
from enum import Enum


class Planes(Enum):
    EARTH_EQUATOR = "Earth mean Equator and Equinox of epoch (J2000.0)"
    EARTH_ECLIPTIC = "Earth mean Ecliptic and Equinox of epoch (J2000.0)"
    # BODY_EQUATOR = 'Body mean Equator and node of date'  # TODO: Implement proper conversions
