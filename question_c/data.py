#!/usr/bin/env python
class Data:

    def __init__(self, key, value):
        self.key = key
        self.value = value

    def read(self):
        print('reading {} data from cache'.format(self.key))

    def write(self, region):
        print("writing {} data to {}".format(self.key, region))

    def delete(self, region):
        print("deleting {} data from {}".format(self.key, region))

    def __repr__(self):
        return 'key:{}, data:{}'.format(self.key, self.value)
