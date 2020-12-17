"""
This can be used, for example, to do more expensive setup at test run time in the fixture,
rather than having to run those setup steps at collection time.
"""
import pytest


@pytest.fixture
def fixt(request):
    return request.param * 3


@pytest.mark.parametrize("fixt", ["a", "b"], indirect=True)
def test_indirect(fixt):
    assert len(fixt) == 3