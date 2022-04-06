import unittest
from level import Level
from game_loop import GameLoop

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
        types = map(lambda x: x.type, self.level.all_tetriminos)
        tetriminotypes = list(types)
        self.assertEqual(tetriminotypes, [7, 5])

  #  def test_block_2(self:
       # level=Level(StubIO()))

