import random


class Snake:

    def __init__(self, head_loc, direction, board):
        self.head = tuple(head_loc)
        self.coords = [self.head, (self.head[0] - direction[0], self.head[1] - direction[1])]
        self.direction = direction
        self.grow = False
        self.removed = ()
        self.board = board

    def move(self):
        self.head = (self.head[0] + self.direction[0], self.head[1] + self.direction[1])
        self.coords = [self.head] + self.coords
        if not self.grow:
            self.removed = self.coords.pop()

    def get_valid_moves(self):
        valid_moves = []

        for row, col in [(1,0), (0, 1), (-1, 0), (0, -1)]:
            if not self.board[row][col]:
                valid_moves.append((row, col))

        return valid_moves


class Board:

    def __init__(self, size=(10,10), num_snakes=1):
        self.snakes = []

        for _ in range(num_snakes):
            head = (random.randint(2, size[0]-2), random.randint(2, size[1]-2))
            offset = (abs(head[0] - size[0]), abs(head[1] - size[1]))
            if offset[0] <= offset[1]:
                direction = (1 if head[0] <= size[0] else 0, 0)
            else:
                direction = (0, 1 if head[1] <= size[1] else 0)
            self.snakes.append(Snake(head, direction, self))

        self.board = [[False for i in range(size[0])] for row in range(size[1])]

        for snake in self.snakes:
            for row, col in snake.coords:
                self.board[row][col] = True

    def tick(self):
        for snake in self.snakes:
            snake.move()
            self.board[snake.head[0]][snake.head[1]] = True
            self.board[snake.removed[0]][snake.removed[1]] = False



    def __str__(self):
        return '\n'.join(['|' + ''.join(["X" if i else '.' for i in row]) + '|' for row in self.board])
