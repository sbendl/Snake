from lib import *

board = Board()

print(board)

while board.snakes[0].alive:
    board.tick()
    print(board)