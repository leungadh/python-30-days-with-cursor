import math
import subprocess
import sys
from day_01_import_helper import import_from_path

# Import the module functions without relying on package install
mod = import_from_path('temp_converter', 'day-01/temp_converter.py')


def approx_equal(a, b, tol=1e-6):
    return abs(a - b) <= tol


def test_c_to_f():
    assert approx_equal(mod.c_to_f(0), 32)
    assert approx_equal(mod.c_to_f(100), 212)


def test_f_to_c():
    assert approx_equal(mod.f_to_c(32), 0)
    assert approx_equal(mod.f_to_c(212), 100)


def test_c_to_k_and_back():
    k = mod.c_to_k(25)
    assert approx_equal(k, 298.15)
    c = mod.k_to_c(k)
    assert approx_equal(c, 25)


def test_convert_valid():
    assert approx_equal(mod.convert(22, 'c', 'f'), 71.6)
    assert approx_equal(mod.convert(80, 'f', 'c'), 26.6666667)
    assert approx_equal(mod.convert(25, 'c', 'k'), 298.15)


def test_convert_invalid_physical():
    import pytest
    with pytest.raises(mod.ConversionError):
        mod.convert(-1, 'k', 'c')
    with pytest.raises(mod.ConversionError):
        mod.convert(-274, 'c', 'k')
    with pytest.raises(mod.ConversionError):
        mod.convert(-500, 'f', 'c')


def run_cli(args):
    cmd = [sys.executable, 'day-01/temp_converter.py'] + args
    res = subprocess.run(cmd, capture_output=True, text=True)
    return res.returncode, res.stdout.strip(), res.stderr.strip()


def test_cli_samples():
    code, out, err = run_cli(['--to','f','--c','22'])
    assert code == 0 and out == '71.6'

    code, out, err = run_cli(['--to','c','--f','80'])
    assert code == 0 and out.startswith('26.67')

    code, out, err = run_cli(['--to','k','--c','25','--precision','3'])
    assert code == 0 and out == '298.15'  # rounding to 3 keeps 298.150 -> 298.15
