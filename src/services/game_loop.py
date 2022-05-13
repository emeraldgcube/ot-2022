import sys
import os
import pygame

class GameLoop:
    def __init__(self, level, renderer, event_queue, clock):
        self._level = level
        self._renderer = renderer
        self._event_queue = event_queue
        self._clock = clock
        """set timer for block to fall"""
        self._clock.set_timer(25, int(1000/self._level.speed))
        self.stop_loop = False

    def start(self):
        while not self._level.game_over and not self.stop_loop:
            self.go_through_events_during_game()
            self._renderer.render_game()
            self._clock.tick(60)

        while self._level.game_over and not self.stop_loop:
            self.go_through_events_in_hiscore()
            self._renderer.render_game_and_hiscore()
            self._clock.tick(30)
            

    def go_through_events_during_game(self):
        for event in self._event_queue.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self._level.controls("left")
                if event.key == pygame.K_RIGHT:
                    self._level.controls("right")
                if event.key == pygame.K_SPACE:
                    self._level.controls("drop")
                if event.key == pygame.K_DOWN:
                    self._level.controls("down")
                if event.key == pygame.K_UP:
                    self._level.controls("rotate")
                    #rotating clockwise and counter-clockwise
                if event.key == pygame.K_a:
                    self._level.controls("countercw")
                if event.key == pygame.K_d:
                    self._level.controls("cw")

            if event.type == 25:
                self._level.controls("down")

            # for testing
            if event.type == "stop_loop":
                self.stop_loop = True

    def go_through_events_in_hiscore(self):
        for event in self._event_queue.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                os.execl(sys.executable, sys.executable, *sys.argv)

            # for testing
            if event.type == "stop_loop":
                self.stop_loop = True
