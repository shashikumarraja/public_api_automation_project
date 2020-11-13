import pytest

def pytest_addoption(parser):
    """User defined options

    Args:
        parser ([type]): [description]
    """
    parser.addoption("--base-url", dest="base_url", action="store",
                     help="Base url of API", required=False,
                     default="https://cat-fact.herokuapp.com/")


def pytest_configure(config):
    """
    Read user defined options and make it available for tests
    :param config: pytest config object which contains input arguments
    :return:
    """
    config.base_url = config.getoption("base_url")