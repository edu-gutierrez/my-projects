import sys
from PyQt5.QtWidgets import QApplication
from pathfinding_visualizer import PathfindingVisualizer
from pathfinding_algorithms import bfs, generate_maze

if __name__ == "__main__":
    app = QApplication([])

    ROWS, COLUMNS = 50, 50
    vis = PathfindingVisualizer(ROWS, COLUMNS)
    prob = 0.3
    
    generate_maze(vis.grid_data, prob)

    vis.img_item.setImage(vis.grid_data, autoLevels=False)

    start_node = (0, 0)
    end_node = (ROWS - 1, COLUMNS - 1)

    vis.grid_data[start_node] = 3
    vis.grid_data[end_node] = 3

    bfs_generator = bfs(vis.grid_data, start_node, end_node)

    vis.set_generator(bfs_generator)
    
    sys.exit(app.exec())