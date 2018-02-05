

class Snake:

    def __init__(self, head_loc, direction):
        self.head = tuple(head_loc)
        self.coords = [self.head, (self.head[0] + direction[0], self.head[1] + direction[1])]
        self.direction = direction
        self.grow = False
        self.removed = ()

    def move(self):
        self.head = (self.head[0] + self.direction[0], self.head[1] + self.direction[1])
        self.coords = [self.head].extend(self.coords)
        if not self.grow:
            self.removed = self.coords.pop()


class Board:

    def __init__(self, size=[10,10], num_snakes=1):
