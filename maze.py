class Maze:
    def __init__(self, grid):
        self.grid = grid
        self.start = None
        self.end = None
        self.find_special_cells()

    def find_special_cells(self):
        """Find and set the start ('S') and end ('E') positions in the maze."""
        for y, row in enumerate(self.grid):
            for x, cell in enumerate(row):
                if cell == 'S':
                    self.start = (x, y)
                elif cell == 'E':
                    self.end = (x, y)
        
        if self.start is None:
            raise ValueError("No start position ('S') found in maze")
        if self.end is None:
            raise ValueError("No end position ('E') found in maze")

    def is_wall(self, position):
        """Return True if the position is a wall (1) or out of bounds."""
        x, y = position
        
        # Check if position is out of bounds
        if y < 0 or y >= len(self.grid) or x < 0 or x >= len(self.grid[0]):
            return True
        
        # Check if the cell is a wall (1) or start/end positions
        cell = self.grid[y][x]
        return cell == 1

    def is_valid_position(self, position):
        """Check if a position is within the maze bounds."""
        x, y = position
        return 0 <= y < len(self.grid) and 0 <= x < len(self.grid[0])

    def get_neighbors(self, position):
        """Get valid neighboring positions (up, down, left, right)."""
        x, y = position
        neighbors = []
        
        # Check all four directions
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]  # up, down, left, right
        
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            new_pos = (new_x, new_y)
            
            if self.is_valid_position(new_pos) and not self.is_wall(new_pos):
                neighbors.append(new_pos)
        
        return neighbors

    def get_maze_stats(self):
        """Get statistics about the maze."""
        total_cells = len(self.grid) * len(self.grid[0])
        wall_cells = sum(row.count(1) for row in self.grid)
        path_cells = total_cells - wall_cells - 2  # Subtract start and end
        
        return {
            'width': len(self.grid[0]),
            'height': len(self.grid),
            'total_cells': total_cells,
            'wall_cells': wall_cells,
            'path_cells': path_cells,
            'wall_percentage': (wall_cells / total_cells) * 100,
            'start': self.start,
            'end': self.end
        }

    def validate_path(self, path):
        """
        Validate if a path is valid (connects start to end without walls).
        
        Args:
            path (list): List of positions representing the path
            
        Returns:
            dict: Validation result with details
        """
        if not path:
            return {'valid': False, 'error': 'Empty path'}
        
        if path[0] != self.start:
            return {'valid': False, 'error': 'Path does not start at start position'}
        
        if path[-1] != self.end:
            return {'valid': False, 'error': 'Path does not end at end position'}
        
        # Check if each step in the path is valid
        for i in range(len(path) - 1):
            current = path[i]
            next_pos = path[i + 1]
            
            # Check if positions are adjacent
            dx = abs(current[0] - next_pos[0])
            dy = abs(current[1] - next_pos[1])
            
            if not ((dx == 1 and dy == 0) or (dx == 0 and dy == 1)):
                return {'valid': False, 'error': f'Non-adjacent positions at step {i}'}
            
            # Check if next position is not a wall
            if self.is_wall(next_pos):
                return {'valid': False, 'error': f'Path goes through wall at {next_pos}'}
        
        return {'valid': True, 'length': len(path)}

    def get_shortest_path_length(self):
        """Calculate the Manhattan distance between start and end (minimum possible path length)."""
        return abs(self.start[0] - self.end[0]) + abs(self.start[1] - self.end[1])

    def display(self, player_pos=None, path=None):
        """Display the maze with optional player position and solution path."""
        print("\n" + "=" * (len(self.grid[0]) * 2 + 1))
        
        for y, row in enumerate(self.grid):
            print("|", end="")
            for x, cell in enumerate(row):
                current_pos = (x, y)
                
                if player_pos == current_pos:
                    print("P", end="")  # Player
                elif path and current_pos in path:
                    if current_pos == path[0]:
                        print("S", end="")  # Start of path
                    elif current_pos == path[-1]:
                        print("E", end="")  # End of path
                    else:
                        print("·", end="")  # Path marker
                elif cell == 'S':
                    print("S", end="")  # Start
                elif cell == 'E':
                    print("E", end="")  # End
                elif cell == 1:
                    print("█", end="")  # Wall
                else:
                    print(" ", end="")  # Empty space
                print("|", end="")
            print()
        
        print("=" * (len(self.grid[0]) * 2 + 1))
        print("Legend: P=Player, S=Start, E=End, ·=Path, █=Wall")
        print()

    def display_with_stats(self, player_pos=None, path=None):
        """Display the maze with statistics."""
        self.display(player_pos, path)
        
        # Display maze statistics
        stats = self.get_maze_stats()
        print(f"Maze Size: {stats['width']}x{stats['height']}")
        print(f"Wall Coverage: {stats['wall_percentage']:.1f}%")
        print(f"Path Cells: {stats['path_cells']}")
        
        if path:
            path_validation = self.validate_path(path)
            if path_validation['valid']:
                shortest_possible = self.get_shortest_path_length()
                efficiency = (shortest_possible / len(path)) * 100
                print(f"Path Length: {len(path)}")
                print(f"Shortest Possible: {shortest_possible}")
                print(f"Path Efficiency: {efficiency:.1f}%")
            else:
                print(f"Path Error: {path_validation['error']}")
        
        print() 