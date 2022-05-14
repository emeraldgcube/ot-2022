import pygame
from services.hiscore import Hiscore

class Renderer:
    """ Class that takes care of rendering in pygame """

    def __init__(self, display, level, scale):
        """Initialize renderer.
        args: display aka the pygame window
              level for rendering pieces of level
              scale for future scaling of game window
        """
        self._display = display
        self._level = level
        self._scale = scale


    def render_text(self, text, color, size, x_coord, y_coord):
        """ renders text in wanted position, size and color
        parameters: text, color, size, x_coord, y_coord
        """
        font = pygame.font.SysFont("Arial", int(size*self._scale))
        if color == "red":
            color = (255, 100, 0)
        if color == "blue":
            color = (0, 0, 255)
        score = font.render(text, True, color)
        self._display.blit(score, (int(x_coord*self._scale), int(y_coord*self._scale)))

    def render_game(self):
        """ renders the window during game."""
        self.render_edges()
        self.render_matrix()
        self.render_blocks_not_set_yet()
        self.render_score()
        pygame.display.flip()

    def render_game_and_hiscore(self):
        """ renders game in the background and hiscore on top of it.
         used after the game has ended. """
        self.render_edges()
        self.render_matrix()
        self.render_blocks_not_set_yet()
        self.render_score()
        self.render_text("GAME OVER", "blue", 1, 0.8, 8)
        self.render_text("AGAIN?", "orange", 1.2, 1.6, 10)
        self.render_hiscore()
        pygame.display.flip()

    def render_hiscore(self):
        """ own function for rendering hiscore """
        hiscore = Hiscore()
        pygame.draw.rect(
            self._display,
            (192, 192, 192),
            [self._scale * 8, self._scale * 1, self._scale*16, self._scale*19]
            )
        five_best = hiscore.get_top_five()
        own_best = hiscore.get_highest_own()[0]
        five_best.append(("Your Best", own_best))
        for item in range(6):
            print(five_best)
            name = five_best[item][0]
            score = five_best[item][1]
            self.render_text(str(name), "yellow", 1.6, 10, 3*item+2)
            self.render_text(str(score), "yellow", 1.6, 18, 3*item+2)

    def render_score(self):
        """ renders score on gamefield """
        self.render_text(str(self._level.score), "red", 2, 2, 4)

    def render_edges(self):
        """ renders edges on field """
        # renders edges
        self._display.fill((0, 0, 0))
        pygame.draw.rect(self._display, (15, 15, 155),
                         [int(7.4*self._scale), 0, int(self._scale*0.6), 22*self._scale])
        pygame.draw.rect(
            self._display,
            (15, 15, 155),
            [int(18*self._scale), 0, int(self._scale*0.6), 22*self._scale]
            )
        pygame.draw.rect(
            self._display,
            (0, 255, 0),
            [0, 0, self._scale*7.4, self._scale*22]
            )
        pygame.draw.rect(
            self._display,
            (0, 255, 0),
            [int(18.6*self._scale), 0, self._scale*7.4, self._scale*22]
        )
        pygame.draw.rect(
            self._display,
            (0, 0, 0),
            [int(20*self._scale), int(2.5*self._scale), self._scale*4.6, self._scale*5]
        )

    def render_matrix(self):
        """ renders each block in matrix"""
        for row in range(0, 22):
            for column in range(0, 10):
                number = self._level.matrix[row][column]
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

    def render_blocks_not_set_yet(self):
        """ renders the two last tetriminos in array, making moving and "next" block visible """
        for number in range(0, 2):
            tetrimino = self._level.all_tetriminos[-(number+1)] # indice -1 and -2
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
