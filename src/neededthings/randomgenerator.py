import random
class Random:
    def __init__(self):
        self._random = random

    def randint_one_to_seven(self):
        return random.randint(1, 7)
