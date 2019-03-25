#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from app.question_b.compare import which_is_greater


class TestCompare(unittest.TestCase):

    def test1(self):
        print("Comparing '11.1' and '33.1':")
        which_is_greater("11.1", "33.1")

    def test2(self):
        print("Comparing 'a' and 'b':")
        which_is_greater("a", "b")

    def test3(self):
        print("Comparing '0.1' and '1.1':")
        which_is_greater("0.1", "1.1")


if __name__ == '__main__':
    unittest.main()
