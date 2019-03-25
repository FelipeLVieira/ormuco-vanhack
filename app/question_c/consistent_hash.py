#!/usr/bin/env python
# -*- coding: utf-8 -*-

import bisect
import hashlib


class ConsistentHash:

    def __init__(self, num_machines=1, num_replicas=1):
        self.num_machines = num_machines
        self.num_replicas = num_replicas
        hash_tuples = [(j, k, generate_hash(str(j) + "_" + str(k)))
                       for j in range(self.num_machines)
                       for k in range(self.num_replicas)]
        # Sort the hash tuples based on just the hash values
        hash_tuples.sort(key=lambda x, y: ((x[2] > y[2]) - (x[2] < y[2])))
        self.hash_tuples = hash_tuples

    def get_machine(self, key):
        # Returns the number of the machine which key gets sent to.
        h = generate_hash(key)
        # Edge case where we cycle past hash value of 1 and back to 0.
        if h > self.hash_tuples[-1][2]:
            return self.hash_tuples[0][0]
        hash_values = map(lambda x: x[2], self.hash_tuples)
        index = bisect.bisect_left(hash_values, h)
        return self.hash_tuples[index][0]


def generate_hash(key):
    # generate_hash(key) returns a hash in the range [0,1).
    return (int(hashlib.md5(key).hexdigest(), 16) % 1000000) / 1000000.0
