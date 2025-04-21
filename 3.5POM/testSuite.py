import unittest
from test_homePage import Testing_HomePage
from test_CreateNewProfile import Testing

test_HomePage = unittest.TestLoader().loadTestsFromTestCase(Testing_HomePage)
test_CreateNewProfile = unittest.TestLoader().loadTestsFromTestCase(Testing)

test_suite = unittest.TestSuite([test_HomePage, test_CreateNewProfile])

unittest.TextTestRunner(verbosity=2).run(test_suite)