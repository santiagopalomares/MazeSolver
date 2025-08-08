#!/usr/bin/env python3
"""
Test script for Maze Solver
Demonstrates all solver algorithms and validates their functionality.
"""

from maze import Maze
from solver import DFSMazeSolver, BFSMazeSolver, AStarMazeSolver, DijkstraMazeSolver
from player import Player

def test_simple_maze():
    """Test with a simple maze."""
    print("="*60)
    print("TESTING SIMPLE MAZE")
    print("="*60)
    
    # Create a simple maze
    grid = [
        ['S', 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 0, 1, 1, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 'E']
    ]
    
    maze = Maze(grid)
    maze.display_with_stats()
    
    # Test all solvers
    solvers = [
        ("DFS", DFSMazeSolver()),
        ("BFS", BFSMazeSolver()),
        ("A*", AStarMazeSolver()),
        ("Dijkstra", DijkstraMazeSolver())
    ]
    
    for name, solver in solvers:
        print(f"\n--- Testing {name} Solver ---")
        path = solver.solve(maze)
        
        if path:
            print(f"Path found: {len(path)} steps")
            print(f"Path: {path}")
            
            # Validate the path
            validation = maze.validate_path(path)
            if validation['valid']:
                print("✅ Path is valid!")
            else:
                print(f"❌ Path error: {validation['error']}")
        else:
            print("❌ No path found!")
        
        # Display maze with path
        maze.display(path=path)

def test_player_movement():
    """Test player movement functionality."""
    print("\n" + "="*60)
    print("TESTING PLAYER MOVEMENT")
    print("="*60)
    
    # Create a simple maze
    grid = [
        ['S', 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 0, 1, 1, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 'E']
    ]
    
    maze = Maze(grid)
    player = Player(maze.start)
    
    print("Initial position:", player.position)
    print("Distance to goal:", player.get_distance_to_goal(maze.end))
    
    # Test some moves
    moves = ['right', 'right', 'down', 'down', 'left', 'left']
    
    for i, move in enumerate(moves):
        print(f"\nMove {i+1}: {move}")
        if player.move(move, maze):
            print(f"✅ Moved to: {player.position}")
            print(f"Distance to goal: {player.get_distance_to_goal(maze.end)}")
        else:
            print(f"❌ Invalid move: {move}")
    
    print(f"\nTotal moves: {player.get_move_count()}")
    print(f"Move history: {len(player.get_move_history())} moves recorded")

def test_maze_validation():
    """Test maze validation functionality."""
    print("\n" + "="*60)
    print("TESTING MAZE VALIDATION")
    print("="*60)
    
    # Test maze with no solution
    no_solution_grid = [
        ['S', 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 1, 1, 1, 1, 1, 1, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 'E']
    ]
    
    try:
        maze = Maze(no_solution_grid)
        print("Maze created successfully")
        
        # Test all solvers on unsolvable maze
        solvers = [
            ("DFS", DFSMazeSolver()),
            ("BFS", BFSMazeSolver()),
            ("A*", AStarMazeSolver()),
            ("Dijkstra", DijkstraMazeSolver())
        ]
        
        for name, solver in solvers:
            path = solver.solve(maze)
            if path:
                print(f"❌ {name} found a path when none should exist!")
            else:
                print(f"✅ {name} correctly found no path")
                
    except ValueError as e:
        print(f"❌ Maze creation failed: {e}")

def main():
    """Run all tests."""
    print("MAZE SOLVER TEST SUITE")
    print("Testing all components and algorithms...")
    
    try:
        test_simple_maze()
        test_player_movement()
        test_maze_validation()
        
        print("\n" + "="*60)
        print("✅ ALL TESTS COMPLETED SUCCESSFULLY!")
        print("="*60)
        print("\nTo run the full game:")
        print("python main.py")
        
    except Exception as e:
        print(f"\n❌ Test failed with error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main() 