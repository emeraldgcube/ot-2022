import unittest
from level import Level

class StubIO:
    def __init__(self):
        self.done = 0

    def randint_zero_to_six(self):
        if self.done == 0:
            self.done+=1
            return 0
        elif self.done == 1:
            return 5
        return

class TestLevel(unittest.TestCase):
    def setUp(self):
        self.level = Level(StubIO())

    def test_block_generates(self):
        self.assertEqual(self.level.all_tetriminos,
        [[7, [[(0, 0), (0, 1), (1, 0), (1, 1)]], (0, 4), 0],
         [5, [[(0, 0), (1, 0), (1, 1), (2, 1)], [(1, 0), (1, 1), (0, 1), (0, 2)]], (3, 13), 0]])

  #  def test_block_2(self:
       # level=Level(StubIO()))

