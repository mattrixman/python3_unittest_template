import unittest
import proj

import IPython

class Bar(unittest.TestCase):

    # This test pases
    def test_qux(self):
        self.assertEqual('quux', proj.Qux.Quux())
    
    # This test fails
    def test_baz(self):
        self.assertEqual('baz', proj.Qux.Quux())
