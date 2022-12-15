#https://www.codewars.com/kata/5671d975d81d6c1c87000022

from itertools import permutations

def visible_number(line):
    return len(set(max(line[:i + 1]) for i in range(len(line))))

def is_valid(grid, clues):
    grid1 = tuple(zip(*grid))
    grid2 = tuple(row[::-1] for row in grid)
    grid3 = tuple(zip(*grid[::-1]))[::-1]
    grid4 = grid[::-1]
    for i, line in enumerate(grid1 + grid2 + grid3 + grid4):
        if i < 4 and set(line) != {1, 2, 3, 4}:
            return False
        if clues[i] and visible_number(line) != clues[i]:
            return False
    return True

def solve_puzzle(clues):
    for grid in permutations(permutations(range(1, 5)), r=4):
        if is_valid(grid, clues):
            return grid
    return