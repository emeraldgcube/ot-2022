import pygame

class Clock:
    """ Class for using pygame's time.Clock """
    def __init__(self):
        """ Initialize class """
        self._clock = pygame.time.Clock()

    def tick(self, fps):
        """ tick
        params: fps
        use to get as many frames a second as you enter"""
        self._clock.tick(fps)

    def set_timer(self, whatsets, time):
        """ sets timer on clock
        parameters: whatsets for what the timer sets,
                    time for how often """
        return pygame.time.set_timer(whatsets, time)
        