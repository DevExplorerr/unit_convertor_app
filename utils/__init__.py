# filepath: /unit-converter-app/unit-converter-app/src/utils/__init__.py
# This file is intentionally left blank.

def convert_units(value, unit_from, unit_to):
    """Converts a value from one unit to another."""
    if unit_from == unit_to:
        return value

    # Conversion factors (meters as base unit)
    conversion_factors = {
        "Kilometers": 1000.0,
        "Meters": 1.0,
        "Centimeters": 0.01,
        "Millimeters": 0.001,
        "Micrometers": 1e-6,
        "Nanometers": 1e-9,
        "Miles": 1609.34,
        "Yards": 0.9144,
        "Foot": 0.3048,
        "Inches": 0.0254,
        "Nautical miles": 1852.0,
    }

    # Convert to base unit (meters)
    value_in_meters = value * conversion_factors[unit_from]

    # Convert from base unit to target unit
    result = value_in_meters / conversion_factors[unit_to]

    return result
