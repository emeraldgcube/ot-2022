from entities.tetrimino import Tetrimino
from services.hiscore import Hiscore

class Level:
    """class for gamefield aka level. 
    args: random (random number generator)
    """
    def __init__(self, random):
        """initialized gamefield
        args: random for random number generator"""
        self.speed = 1
        self.matrix = []
        self.all_tetriminos = []
        self._random = random
        # generate matrix
        for row in range(0, 22):
            self.matrix.append([])
            for _ in range(0, 10):
                self.matrix[row].append(0)
        # generates one block before adding new one on playfield
        self._generate_tetrimino()
        self._new_tetrimino()
        self.game_over = False
        self.score = 0
        self.hiscore = Hiscore()
        self.control = ""

    def _generate_tetrimino(self):
        """generates new tetrimino object using self._random"""
        random = self._random.randint_one_to_seven() # tetrimino types 1-7
        tetrimino = Tetrimino(random)
        self.all_tetriminos.append(tetrimino)

    def _new_tetrimino(self):
        """ protocol for when a block lands:
            use generate_tetrimino
            makes landed tetrimino as part of matrix 
            check for game over"""
        self._generate_tetrimino()
        if len(self.all_tetriminos) > 2:
            tetrimino = self.all_tetriminos[-3]
            block_rotation = tetrimino.rotation % len(tetrimino.blocks)
            for block in range(0, 4):
                block_positions = tetrimino.blocks[block_rotation][block]
                tetrimino_pos = tetrimino.position
                index_1 = block_positions[0] + tetrimino_pos[0]
                index_2 = block_positions[1] + tetrimino_pos[1]
                self.matrix[index_1][index_2] = tetrimino.type
            self._check_for_full_row()
        tetrimino_being_played = self.all_tetriminos[-2]
        tetrimino_being_played.position = (0, 4)
        if self.intersects(tetrimino_being_played.position, tetrimino_being_played.rotation):
            self._game_over()

    def _game_over(self):
        """ used when game ends """
        self.game_over = True
        self.hiscore.add_score(self.score)

    def _check_for_full_row(self):
        """ checks for full row(s) """
        cleared_rows = 0
        for row in range(0, 22):
            block_amount = 0
            for block in self.matrix[row]:
                if block != 0:
                    block_amount += 1
            if block_amount == 10:
                self._clear_row(row)
                cleared_rows += 1
                self.score += 50
        if cleared_rows == 4:
            self.score += 100


    def _clear_row(self, cleared_row):
        """ used to clear full row """
        for row in range(0, cleared_row):
            #moves columns downwards by one starting from the lowest
            for block in range(10):
                self.matrix[cleared_row-row][block] = self.matrix[cleared_row-row-1][block]


    def controls(self, control):
        """ controls current piece """
        self.control = control
        current_piece = self.all_tetriminos[-2]
        position = current_piece.position
        angle = current_piece.rotation
        if self.control == "left":
            newpos = position[0], position[1]-1
            if not self.intersects(newpos, angle):
                current_piece.position = newpos

        if self.control == "right":
            newpos = position[0], position[1]+1
            if not self.intersects(newpos, angle):
                current_piece.position = newpos

        if self.control == "down":
            newpos = position[0] + 1, position[1]
            if self.intersects(newpos, angle):
                self._new_tetrimino()
            else:
                current_piece.position = newpos

        if self.control == "drop":
            newpos = position[0] + 1, position[1]
            self.controls("down")
            if not self.intersects(newpos, angle):
                self.controls("drop")

        if self.control == "rotate":
            newangle = current_piece.rotation + 1
            if not self.intersects(position, newangle):
                current_piece.rotate()

        self.control = ""


    def intersects(self, newpos, angle):
        """Checks for intersecting blocks on path of each block of tetrimino.
        Parameters: newpos (new position) and angle (new angle)
        """
        tetrimino = self.all_tetriminos[-2]
        oldpos = tetrimino.position
        y_difference = oldpos[0] - newpos[0]
        x_difference = oldpos[1] - newpos[1]
        current_rotation = tetrimino.blocks[angle%len(tetrimino.blocks)]
        for block in current_rotation:
            y_coord = block[0]+oldpos[0] - y_difference
            x_coord = block[1]+oldpos[1] - x_difference
            if (y_coord >= 22 or
                    x_coord >= 10 or
                    x_coord < 0 or
                    self.matrix[y_coord][x_coord] != 0):
                return True
        return False
