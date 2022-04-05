import unittest
from ..level import Level
from ..game_loop import GameLoop

class StubClock:
    def tick(self, fps):
        pass

    def set_timer(self, event, ms):
        0

class StubEventQueue:
    def __init__(self, events=None):
        self._events = events

    def get(self):
        return self._events

class StubRandom:
    def __init__(self):
        self.done = 0

    def randint_one_to_seven(self):
        if self.done == 0:
            self.done+=1
            return 7
        elif self.done == 1:
            return 5
        return

class StubRenderer:
    def render(self):
        pass

class TestLevel(unittest.TestCase):
    def setUp(self):
        self.level = Level(StubRandom())

    def test_blocks_get_generated(self):
        loop = GameLoop(self.level, StubRenderer(), StubEventQueue(), StubClock())


        self.assertEqual(self.level.all_tetriminos,
        [[7, [[(0, 0), (0, 1), (1, 0), (1, 1)]], (0, 4), 0],
         [5, [[(0, 0), (1, 0), (1, 1), (2, 1)], [(1, 0), (1, 1), (0, 1), (0, 2)]], (3, 13), 0]])

  #  def test_block_2(self:
       # level=Level(StubIO()))

