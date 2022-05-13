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

    def makeStubSpace(self):
        return StubEvent(pygame.KEYDOWN, pygame.K_SPACE)

    def test_blocks_get_generated(self):
        loop = GameLoop(self.level, StubRenderer(), StubEventQueue(), StubClock())
        types = map(lambda x: x.type, self.level.all_tetriminos)
        tetriminotypes = list(types)
        self.assertEqual(tetriminotypes, [7, 6])

    def test_moveset_clears_one_line(self):
        stub_press_space = StubEvent(pygame.KEYDOWN, pygame.K_SPACE)
        stub_press_down = StubEvent(pygame.KEYDOWN, pygame.K_DOWN)
        stub_press_up = StubEvent(pygame.KEYDOWN, pygame.K_UP)
        stub_press_left = StubEvent(pygame.KEYDOWN, pygame.K_LEFT)
        stub_press_right = StubEvent(pygame.KEYDOWN, pygame.K_RIGHT)

        queue = StubEventQueue([stub_press_space, stub_press_space, stub_press_space,
                                stub_press_right, stub_press_right, stub_press_up, stub_press_space,
                                stub_press_left, stub_press_left, stub_press_left, stub_press_left, 
                                stub_press_space, stub_press_left, stub_press_left, stub_press_up,
                                stub_press_up, stub_press_up, stub_press_space, stub_press_space, 
                                stub_press_down, StubEvent("stop_loop")])
        loop = GameLoop(self.level, StubRenderer(), queue, StubClock())
        loop.start()
        #types = map(lambda x: x.type, self.level.all_tetriminos)
        #tetriminotypes = list(types)
        #self.assertEqual(tetriminotypes, [7, 6, 5, 4, 3, 2, 1, 1, 1])
        self.assertEqual(self.level.score, 50)

    def test_movement_dropdown(self):
        stub_press_space = StubEvent(pygame.KEYDOWN, pygame.K_SPACE)
        queue = StubEventQueue([stub_press_space, StubEvent("stop_loop")])
        loop = GameLoop(self.level, StubRenderer(), queue, StubClock())
        loop.start()
        self.assertEqual(len(self.level.all_tetriminos), 3)

    def test_game_ends(self):
        stub_press_space = StubEvent(pygame.KEYDOWN, pygame.K_SPACE)
        queue = StubEventQueue([stub_press_space, stub_press_space, stub_press_space, 
                                stub_press_space, stub_press_space, stub_press_space, 
                                stub_press_space, stub_press_space, stub_press_space, 
                                stub_press_space, stub_press_space, stub_press_space, 
                                StubEvent("stop_loop")])
        loop = GameLoop(self.level, StubRenderer(), queue, StubClock())
        loop.start()
        self.assertEqual(self.level.game_over, True)