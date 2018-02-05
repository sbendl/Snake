import math

def Stupid(snake):
    return add(snake.head,snake.direction)

def Greedy(snake):
    f = snake.board.food_loc
    h = snake.head

    best_choice = None
    shortest = math.inf
    valid_moves = snake.get_valid_moves()
    if not valid_moves:
        snake.alive = False
        return h
    for choice in valid_moves:
        if dist(choice, f) < shortest:
            shortest = dist(choice, f)
            best_choice = choice
    return best_choice


def add(l1, l2):
    return [l1[0] + l2[0], l1[1] + l2[1]]

def sub(l1, l2):
    return [l1[0] - l2[0], l1[1] - l2[1]]

def dist(l1, l2):
    return abs(l1[0] - l2[0]) + abs(l1[1] - l2[1])