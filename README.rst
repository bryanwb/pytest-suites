Pytest-suites
--------------------


This plugin makes it easy to execute subsets of your tests.

This plugin determines which tests belong in a suite by applying UNIX-style glob
to the test function name. A suite consists of a name, pattern (glob) or patterns, and
additional metadata.


Usage
=========


First, add pytest-suites to your conftest.py

::

   # conftest.py

   pytest_plugins = ['suites']

Next you will likely want to define a suite or two. Also do this in ``conftest.py``


::

   # conftest.py

   from pytest_suites import add_suite

   add_suite(name="smoke", pattern="*basic*")
   add_suite(name="advanced", pattern="*")
   add_suite(name="extended", pattern="*", tags={'mode': 'extended'})

   
Meanwhile, add some tests::
  
  # my_test.py


  def test_basic_feature1():
      assert True

  def test_basic_feature2():
      assert True

  def test_advanced_feature1():
      assert True

  def test_advanced_feature1():
      assert True


Use the command-line option ``--suite SUITE`` to specify the suite

Executing ``pytest my_test.py --suite smoke`` will only execute the tests
`test_basic_feature1` and `test_basic_feature2`.

Likewise, ``pytest my_test.py --suite advanced`` will execute all tests.


pytest-suites provides a mechanism for running tests to learn what suite is
currently being executed and access the suite's tags dictionary. This can be
useful when you want to occasionally test less or greater functionality within a
given test. For example, you may frequently want `test_my_feature` to check the
common case but right before a release you may the same test to be more
exhaustive.::

  def test_advanced_feature1(suite):
      mode = suite.tags.get('mode', 'basic')
      if mode == 'extended':
          # test exhaustively
          assert do_expensive_operation()
      else:
          # test the common case
          assert True


Author
==========

Bryan W. Berry



License
==============

Copyright 2017 Bryan W. Berry

MIT License


   
