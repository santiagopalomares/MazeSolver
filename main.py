from maze import Maze
from solver import DFSMazeSolver
from game import Game

if __name__ == "__main__":
    # Create a more interesting maze layout
    grid = [
        ['S', 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 0, 1, 1, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 'E']
    ]
    
    maze = Maze(grid)
    solver = DFSMazeSolver()
    game = Game(maze, solver)
    game.run() 