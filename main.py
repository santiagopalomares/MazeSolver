from maze import Maze
from solver import DFSMazeSolver
from game import Game

if __name__ == "__main__":
    grid = [
        ['S', 0, 1, 0, 'E'],
        [1, 0, 1, 0, 1],
        [0, 0, 0, 0, 0],
    ]  # TODO: Replace with dynamic input or file loading
    maze = Maze(grid)
    solver = DFSMazeSolver()
    game = Game(maze, solver)
    game.run()  # TODO: Implement game loop 