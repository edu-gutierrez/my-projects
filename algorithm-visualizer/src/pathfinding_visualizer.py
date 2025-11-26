import pyqtgraph as pg
from PyQt5.QtCore import QTimer
import numpy as np

class PathfindingVisualizer:
    def __init__(self, rows, columns, algorithm_name):
        self.rows = rows
        self.columns = columns
        self.algorithm_name = algorithm_name

        self.win = pg.GraphicsLayoutWidget(show=True, title=f"{algorithm_name}")
        self.plot = self.win.addPlot()
        
        self.plot.setAspectLocked(True) 
        self.plot.hideAxis("left")
        self.plot.hideAxis("bottom")

        self.grid_data = np.zeros((rows, columns), dtype=int)
        self.img_item = pg.ImageItem(self.grid_data)
        self.plot.addItem(self.img_item)

        pos = np.array([0.0, 0.2, 0.4, 0.6, 0.8, 1.0])
        color = np.array([
            [255, 255, 255, 255],
            [0, 0, 0, 255],
            [255, 127, 0, 255],
            [0, 0, 255, 255],
            [0, 200, 200, 255],
            [128, 0, 128, 255]
        ], dtype=np.ubyte)

        map = pg.ColorMap(pos, color)
        lut = map.getLookupTable(0.0, 1.0, 256)
        self.img_item.setLookupTable(lut)
        self.img_item.setLevels([0, 5])

        self.timer = QTimer()
        self.timer.timeout.connect(self.update)
        self.generator = None

    def set_generator(self, gen):
        self.generator = gen
        self.timer.start(5)
    
    def update(self):
        try:
            event, r, c = next(self.generator)
            
            if event == "visit":
                self.grid_data[r, c] = 2 
            elif event == "path":
                self.grid_data[r, c] = 4 
            elif event == "close":
                self.grid_data[r, c] = 5
            
            self.img_item.setImage(self.grid_data, autoLevels=False)
            
        except StopIteration:
            self.timer.stop()