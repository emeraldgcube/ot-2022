import pygame
from pygame import display

class Renderer:
    def __init__(self, display, level, scale):
        self._display = display
        self._level = level
        self._scale = scale

    def render(self):
        self._display.fill((0, 0, 0))
        pygame.draw.rect(self._display, (15, 15, 155),
                         [int(7.4*self._scale), 0, int(self._scale*0.6), 22*self._scale])
        pygame.draw.rect(self._display, (15, 15, 155),
                         [int(18*self._scale), 0, int(self._scale*0.6), 22*self._scale])
        pygame.draw.rect(self._display, (0, 255, 0),
                         [0, 0, self._scale*7.4, self._scale*22])
        pygame.draw.rect(self._display, (0, 255, 0),
                         [int(18.6*self._scale), 0, self._scale*7.4, self._scale*22])
        pygame.draw.rect(self._display, (0, 0, 0),
                         [int(20*self._scale), int(2.5*self._scale), self._scale*4.6, self._scale*5])


        for row in range(0, 22):
            for column in range(0, 10):
                number=self._level.matrix[row][column]
                if number == 1:
                    color = 0, 255, 0
                if number == 2:
                    color = 0, 0, 255
                if number == 3:
                    color = 255, 255, 0
                if number == 4:
                    color = 255, 0, 255
                if number == 5:
                    color = 0, 255, 255
                if number == 6:
                    color = 100, 100, 255
                if number == 7:
                    color = 255, 0, 0
                if number == 0:
                    color = 0, 0, 0

                y_coord = row*self._scale
                x_coord = column*self._scale+8*self._scale
                pygame.draw.rect(self._display, color, 
                pygame.Rect(x_coord, y_coord, self._scale, self._scale))


        for a in range(0, 2):
            tetrimino = self._level.all_tetriminos[-(a+1)]
            if tetrimino.type == 1:
                color = 0, 255, 0
            if tetrimino.type == 2:
                color = 0, 0, 255
            if tetrimino.type == 3:
                color = 255, 255, 0
            if tetrimino.type == 4:
                color = 255, 0, 255
            if tetrimino.type == 5:
                color = 0, 255, 255
            if tetrimino.type == 6:
                color = 100, 100, 255
            if tetrimino.type == 7:
                color = 255, 0, 0
            for block in tetrimino.blocks[tetrimino.rotation%len(tetrimino.blocks)]:
                #field is supposed to start at (8,-2)
                y_coord = block[0]*self._scale+self._scale*tetrimino.position[0]
                x_coord = block[1]*self._scale+8*self._scale+self._scale*tetrimino.position[1]
                pygame.draw.rect(self._display, color, 
                pygame.Rect(x_coord, y_coord, self._scale, self._scale))

        pygame.display.flip()
