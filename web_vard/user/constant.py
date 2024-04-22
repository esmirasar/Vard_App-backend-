import random


base_random = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890'

RANDOM_STRING = ''.join([random.choice(base_random) for _ in range(100)])
