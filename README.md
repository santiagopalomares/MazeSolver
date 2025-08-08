# Maze Solver

A Python-based maze solver game with multiple pathfinding algorithms and interactive gameplay.

## Features

- **Multiple Solver Algorithms**: DFS (Depth-First Search), BFS (Breadth-First Search), and A* pathfinding
- **Interactive Gameplay**: Navigate through mazes using WASD controls
- **Visual Display**: Clear ASCII representation of the maze with player position and solution path
- **Customizable Mazes**: Easy to create and modify maze layouts
- **Solution Visualization**: See the optimal path from start to end

## Project Structure

```
MazeSolver/
├── main.py          # Main entry point and example maze
├── maze.py          # Maze class with grid management
├── solver.py        # Pathfinding algorithms (DFS, BFS, A*)
├── player.py        # Player movement and position tracking
├── game.py          # Game loop and user interaction
├── requirements.txt # Project dependencies
└── README.md       # This file
```

## Installation

1. Clone or download the project
2. Ensure you have Python 3.6+ installed
3. No external dependencies required - uses only Python standard library

## Usage

### Running the Game

```bash
python main.py
```

### Controls

- **W**: Move up
- **A**: Move left  
- **S**: Move down
- **D**: Move right
- **Q**: Quit game

### Creating Custom Mazes

You can create your own maze by modifying the grid in `main.py`:

```python
grid = [
    ['S', 0, 0, 0, 0, 0, 0, 0, 0, 0],  # S = Start
    [1, 1, 0, 1, 1, 1, 1, 1, 1, 0],    # 1 = Wall
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],    # 0 = Path
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 'E']   # E = End
]
```

## Algorithms

### DFS (Depth-First Search)
- Uses a stack-based approach
- May not find the shortest path
- Good for exploring all possible paths

### BFS (Breadth-First Search)  
- Uses a queue-based approach
- Guarantees the shortest path
- Explores all nodes at current depth before moving deeper

### A* (A* Search)
- Uses heuristic-based approach with Manhattan distance
- Finds optimal path efficiently
- Best for performance-critical applications

## Display Legend

- **P**: Player position
- **S**: Start position
- **E**: End position  
- **·**: Solution path
- **█**: Wall
- **|**: Maze border

## Example Output

```
=====================
|S| | | | | | | | | |
|█|█| |█|█|█|█|█|█| |
| | | | | | | | | | |
| |█|█|█|█|█|█|█|█| |
| | | | | | | | | | |
|█|█|█|█|█|█|█|█|█| |
| | | | | | | | | |E|
=====================
Legend: P=Player, S=Start, E=End, ·=Path, █=Wall
```

## Contributing

Feel free to contribute by:
- Adding new pathfinding algorithms
- Improving the UI/UX
- Adding maze generation algorithms
- Creating more complex maze layouts

## License

This project is open source and available under the MIT License.