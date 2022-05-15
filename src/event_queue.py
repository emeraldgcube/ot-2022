import pygame

class EventQueue:
    """ class for getting events """

    def get(self):
        """ returns pygame.event.get() """
        return pygame.event.get()
        