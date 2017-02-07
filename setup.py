from setuptools import setup

setup(
    name='pytest-suites',
    description='pytest plugin that allows you to group your tests for more granular execution',
    long_description=open("README.rst").read(),
    version='0.0.1',
    author='Bryan W. Berry',
    author_email='bryan.berry@gmail.com',
    url='https://github.com/bryanwb/pytest-suites',
    packages=['pytest_suites'],
    entry_points={'pytest11': ['suites = pytest_suites.plugin']},
    install_requires=['pytest'],
    classifiers=['Development Status :: 3 - Alpha',
                 'Intended Audience :: Developers',
                 'License :: OSI Approved :: MIT License',
                 'Operating System :: POSIX',
                 'Operating System :: Microsoft :: Windows',
                 'Operating System :: MacOS :: MacOS X',
                 'Topic :: Software Development :: Testing',
                 'Topic :: Software Development :: Libraries',
                 'Topic :: Utilities',
                 'Programming Language :: Python'],
)
