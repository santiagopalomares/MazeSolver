class Player:
    def __init__(self, start_pos):
        self.position = start_pos
        self.move_history = []
        self.total_moves = 0

    def move(self, direction, maze):
        """
        Move the player in the specified direction.
        
        Args:
            direction (str): Direction to move ('up', 'down', 'left', 'right')
            maze (Maze): The maze object to validate movement against
            
        Returns:
            bool: True if move was successful, False otherwise
        """
        x, y = self.position
        new_x, new_y = x, y
        
        # Calculate new position based on direction
        if direction == 'up':
            new_y -= 1
        elif direction == 'down':
            new_y += 1
        elif direction == 'left':
            new_x -= 1
        elif direction == 'right':
            new_x += 1
        else:
            return False  # Invalid direction
        
        new_pos = (new_x, new_y)
        
        # Validate the move
        if self._is_valid_move(new_pos, maze):
            # Record the move
            self.move_history.append({
                'from': self.position,
                'to': new_pos,
                'direction': direction
            })
            
            # Update position and move count
            self.position = new_pos
            self.total_moves += 1
            return True
        else:
            return False

    def _is_valid_move(self, new_pos, maze):
        """
        Check if a move to the new position is valid.
        
        Args:
            new_pos (tuple): The new position to move to
            maze (Maze): The maze object
            
        Returns:
            bool: True if the move is valid, False otherwise
        """
        x, y = new_pos
        
        # Check if position is within maze bounds
        if not maze.is_valid_position(new_pos):
            return False
        
        # Check if the position is not a wall
        if maze.is_wall(new_pos):
            return False
        
        return True

    def get_move_count(self):
        """Get the total number of moves made."""
        return self.total_moves

    def get_move_history(self):
        """Get the history of all moves made."""
        return self.move_history.copy()

    def reset(self, start_pos):
        """Reset the player to a new start position."""
        self.position = start_pos
        self.move_history = []
        self.total_moves = 0

    def get_distance_to_goal(self, goal_pos):
        """
        Calculate Manhattan distance to the goal.
        
        Args:
            goal_pos (tuple): The goal position
            
        Returns:
            int: Manhattan distance to the goal
        """
        return abs(self.position[0] - goal_pos[0]) + abs(self.position[1] - goal_pos[1])

    def get_last_move(self):
        """Get the last move made by the player."""
        if self.move_history:
            return self.move_history[-1]
        return None

    def undo_last_move(self):
        """
        Undo the last move made by the player.
        
        Returns:
            bool: True if undo was successful, False if no moves to undo
        """
        if self.move_history:
            last_move = self.move_history.pop()
            self.position = last_move['from']
            self.total_moves -= 1
            return True
        return False 