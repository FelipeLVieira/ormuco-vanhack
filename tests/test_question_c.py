#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import unittest

from app.question_c.lru_cache import LRUCache
from util.helper import generate_data


class TestCache(unittest.TestCase):

    def test_cache_filled(self):
        cache = LRUCache(size=1000, expiry=1000, region='BR')
        users = generate_data(n=5)
        for user in users:
            cache.put(user)

        # cache has 5 items?
        print("Check if cache has five items: " + str(len(cache)))
        self.assertEqual(len(cache), 5)

    def test_cache_expired(self):
        cache = LRUCache(size=1000, expiry=1000, region='BR')
        # sleep for 3 seconds, all items expired?
        time.sleep(3)
        cache.drop_expired()
        print("Check if all values with 1 second life expired \n"
              "after three seconds: " + str(cache.is_empty()))
        self.assertTrue(cache.is_empty())


if __name__ == '__main__':
    unittest.main()
