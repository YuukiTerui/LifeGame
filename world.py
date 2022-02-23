import numpy as np


class World:
    def __init__(self, length=5) -> None:
        self.size = length
        self.now = np.zeros((length, length), dtype=np.int)
        self.history = []

    def __call__(self, i=None, j=None):
        if i!=None and j!=None:
            return self.now[i][j]
        else:
            return self.now

    def create_random(self):
        self.now = [[np.random.randint(0, 2) for _ in range(self.size)] for _ in range(self.size)]

    def inversion(self, i, j):
        self.now[i][j] = 0 if self.now[i][j] == 1 else 1

    def clear(self):
        self.now = np.zeros_like(self.now)

    def fill_all(self):
        self.now = np.ones_like(self.now)

    def update(self):
        next_world = np.zeros_like(self.now)
        for i in range(self.size):
            for j in range(self.size):
                next_world[i][j] = self.calc(i, j)
        self.history.append(self.now)
        self.now = next_world

    def calc(self, i, j):
        n = self.size
        cnt = 0
        for x in range(i-1, i+2):
            for y in range(j-1, j+2):
                cnt += self.now[(x+n)%n][(y+n)%n]
        cnt -= self.now[i][j]
        if cnt == 3:
            return 1
        elif cnt == 2:
            return self.now[i][j]
        else:
            return 0
