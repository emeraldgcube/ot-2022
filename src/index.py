import pygame
from entities.level import Level
from renderer import Renderer
from services.game_loop import GameLoop
from event_queue import EventQueue
from neededthings.clock import Clock
from neededthings.randomgenerator import Random

def main():
    pygame.init()
    pygame.display.set_caption("Tetris")
    #new_game()
    scale = 30
    screen_width = 26*scale
    screen_height = 22*scale
    window = pygame.display.set_mode((screen_width, screen_height))
    clock = Clock()
    random = Random()
    level = Level(random)
    event_queue = EventQueue()
    renderer = Renderer(window, level, scale)
    loop = GameLoop(level, renderer, event_queue, clock)
    loop.start()

if __name__ == "__main__":
    main()
    
