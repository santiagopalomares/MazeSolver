class Player:
    def __init__(self, start_pos):
        self.position = start_pos

    def move(self, direction, maze):
        x, y = self.position
        new_x, new_y = x, y
        
        if direction == 'up':
            new_y -= 1
        elif direction == 'down':
            new_y += 1
        elif direction == 'left':
            new_x -= 1
        elif direction == 'right':
            new_x += 1
        
        new_pos = (new_x, new_y)
        
        if (0 <= new_x < len(maze.grid[0]) and 
            0 <= new_y < len(maze.grid) and 
            not maze.is_wall(new_pos)):
            self.position = new_pos
            return True
        return False 