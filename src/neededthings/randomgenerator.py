import random
class Random:
    """ Class used for random number generation """
    
    def __init__(self):
        """ initialize class"""
        self._random = random
        

    def randint_one_to_seven(self):
        """ call for a random integral number from between 1 to 7 """
        return random.randint(1, 7)
