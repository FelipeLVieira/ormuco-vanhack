#!/usr/bin/env python
import time
from collections import OrderedDict


class LRUCache:

    def __init__(self, size=10, expiry=3600, region='BR'):
        self.size = size
        self.expiry = expiry
        self.cache = OrderedDict()
        self.region = region
        self._head = None

    @property
    def lru(self):
        return self._head

    def put(self, data):
        ts = time.time()
        # data is new
        if data.key not in self.cache:
            self.cache[data.key] = (data, ts)
            data.write(self.region)
        # data is already in the cache
        else:
            del self.cache[data.key]
            self._head = list(self.cache.keys())[0]

        if self._head is None:
            self._head = data.key

        if len(self.cache) > self.size:
            lru_data, _ = self.cache[self._head]
            lru_data.delete(self.region)
            del self.cache[self._head]
            self._head = list(self.cache.keys())[0]

    def get(self, key):
        if self.in_cache(key):
            data, _ = self.cache[key]
            del self.cache[key]
            self.cache[key] = (data, time.time())
            data.read()
            return data
        raise KeyError('key {} not in cache'.format(key))

    def in_cache(self, key):
        return key in self.cache

    def is_empty(self):
        return len(self.cache) == 0

    def drop_expired(self):
        if self.is_empty():
            return
        head_ts = self.cache[self._head][1]
        while time.time() - head_ts > self.expiry:
            if len(self.cache) == 1:
                del self.cache[self._head]
                self._head = None
                return
            nxt = list(self.cache.keys())[1]
            del self.cache[self._head]
            self._head = nxt
            head_ts = self.cache[self._head][1]

    def __len__(self):
        return len(self.cache)

    def __contains__(self, key):
        return key in self.cache
