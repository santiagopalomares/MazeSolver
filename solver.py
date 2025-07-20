from abc import ABC, abstractmethod
from maze import Maze

class MazeSolver(ABC):
    @abstractmethod
    def solve(self, maze: Maze):
        pass  # TODO: Return a list of positions from start to end

class DFSMazeSolver(MazeSolver):
    def solve(self, maze: Maze):
        pass  # TODO: Implement DFS algorithm 