# -*- coding: utf-8 -*-

from .context import {{cookiecutter.project_slug}}

import unittest


class AdvancedTestSuite(unittest.TestCase):
    """Advanced test cases."""

    def test_thoughts(self):
        self.assertIsNone( {{cookiecutter.project_slug}}.hmm())


if __name__ == '__main__':
    unittest.main()
