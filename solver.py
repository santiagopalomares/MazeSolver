from abc import ABC, abstractmethod
from collections import deque
import heapq
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

class BFSMazeSolver(MazeSolver):
    def solve(self, maze: Maze):
        """Solve the maze using Breadth-First Search algorithm."""
        queue = deque([(maze.start, [maze.start])])
        visited = set()
        
        while queue:
            current_pos, path = queue.popleft()
            
            if current_pos == maze.end:
                return path
            
            if current_pos in visited:
                continue
                
            visited.add(current_pos)
            
            for neighbor in maze.get_neighbors(current_pos):
                if neighbor not in visited:
                    new_path = path + [neighbor]
                    queue.append((neighbor, new_path))
        
        return []  # No path found

class AStarMazeSolver(MazeSolver):
    def solve(self, maze: Maze):
        """Solve the maze using A* algorithm with Manhattan distance heuristic."""
        def manhattan_distance(pos1, pos2):
            """Calculate Manhattan distance between two positions."""
            return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])
        
        def heuristic(pos):
            """Calculate heuristic value for A* (distance to goal)."""
            return manhattan_distance(pos, maze.end)
        
        # Priority queue: (f_score, current_pos, path)
        open_set = [(0, maze.start, [maze.start])]
        visited = set()
        
        while open_set:
            f_score, current_pos, path = heapq.heappop(open_set)
            
            if current_pos == maze.end:
                return path
            
            if current_pos in visited:
                continue
                
            visited.add(current_pos)
            
            for neighbor in maze.get_neighbors(current_pos):
                if neighbor not in visited:
                    new_path = path + [neighbor]
                    g_score = len(new_path) - 1  # Cost from start to neighbor
                    h_score = heuristic(neighbor)  # Estimated cost from neighbor to goal
                    f_score = g_score + h_score
                    
                    heapq.heappush(open_set, (f_score, neighbor, new_path))
        
        return []  # No path found

class DijkstraMazeSolver(MazeSolver):
    def solve(self, maze: Maze):
        """Solve the maze using Dijkstra's algorithm."""
        distances = {maze.start: 0}
        previous = {}
        unvisited = set()
        
        # Initialize all positions as unvisited
        for y in range(len(maze.grid)):
            for x in range(len(maze.grid[0])):
                pos = (x, y)
                if not maze.is_wall(pos):
                    unvisited.add(pos)
                    if pos != maze.start:
                        distances[pos] = float('inf')
        
        while unvisited:
            # Find unvisited node with minimum distance
            current = min(unvisited, key=lambda pos: distances[pos])
            
            if current == maze.end:
                break
                
            unvisited.remove(current)
            
            for neighbor in maze.get_neighbors(current):
                if neighbor in unvisited:
                    distance = distances[current] + 1
                    if distance < distances[neighbor]:
                        distances[neighbor] = distance
                        previous[neighbor] = current
        
        # Reconstruct path
        if maze.end not in previous and maze.end != maze.start:
            return []
            
        path = []
        current = maze.end
        while current is not None:
            path.append(current)
            current = previous.get(current)
        
        return path[::-1]  # Reverse to get start to end order 