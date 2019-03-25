#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import unittest

from app.question_c.lru_cache import LRUCache
from util.helper import generate_data


class TestCache(unittest.TestCase):

    def test_expiry(self):
        cache = LRUCache(size=1000, expiry=1000, region='BR')
        users = generate_data(n=5)
        for user in users:
            cache.put(user)

        # cache has 5 items?
        self.assertEqual(len(cache), 5)

        # sleep for 3 seconds, all items expired?
        time.sleep(3)
        cache.drop_expired()
        print("In cache: " + str(cache.cache))
        self.assertFalse(cache.is_empty())

        # remove expired items
        user1 = users[0]
        cache.put(user1)
        time.sleep(3)
        cache.drop_expired()
        self.assertEqual(len(cache), 4)


if __name__ == '__main__':
    unittest.main()
