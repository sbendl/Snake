import random
import numpy as np
from Agents import *


class Snake:

    def __init__(self, head_loc, direction, board, agent=Greedy):
        self.head = tuple(head_loc)
        self.coords = [self.head, (self.head[0] - direction[0], self.head[1] - direction[1])]
        self.grow = False
        self.removed = ()
        self.board = board
        self.alive = True
        self.agent = agent

    def move(self):
        return self.agent(self)

    def tick(self):
        move = self.move()
        if not self.alive:
            return None

        self.head = tuple(move)
        self.coords = [self.head] + self.coords
        if not self.grow:
            self.removed = self.coords.pop()
        else:
            self.grow = False

        if self.board.board[self.head[0]][self.head[1]]:
            self.alive = False
        elif self.board.food_loc == self.head:
            self.grow = True
            return True

    def get_valid_moves(self):
        valid_moves = []

        for row, col in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            new_row = self.head[0] + row
            new_col = self.head[1] + col
            if not self.board.board[new_row][new_col]:
                valid_moves.append((new_row, new_col))

        return valid_moves


class Board:

    def __init__(self, size=(10,10), num_snakes=1):
        self.snakes = []
        self.size = size

        for _ in range(num_snakes):
            head = (random.randint(2, size[0]-2), random.randint(2, size[1]-2))
            offset = (abs(head[0] - size[0]), abs(head[1] - size[1]))
            if offset[0] <= offset[1]:
                direction = (-1 if head[0] <= size[0] else 0, 0)
            else:
                direction = (0, -1 if head[1] <= size[1] else 0)
            self.snakes.append(Snake(head, direction, self))

        self.board = [[True for i in range(size[0] + 2)]] + [[True] + [False for i in range(size[0])] + [True] for row in range(size[1])] + [[True for i in range(size[0] + 2)]]

        for snake in self.snakes:
            for row, col in snake.coords:
                self.board[row][col] = True

        self.add_food()

    def tick(self):
        for snake in self.snakes:
            ret = snake.tick()
            if ret:
                self.add_food()
            self.board[snake.head[0]][snake.head[1]] = True
            self.board[snake.removed[0]][snake.removed[1]] = False

    def add_food(self):
        self.food_loc = tuple(random.choice(list(zip(*np.where(~np.array(self.board))))))

    def __str__(self):
        b = [["X" if i else '.' for i in row] for row in self.board]
        b[self.food_loc[0]][self.food_loc[1]] = 'O'
        return '\n'.join([''.join(row) for row in b])
