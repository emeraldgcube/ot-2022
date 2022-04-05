import tetrimino

class Level:
    def __init__(self, random):
        self.speed = 1
        self.matrix = []
        self.all_tetriminos = []
        self.control = ""
        self._random = random
        """generate matrix"""
        for row in range(0, 22):
            self.matrix.append([])
            for _ in range(0, 10):
                self.matrix[row].append(0)
        """generates one block before adding new one on playfield"""
        self._generate_tetrimino()
        self._new_tetrimino()
        self.game_over=False
        

    def _generate_tetrimino(self):
        tetrimino = self._random.randint_one_to_seven()
        if tetrimino == 1: # T
            blocks = [[(0, 1), (1, 0), (1, 1), (2, 1)], [(0, 0), (0, 1), (0, 2), (1, 1)],
                      [(0, 0), (1, 0), (1, 1), (2, 0)], [(0, 1), (1, 0), (1, 1), (1, 2)]]
        if tetrimino == 2: # L
            blocks = [[(0, 0), (0, 1), (0, 2), (1, 0)], [(0, 0), (1, 0), (2, 0), (2, 1)],
                      [(1, 0), (1, 1), (1, 2), (0, 2)], [(0, 0), (0, 1), (1, 1), (2, 1)]]
        if tetrimino == 3: # J
            blocks = [[(0, 0), (1, 0), (1, 1), (1, 2)], [(2, 0), (2, 1), (1, 1), (0, 1)],
                      [(0, 0), (0, 1), (0, 2), (1, 2)], [(0, 0), (0, 1), (1, 0), (2, 0)]]
        if tetrimino == 4: # I
            blocks = [[(0, 1), (1, 1), (2, 1), (3, 1)], [(1, 0), (1, 1), (1, 2), (1, 3)]]
        if tetrimino == 5: # S
            blocks = [[(0, 0), (1, 0), (1, 1), (2, 1)], [(1, 0), (1, 1), (0, 1), (0, 2)]]
        if tetrimino == 6: # Z
            blocks = [[(1, 0), (2, 0), (0, 1), (1, 1)], [(0, 0), (0, 1), (1, 1), (1, 2)]]
        if tetrimino == 7:
            blocks = [[(0, 0), (0, 1), (1, 0), (1, 1)]]
        self.all_tetriminos.append([tetrimino, blocks, (3, 13), 0])
                                 #  blocktypes, blocks, location, rotation
                                 #  x and y   ,
    def _new_tetrimino(self):
        self._generate_tetrimino()
        if len(self.all_tetriminos)>2:
            tetrimino=self.all_tetriminos[-3]
            for block in range(0, 4):
                block_positions = tetrimino[1][tetrimino[3]%len(tetrimino[1])][block]
                tetrimino_pos = tetrimino[2]
                index_1 = block_positions[0]+tetrimino_pos[0]
                index_2 = block_positions[1]+tetrimino_pos[1]
                self.matrix[index_1][index_2]=tetrimino[0]  
            self._check_for_full_row()
        self.all_tetriminos[-2][2] = (0, 4)
        if self.intersects(self.all_tetriminos[-2][2], self.all_tetriminos[-2][3]):
            self._game_over()


    def _game_over(self):
        self.game_over=True

    def _check_for_full_row(self):
        for row in range(0,22):
            block_amount=0
            for block in self.matrix[row]:
                if block != 0:
                    block_amount+=1
            if block_amount == 10:
                self._clear_row(row)

        
    def _clear_row(self, cleared_row):
        for row in range(0, cleared_row):
            """moves columns downwards by one starting from the lowest"""
            for block in range(10):
                self.matrix[cleared_row-row][block]=self.matrix[cleared_row-row-1][block]

                

    def controls(self):
        position = self.all_tetriminos[-2][2]
        if self.control == "left":
            newpos = position[0], position[1]-1
            angle = self.all_tetriminos[-2][3]
            if not self.intersects(newpos, angle):
                self.all_tetriminos[-2][2] = newpos
            self.control = ""

        if self.control == "down":
            newpos = position[0]+1, position[1]
            angle = self.all_tetriminos[-2][3]

            if self.intersects(newpos, angle):
                self._new_tetrimino()
            else:
                self.all_tetriminos[-2][2] = newpos
            self.control = ""

        if self.control == "right":
            newpos = position[0], position[1]+1
            angle = self.all_tetriminos[-2][3]
            if not self.intersects(newpos, angle):
                self.all_tetriminos[-2][2] = newpos
            self.control = ""

       # if self.control=="ccw":
        #    self.all_tetriminos[-2][1]
        # if self.control=="cw":
        #    self.all_tetriminos[-2]

        if self.control == "drop":
            newpos = position[0] + 1, position[1]
            angle = self.all_tetriminos[-2][3]

            if not self.intersects(newpos, angle):
                self.all_tetriminos[-2][2] = newpos
                self.control = "drop"
                self.controls()
        
            self.control = ""

        if self.control == "rotate":
            newangle = self.all_tetriminos[-2][3] + 1
            if not self.intersects(position, newangle):
                self.all_tetriminos[-2][3] += 1
            self.control = ""


    def intersects(self, position, angle):
        """Checks for intersecting blocks on path of block 
        """
        tetrimino = self.all_tetriminos[-2].copy()
        tetrimino[2] = position
        for block in tetrimino[1][angle%len(tetrimino[1])]:
            y_coord=block[0]+tetrimino[2][0]
            x_coord=block[1]+tetrimino[2][1]
            if (block[0]+tetrimino[2][0] >= 22 or
                    block[1]+tetrimino[2][1] >= 10 or
                    block[1]+tetrimino[2][1] < 0 or
                    self.matrix[y_coord][x_coord] != 0
                    ):
                return True
        return False
