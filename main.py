from maze import Maze
from solver import DFSMazeSolver, BFSMazeSolver, AStarMazeSolver, DijkstraMazeSolver
from game import Game

def create_simple_maze():
    """Create a simple maze for beginners."""
    return [
        ['S', 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 0, 1, 1, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 'E']
    ]

def create_medium_maze():
    """Create a medium difficulty maze."""
    return [
        ['S', 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [1, 1, 0, 1, 1, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 'E']
    ]

def create_complex_maze():
    """Create a complex maze with multiple paths."""
    return [
        ['S', 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [1, 1, 0, 1, 1, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 'E']
    ]

def create_spiral_maze():
    """Create a spiral-shaped maze."""
    return [
        ['S', 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 'E']
    ]

def select_maze():
    """Let user select a maze."""
    print("\n" + "="*50)
    print("           MAZE SELECTION")
    print("="*50)
    print("1. Simple Maze (Beginner)")
    print("2. Medium Maze (Intermediate)")
    print("3. Complex Maze (Advanced)")
    print("4. Spiral Maze (Expert)")
    print("-"*50)
    
    while True:
        choice = input("Select maze (1-4): ").strip()
        if choice == '1':
            return create_simple_maze(), "Simple Maze"
        elif choice == '2':
            return create_medium_maze(), "Medium Maze"
        elif choice == '3':
            return create_complex_maze(), "Complex Maze"
        elif choice == '4':
            return create_spiral_maze(), "Spiral Maze"
        else:
            print("Invalid choice. Please select 1-4.")

def select_solver():
    """Let user select a solver algorithm."""
    print("\n" + "="*50)
    print("           SOLVER SELECTION")
    print("="*50)
    print("1. DFS (Depth-First Search)")
    print("2. BFS (Breadth-First Search)")
    print("3. A* (A-Star)")
    print("4. Dijkstra")
    print("-"*50)
    
    while True:
        choice = input("Select solver (1-4): ").strip()
        if choice == '1':
            return DFSMazeSolver(), "DFS"
        elif choice == '2':
            return BFSMazeSolver(), "BFS"
        elif choice == '3':
            return AStarMazeSolver(), "A*"
        elif choice == '4':
            return DijkstraMazeSolver(), "Dijkstra"
        else:
            print("Invalid choice. Please select 1-4.")

def main():
    """Main function to run the maze solver game."""
    print("Welcome to Maze Solver!")
    print("This game demonstrates different pathfinding algorithms.")
    
    # Select maze and solver
    maze_grid, maze_name = select_maze()
    solver, solver_name = select_solver()
    
    print(f"\nStarting {maze_name} with {solver_name} solver...")
    
    # Create and run the game
    maze = Maze(maze_grid)
    game = Game(maze, solver)
    game.run()

if __name__ == "__main__":
    main() 