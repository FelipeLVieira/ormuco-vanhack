#!/usr/bin/env python
import time
import unittest

from question_c.data import Data
from question_c.lru_cache import LRUCache
from util.util import generate_data


class TestCache(unittest.TestCase):

    def test_expiry(self):
        cache = LRUCache(size=1000, expiry=2, region='BR')
        users = generate_data(n=5)
        for user in users:
            cache.put(user)

        # cache has 5 items?
        self.assertEqual(len(cache), 5)

        # sleep for 3 seconds, all items expired?
        time.sleep(3)
        cache.drop_expired()
        self.assertTrue(cache.is_empty())

        # remove expired items
        user1 = users[0]
        cache.put(user1)
        time.sleep(2)
        for user in users[1:]:
            cache.put(user)
        cache.drop_expired()
        self.assertEqual(len(cache), 4)

    def test_capacity(self):
        cache = LRUCache(size=3, expiry=1000, region='BR')
        users = generate_data(n=5)
        for user in users:
            cache.put(user)

        self.assertEqual(cache.lru, users[2].key)


if __name__ == '__main__':
    unittest.main()
