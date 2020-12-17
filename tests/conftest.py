def pytest_addoption(parser):
    parser.addoption(
        "--stringinput",
        action="append",
        default=[],
        help="list of stringinputs to pass to test functions",
    )
    parser.addoption("--all", action="store_true", help="run all combinations")

