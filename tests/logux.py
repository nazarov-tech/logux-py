"""Tests for `logux` package."""

import pytest

from logux import logux


@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    assert dir(logux) == dir(logux )


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument."""

    assert dir(logux) == dir(logux)
