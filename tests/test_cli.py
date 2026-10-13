import subprocess
import sys


def test_cli_help():
    result = subprocess.run(
        [sys.executable, "-m", "toolkit", "--help"],
        capture_output=True,
        check=False,
    )
    assert result.returncode == 0


def test_cli_calc():
    result = subprocess.run(
        [sys.executable, "-m", "toolkit", "calc", "2 + 3 * 4"],
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0
    assert result.stdout.strip() == "14.0"


def test_cli_error():
    result = subprocess.run(
        [sys.executable, "-m", "toolkit", "calc", "1 / 0"],
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 2
    assert "Деление на ноль" in result.stderr
