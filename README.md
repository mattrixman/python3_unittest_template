# Python3 Unittest Template

### Structure

The project is called `proj`

    .
    ├── proj
    │   ├── __init__.py
    │   └── Qux.py
    ├── test
    │   ├── __init__.py
    │   └── test_foo.py
    └── test_all.py

### Ways to run tests

##### Invoke the test run script:

    $ ./test_all.py
        F.
        ======================================================================
        FAIL: test_baz (test_foo.Bar)
        ----------------------------------------------------------------------
        Traceback (most recent call last):
          File "/home/matt/python_unittest_template/test/test_foo.py", line 14, in test_baz
            self.assertEqual('baz', proj.Qux.Quux())
        AssertionError: 'baz' != 'quux'
        - baz
        + quux
        ----------------------------------------------------------------------
        Ran 2 tests in 0.000s

        FAILED (failures=1)

##### Let unittest find them:

    $ python -m unittest
        F.
        ======================================================================
        FAIL: test_baz (test.test_foo.Bar)
        ----------------------------------------------------------------------
        Traceback (most recent call last):
          File "/home/matt/python_unittest_template/test/test_foo.py", line 14, in test_baz
            self.assertEqual('baz', proj.Qux.Quux())
        AssertionError: 'baz' != 'quux'
        - baz
        + quux


        ----------------------------------------------------------------------
        Ran 2 tests in 0.000s

        FAILED (failures=1)

----------------------------------------------------------------------
Ran 2 tests in 0.000s


##### Tell unittest which one to run

    $ python -m unittest test.test_foo.Bar.test_qux
        .
        ----------------------------------------------------------------------
        Ran 1 test in 0.000s

        OK

##### Tell unittest to run several

    $ python -m unittest test.test_foo.Bar
        F.
        ======================================================================
        FAIL: test_baz (test.test_foo.Bar)
        ----------------------------------------------------------------------
        Traceback (most recent call last):
          File "/home/matt/python_unittest_template/test/test_foo.py", line 14, in test_baz
            self.assertEqual('baz', proj.Qux.Quux())
        AssertionError: 'baz' != 'quux'
        - baz
        + quux


        ----------------------------------------------------------------------
        Ran 2 tests in 0.000s

        FAILED (failures=1)


