import unittest

from __init__ import get_score


tc = unittest.TestCase()
tc.assertEqual(8, get_score('A', 'Y'))
tc.assertEqual(1, get_score('B', 'X'))
tc.assertEqual(6, get_score('C', 'Z'))
