class Maze:
    def __init__(self, grid):
        self.grid = grid  # TODO: Store the grid
        self.start = None  # TODO: Find and set start position
        self.end = None    # TODO: Find and set end position
        self.find_special_cells()

    def find_special_cells(self):
        pass  # TODO: Implement logic to find start and end

    def is_wall(self, position):
        pass  # TODO: Return True if position is a wall

    def display(self, player_pos=None, path=None):
        pass  # TODO: Print the maze, optionally showing player and path 