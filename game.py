from maze import Maze
from solver import MazeSolver, DFSMazeSolver, BFSMazeSolver, AStarMazeSolver, DijkstraMazeSolver
from player import Player
import os

class Game:
    def __init__(self, maze: Maze, solver: MazeSolver = None):
        self.maze = maze
        self.solver = solver or DFSMazeSolver()
        self.player = Player(maze.start)
        self.path = self.solver.solve(maze)
        self.moves = 0
        self.show_path = True
        self.available_solvers = {
            '1': DFSMazeSolver(),
            '2': BFSMazeSolver(),
            '3': AStarMazeSolver(),
            '4': DijkstraMazeSolver()
        }

    def clear_screen(self):
        """Clear the console screen."""
        os.system('cls' if os.name == 'nt' else 'clear')

    def show_menu(self):
        """Display the main menu."""
        print("\n" + "="*50)
        print("           MAZE SOLVER GAME")
        print("="*50)
        print(f"Moves: {self.moves}")
        print(f"Current Solver: {self.solver.__class__.__name__}")
        print(f"Path Length: {len(self.path) if self.path else 'No path found'}")
        print("-"*50)

    def show_controls(self):
        """Display the controls help."""
        print("\nControls:")
        print("  W/A/S/D - Move (Up/Left/Down/Right)")
        print("  H - Toggle path hint")
        print("  S - Switch solver algorithm")
        print("  R - Reset to start position")
        print("  Q - Quit game")
        print("-"*50)

    def switch_solver(self):
        """Allow user to switch between different solver algorithms."""
        print("\nAvailable Solvers:")
        print("1. DFS (Depth-First Search)")
        print("2. BFS (Breadth-First Search)")
        print("3. A* (A-Star)")
        print("4. Dijkstra")
        
        choice = input("Select solver (1-4): ").strip()
        if choice in self.available_solvers:
            self.solver = self.available_solvers[choice]
            self.path = self.solver.solve(self.maze)
            print(f"Switched to {self.solver.__class__.__name__}")
        else:
            print("Invalid choice. Keeping current solver.")

    def reset_game(self):
        """Reset the player to the start position."""
        self.player.position = self.maze.start
        self.moves = 0
        print("Game reset to start position.")

    def run(self):
        """Main game loop."""
        print("Welcome to Maze Solver!")
        print("Navigate from S (Start) to E (End)")
        
        while True:
            self.clear_screen()
            self.show_menu()
            self.show_controls()
            
            # Display the maze
            self.maze.display(self.player.position, self.path if self.show_path else None)
            
            # Check win condition
            if self.player.position == self.maze.end:
                print(f"\n🎉 Congratulations! You've reached the end in {self.moves} moves!")
                if self.path:
                    optimal_moves = len(self.path) - 1
                    if self.moves == optimal_moves:
                        print("🏆 Perfect! You found the optimal path!")
                    elif self.moves <= optimal_moves * 1.5:
                        print("👍 Great job! You found a good path!")
                    else:
                        print(f"💡 Hint: The optimal path requires {optimal_moves} moves.")
                
                play_again = input("\nPlay again? (y/n): ").lower().strip()
                if play_again == 'y':
                    self.reset_game()
                    continue
                else:
                    print("Thanks for playing!")
                    break
            
            # Get user input
            move = input("\nEnter move: ").lower().strip()
            
            if move == 'q':
                print("Game ended. Thanks for playing!")
                break
            elif move == 'h':
                self.show_path = not self.show_path
                print(f"Path hint {'enabled' if self.show_path else 'disabled'}")
            elif move == 's':
                self.switch_solver()
            elif move == 'r':
                self.reset_game()
            elif move in ['w', 'a', 's', 'd']:
                direction_map = {
                    'w': 'up',
                    'a': 'left', 
                    's': 'down',
                    'd': 'right'
                }
                
                if self.player.move(direction_map[move], self.maze):
                    self.moves += 1
                else:
                    print("Invalid move! You can't move through walls.")
            else:
                print("Invalid input! Use W/A/S/D to move, H for hint, S for solver, R to reset, or Q to quit.") 