class Tetrimino:
    def __init__(self, random):
        self.type = random
        self.blocks = self.get_blocks()
        self.position = (3, 13)
        self.rotation = 0

    def rotate(self):
        self.rotation += 1

    def get_blocks(self):
        if self.type == 1: # T
            blocks = [[(0, 1), (1, 0), (1, 1), (2, 1)], [(0, 0), (0, 1), (0, 2), (1, 1)],
                      [(0, 0), (1, 0), (1, 1), (2, 0)], [(0, 1), (1, 0), (1, 1), (1, 2)]]
        if self.type == 2: # L
            blocks = [[(0, 0), (0, 1), (0, 2), (1, 0)], [(0, 0), (1, 0), (2, 0), (2, 1)],
                      [(1, 0), (1, 1), (1, 2), (0, 2)], [(0, 0), (0, 1), (1, 1), (2, 1)]]
        if self.type == 3: # J
            blocks = [[(0, 0), (1, 0), (1, 1), (1, 2)], [(2, 0), (2, 1), (1, 1), (0, 1)],
                      [(0, 0), (0, 1), (0, 2), (1, 2)], [(0, 0), (0, 1), (1, 0), (2, 0)]]
        if self.type == 4: # I
            blocks = [[(0, 1), (1, 1), (2, 1), (3, 1)], [(1, 0), (1, 1), (1, 2), (1, 3)]]
        if self.type == 5: # S
            blocks = [[(0, 0), (1, 0), (1, 1), (2, 1)], [(1, 0), (1, 1), (0, 1), (0, 2)]]
        if self.type == 6: # Z
            blocks = [[(1, 0), (2, 0), (0, 1), (1, 1)], [(0, 0), (0, 1), (1, 1), (1, 2)]]
        if self.type == 7: # O
            blocks = [[(0, 0), (0, 1), (1, 0), (1, 1)]]
        return blocks
