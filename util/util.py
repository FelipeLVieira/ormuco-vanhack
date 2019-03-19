#!/usr/bin/env python
def try_float(value):
    try:
        return float(value)
    except ValueError:
        print("Error parsing value {} to float".format(value))
        return None


def generate_data(n=5):
    users = []
    for i in range(1, n + 1):
        username = 'user{}'.format(i)
        email = '{}@gmail.com'.format(username)
        user = Data(username, email)
        users.append(user)
    return users
