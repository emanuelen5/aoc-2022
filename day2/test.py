import unittest

import lib


tc = unittest.TestCase()
tc.assertEqual(8, lib.get_score('A', 'Y'))
tc.assertEqual(1, lib.get_score('B', 'X'))
tc.assertEqual(6, lib.get_score('C', 'Z'))

tc.assertEqual('X', lib.get_shape_for_outcome('A', 'Y'))
tc.assertEqual('X', lib.get_shape_for_outcome('B', 'X'))
tc.assertEqual('X', lib.get_shape_for_outcome('C', 'Z'))
