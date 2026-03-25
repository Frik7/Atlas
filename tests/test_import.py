"""
Basic tests for Atlas.
"""

import atlas


def test_version() -> None:
    assert atlas.__version__ == "0.1.0"
