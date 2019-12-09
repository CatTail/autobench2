# -*- coding: utf-8 -*-

from .context import autobench2

import unittest


class AdvancedTestSuite(unittest.TestCase):
    """Advanced test cases."""

    def test_thoughts(self):
        self.assertIsNone(autobench2.hmm())


if __name__ == '__main__':
    unittest.main()
