from abc import ABC, abstractmethod
from maze import Maze

class MazeSolver(ABC):
    @abstractmethod
    def solve(self, maze: Maze):
        pass

class DFSMazeSolver(MazeSolver):
    def solve(self, maze: Maze):
        """Solve the maze using Depth-First Search algorithm."""
        visited = set()
        path = []
        
        def dfs(current_pos):
            if current_pos == maze.end:
                return True
            
            visited.add(current_pos)
            
            for neighbor in maze.get_neighbors(current_pos):
                if neighbor not in visited:
                    if dfs(neighbor):
                        path.append(neighbor)
                        return True
            
            return False
        
        # Start DFS from the start position
        if dfs(maze.start):
            path.append(maze.start)
            return path[::-1]  # Reverse to get start to end order
        else:
            return []  # No path found 