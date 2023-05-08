import subprocess


def test_cov():
    """
    Run all unit test with coverage
    """
    subprocess.run(
        ["pytest", "--cov=.", "--cov-report=html", "tests/"]
    )
