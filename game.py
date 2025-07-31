from maze import Maze
from solver import MazeSolver
from player import Player

class Game:
    def __init__(self, maze: Maze, solver: MazeSolver):
        self.maze = maze
        self.solver = solver
        self.player = Player(maze.start)
        self.path = solver.solve(maze)

    def run(self):
        while True:
            self.maze.display(self.player.position, self.path)
            
            if self.player.position == self.maze.end:
                print("Congratulations! You've reached the end!")
                break
            
            move = input("Enter move (w/a/s/d or q to quit): ").lower()
            
            if move == 'q':
                print("Game ended.")
                break
            elif move == 'w':
                self.player.move('up', self.maze)
            elif move == 's':
                self.player.move('down', self.maze)
            elif move == 'a':
                self.player.move('left', self.maze)
            elif move == 'd':
                self.player.move('right', self.maze) 