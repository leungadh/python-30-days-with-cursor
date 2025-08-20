"""
Day 01 — Temperature Converter CLI

Usage examples:
  python temp_converter.py --to f --c 22
  python temp_converter.py --to c --f 80
  python temp_converter.py --to k --c 25 --precision 3

The tool accepts *one* input scale flag (--c, --f, or --k) and converts to the
scale specified by --to {c,f,k}. It validates inputs and supports configurable
rounding precision.
"""
from __future__ import annotations
import argparse
import sys

# --- Conversion helpers ---

def c_to_f(c: float) -> float:
    return c * 9/5 + 32

def f_to_c(f: float) -> float:
    return (f - 32) * 5/9

def c_to_k(c: float) -> float:
    return c + 273.15

def k_to_c(k: float) -> float:
    return k - 273.15

def f_to_k(f: float) -> float:
    return c_to_k(f_to_c(f))

def k_to_f(k: float) -> float:
    return c_to_f(k_to_c(k))

VALID_SCALES = {"c", "f", "k"}

class ConversionError(Exception):
    pass


def convert(value: float, from_scale: str, to_scale: str) -> float:
    """Convert temperature between C/F/K.

    Raises ConversionError for invalid scales or physical impossibilities
    (e.g., Kelvin < 0).
    """
    fs = from_scale.lower()
    ts = to_scale.lower()
    if fs not in VALID_SCALES or ts not in VALID_SCALES:
        raise ConversionError(f"Invalid scale(s). Use one of: {sorted(VALID_SCALES)}")
    if fs == ts:
        return float(value)

    # Physical validation: Kelvin cannot be below absolute zero
    if fs == 'k' and value < 0:
        raise ConversionError("Kelvin cannot be negative.")
    if fs == 'c' and (value < -273.15):
        raise ConversionError("Celsius below -273.15 is physically invalid.")
    if fs == 'f' and (value < -459.67):
        raise ConversionError("Fahrenheit below -459.67 is physically invalid.")

    if fs == 'c' and ts == 'f':
        return c_to_f(value)
    if fs == 'f' and ts == 'c':
        return f_to_c(value)
    if fs == 'c' and ts == 'k':
        return c_to_k(value)
    if fs == 'k' and ts == 'c':
        return k_to_c(value)
    if fs == 'f' and ts == 'k':
        return f_to_k(value)
    if fs == 'k' and ts == 'f':
        return k_to_f(value)

    # Should not reach here
    raise ConversionError("Unsupported conversion path.")


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        description="Convert temperatures between Celsius, Fahrenheit, Kelvin.")
    p.add_argument('--to', required=True, choices=['c','f','k'],
                   help='Target scale: c, f, or k')

    src = p.add_mutually_exclusive_group(required=True)
    src.add_argument('--c', type=float, help='Input in Celsius')
    src.add_argument('--f', type=float, help='Input in Fahrenheit')
    src.add_argument('--k', type=float, help='Input in Kelvin')

    p.add_argument('--precision', type=int, default=2,
                   help='Decimal places for rounding (default: 2)')
    return p


def main(argv=None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    # Determine input value and scale
    if args.c is not None:
        value, from_scale = args.c, 'c'
    elif args.f is not None:
        value, from_scale = args.f, 'f'
    else:
        value, from_scale = args.k, 'k'

    try:
        result = convert(value, from_scale, args.to)
    except ConversionError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 2

    print(round(result, args.precision))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
