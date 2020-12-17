def pytest_generate_tests(metafunc):
    if "param1" in metafunc.fixturenames:
        end = 5 if metafunc.config.getoption("all") else 2
        metafunc.parametrize("param1", range(end))


def test_compute(param1):
    assert param1 < 4