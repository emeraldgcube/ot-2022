import unittest
from entities.level import Level
from services.game_loop import GameLoop
import pygame

class StubClock:
    def tick(self, fps):
        pass

    def set_timer(self, event, ms):
        0

class StubEvent:
    def __init__(self, type, key=None):
        self.type = type
        self.key = key

class StubEventQueue:
    def __init__(self, events=None):
        self._events = events

    def get(self):
        if self._events == None:
            return [StubEvent(25)]
        events = self._events
        self._events = None
        return events


class StubRandom:
    def __init__(self):
        self.done = 0

    def randint_one_to_seven(self):
        if self.done == 0:
            self.done+=1
            return 7
        elif self.done == 1:
            self.done+=1
            return 6
        elif self.done == 2:
            self.done+=1
            return 5
        elif self.done == 3:
            self.done+=1
            return 4
        elif self.done == 4:
            self.done+=1
            return 3

        elif self.done == 5:
            self.done+=1
            return 2

        elif self.done == 6:
            self.done+=1
            return 1
        else:
            return 1

class StubRenderer:
    def render_game(self):
        pass

    def render_game_and_hiscore(self):
        pass

class TestLevel(unittest.TestCase):
    def setUp(self):
        self.level = Level(StubRandom())
        self.s_sp = StubEvent(pygame.KEYDOWN, pygame.K_SPACE)
        self.s_d = StubEvent(pygame.KEYDOWN, pygame.K_DOWN)
        self.s_u = StubEvent(pygame.KEYDOWN, pygame.K_UP)
        self.s_l = StubEvent(pygame.KEYDOWN, pygame.K_LEFT)
        self.s_r = StubEvent(pygame.KEYDOWN, pygame.K_RIGHT)
        self.s_25 = StubEvent(25)

    def makeStubSpace(self):
        return StubEvent(pygame.KEYDOWN, pygame.K_SPACE)

    def test_blocks_get_generated(self):
        loop = GameLoop(self.level, StubRenderer(), StubEventQueue(), StubClock())
        types = map(lambda x: x.type, self.level.all_tetriminos)
        tetriminotypes = list(types)
        self.assertEqual(tetriminotypes, [7, 6])

    def test_movement_left(self):
        queue = StubEventQueue([self.s_l, StubEvent("stop_loop")])
        loop = GameLoop(self.level, StubRenderer(), queue, StubClock())
        loop.start()
        block_in_air = self.level.all_tetriminos[-2]
        self.assertEqual(block_in_air.position, (0, 3))

    def test_movement_right(self):
        queue = StubEventQueue([self.s_r, StubEvent("stop_loop")])
        loop = GameLoop(self.level, StubRenderer(), queue, StubClock())
        loop.start()
        block_in_air = self.level.all_tetriminos[-2]
        self.assertEqual(block_in_air.position, (0, 5))

    def test_movement_down(self):
        queue = StubEventQueue([self.s_d, StubEvent("stop_loop")])
        loop = GameLoop(self.level, StubRenderer(), queue, StubClock())
        loop.start()
        block_in_air = self.level.all_tetriminos[-2]
        self.assertEqual(block_in_air.position, (1, 4))

    def test_movement_rotate(self):
        queue = StubEventQueue([self.s_u, StubEvent("stop_loop")])
        loop = GameLoop(self.level, StubRenderer(), queue, StubClock())
        loop.start()
        block_in_air = self.level.all_tetriminos[-2]
        self.assertEqual(block_in_air.rotation, 1)

    def test_stub_tetriminos_are_right(self):
        queue = StubEventQueue([self.s_sp, self.s_sp, self.s_sp, self.s_sp,
                                self.s_sp, self.s_sp, self.s_sp, self.s_sp,
                                StubEvent("stop_loop")])
        loop = GameLoop(self.level, StubRenderer(), queue, StubClock())
        loop.start()
        types = map(lambda x: x.type, self.level.all_tetriminos)
        tetriminotypes = list(types)
        self.assertEqual(tetriminotypes, [7, 6, 5, 4, 3, 2, 1, 1, 1, 1])

    def test_movement_dropdown(self):
        queue = StubEventQueue([self.s_sp, StubEvent("stop_loop")])
        loop = GameLoop(self.level, StubRenderer(), queue, StubClock())
        loop.start()
        self.assertEqual(len(self.level.all_tetriminos), 3)

    def test_moveset_clears_one_line(self):
        queue = StubEventQueue([self.s_sp, self.s_sp, self.s_sp,
                                self.s_r, self.s_r, self.s_u, self.s_sp,
                                self.s_l, self.s_l, self.s_l, self.s_l, 
                                self.s_sp, self.s_l, self.s_l, self.s_u,
                                self.s_u, self.s_u, self.s_sp, self.s_sp, 
                                self.s_d, self.s_25, StubEvent("stop_loop")])
        loop = GameLoop(self.level, StubRenderer(), queue, StubClock())
        loop.start()
        self.assertEqual(self.level.score, 50)

    def test_game_ends(self):
        self.s_sp = StubEvent(pygame.KEYDOWN, pygame.K_SPACE)
        queue = StubEventQueue([self.s_sp, self.s_sp, self.s_sp, 
                                self.s_sp, self.s_sp, self.s_sp, 
                                self.s_sp, self.s_sp, self.s_sp, 
                                self.s_sp, self.s_sp, self.s_sp, 
                                StubEvent("stop_loop")])
        loop = GameLoop(self.level, StubRenderer(), queue, StubClock())
        loop.start()
        self.assertEqual(self.level.game_over, True)