# -*- coding: utf-8 -*-

import unittest

def alltests(): # for setuptools
    return _alltests()

def _alltests():
    import tests
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    for t in tests.__all__:
        suite.addTest(loader.loadTestsFromName('tests.%s' % t))
    return suite

if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1:
        suite = unittest.TestSuite()
        for test in sys.argv[1:]:
            suite.addTest(unittest.TestLoader().loadTestsFromName(test))
    else:
        suite = _alltests()
    unittest.TextTestRunner(verbosity=2).run(suite)
