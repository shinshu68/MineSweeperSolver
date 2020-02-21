from minesweeper_solver.square import Square

class Field(object):
    """NxMマスのフィールドを表現する"""
    def __init__(self, n, m):
        self.size_x = n
        self.size_y = m
        self.field = [[Square(j, i) for i in range(n)] for j in range(m)]

    def __getitem__(self, i):
        return self.field[i]

    def __str__(self):
        line = ["".join(map(str, i)) for i in self.field]
        return '\n'.join(map(str, line))

    def get_around(self, x, y):
        return list(map(lambda li: li[max(0, x-1):min(x+2, self.size_x)], self.field[max(0, y-1):min(y+2, self.size_y)]))

