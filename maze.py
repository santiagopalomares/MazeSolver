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