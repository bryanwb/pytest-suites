__version__ = '0.0.1'


_available_suites = []


class SuiteNotFoundError(Exception):
    pass


class Suite():

    def __init__(self, name=None, pattern=None, description=None, tags={}):
        assert name is not None, "You must specify the name keyword when creating a suite"
        assert pattern is not None, "You must specify the pattern keyword when creating a suite"
        self.name = name
        self.pattern = pattern
        self.description = description
        self.tags = tags


def add_suite(name=None, pattern=None, description=None, tags={}):
    '''Adds a suite with the specified properties to the list of available suites

    name - name of suite, must be unique
    pattern - UNIX style glob to filter tests or a list of UNIX style globs
    description - description of suite
    tags - dictionary of arbitrary values, useful for communicating properties of
    specified suite to running tests
    '''
    assert name not in [s.name for s in _available_suites], "A suite with the name %s already exists" % name
    _available_suites.append(Suite(name=name, pattern=pattern, description=description, tags=tags))

        
default_suite = Suite(name="default",
                      pattern="*",
                      description="The default suite, matches all tests")

_available_suites.append(default_suite)


def lookup(suite_name):
    found_suite = filter(lambda s: s.name == suite_name, _available_suites)
    if len(found_suite) < 1:
        available_suite_names = [s.name for s in _available_suites]
        raise SuiteNotFoundError("Could not find a suite with the name %s. "
                                  "Available suites are %s." 
                                  % (suite_name, ", ".join(available_suite_names)))
    return found_suite[0]
