import pytest
import _pytest


pytest_plugins = 'pytester'


def test_pytest_suites_use_fixture(testdir):

    testdir.makepyfile("""
    def test_use_fixture(suite):
        print "The suite name is %s" % suite.name
    """)
    result = testdir.runpytest("-s")
    result.stdout.fnmatch_lines("*The suite name is default*")


def test_pytest_suites_filter_by_suite(testdir):
    testdir.makeconftest("""
    from pytest_suites import add_suite

    pytest_plugins = ['suites']
    add_suite(name="gcp", pattern="*gcp*")
    
    """)

    testdir.makepyfile("""
    def test_gcp():
        assert True

    def test_aws():
        assert True

    """)
 
    result = testdir.runpytest("--verbose", "--suite", "gcp")
    result.stdout.fnmatch_lines("*test_gcp PASSED*")
    with pytest.raises(_pytest.runner.Failed):
        result.stdout.fnmatch_lines("*test_aws*")


def test_pytest_suites_use_tags_basic(testdir):
    testdir.makeconftest("""
    from pytest_suites import add_suite

    pytest_plugins = ['suites']
    add_suite(name="basic", pattern="*")
    """)
    
    testdir.makepyfile("""
    def test_gcp(suite):
        mode = suite.tags.get('mode', 'basic')
        if mode == 'extended':
            assert 0
        else:
            assert True
    """)

    result = testdir.runpytest("--verbose", "--suite", "basic")
    result.stdout.fnmatch_lines("*test_gcp PASSED*")


def test_pytest_suites_use_tags_extended(testdir):
    testdir.makeconftest("""
    from pytest_suites import add_suite

    pytest_plugins = ['suites']
    add_suite(name="superduper", pattern="*", tags={'mode': 'extended'})
    """)
    
    testdir.makepyfile("""
    def test_gcp(suite):
        mode = suite.tags.get('mode', 'basic')
        if mode == 'extended':
            assert 0
        else:
            assert True
    """)

    result = testdir.runpytest("--verbose", "--suite", "superduper")
    result.stdout.fnmatch_lines("*test_gcp FAILED*")


def test_pytest_suites_multiple_patterns(testdir):
    testdir.makeconftest("""
    from pytest_suites import add_suite

    pytest_plugins = ['suites']
    add_suite(name="multiple", pattern=["test_gcp", "test_aws"])
    """)
    
    testdir.makepyfile("""
    def test_gcp():
        assert True

    def test_aws():
        assert True

    def test_foo():
        assert True
    """)

    result = testdir.runpytest("--verbose", "--suite", "multiple")
    result.stdout.fnmatch_lines("*test_gcp PASSED*")
    result.stdout.fnmatch_lines("*test_aws PASSED*")
    with pytest.raises(_pytest.runner.Failed):
        result.stdout.fnmatch_lines("*test_foo*")


    
# def test_pytest_suites_multiple_patterns(testdir):

#     testdir.makepyfile("""
#     def test_gcp(suite):
#         mode = suite.tags.get('mode', 'basic')
#         if mode 
    
#     """)
