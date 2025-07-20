from maze import Maze
from solver import MazeSolver
from player import Player

class Game:
    def __init__(self, maze: Maze, solver: MazeSolver):
        self.maze = maze
        self.solver = solver
        self.player = Player(maze.start)
        self.path = []  # TODO: Store the solution path

    def run(self):
        pass  # TODO: Main game loop: display, get input, move player, check win 