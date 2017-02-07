import fnmatch
from functools import partial
from . import _available_suites, default_suite, lookup
import pytest


def pytest_addoption(parser):
    parser.addoption('--suite', action='store', default=None, type=str,
                     help='execute a specified suite')


def pytest_configure(config):
    suite_name = config.getoption('--suite')
    if suite_name is None:
        config.suite = default_suite
    else:
        config.suite = lookup(suite_name)
        
    config.available_suites = _available_suites


def matches_pattern(pattern, name):
    # the pattern may be a list of patterns
    if isinstance(pattern, list):
        return any([fnmatch.fnmatch(name, p) for p in pattern])
    
    return fnmatch.fnmatch(name, pattern)


def pytest_collection_modifyitems(config, items):
    matches_suite_name = partial(matches_pattern, config.suite.pattern)
    suite_members = filter(lambda i: matches_suite_name(i.name), items)

    # what is this weird shit? `items` is passed in by reference
    # if we just did `items = suite_members` we would overwrite the reference
    # according to this blog post https://hackebrot.github.io/pytest-tricks/run_tests_using_fixture/
    # i should be using pytest_deselected to force the non-matching items to
    # be removed. However, that does not seem to be necessary
    items[:] = suite_members


@pytest.fixture
def suite(request):
    return request.config.suite
