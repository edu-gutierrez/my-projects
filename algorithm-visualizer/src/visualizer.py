import pyqtgraph as pg
from PyQt5.QtCore import QTimer

class SortingVisualizer:
    def __init__(self, arr, algorithm_name, generator):
        self.arr = list(arr)
        self.algorithm_name = algorithm_name
        self.generator = generator

        self.win = pg.GraphicsLayoutWidget(show=False, title=f"{algorithm_name}")

        self.plot = self.win.addPlot()
       
        self.plot.setYRange(0, max(arr) * 1.2)
        self.plot.setXRange(0, len(arr))

        self.bars = pg.BarGraphItem(x=list(range(len(self.arr))), height = arr, width = 0.8)
        
        self.plot.addItem(self.bars)

        self.brushes = [pg.mkBrush("w")] * len(arr)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update)

    def start(self):
        self.timer.start(20)
        if not self.win.isVisible():
            self.win.show()

    def update(self):
        try:
            frame = next(self.generator)

            if isinstance(frame, list):
                arr = frame
                for k in range(len(arr)):
                    self.brushes[k] = pg.mkBrush("w")

            else:
                arr, i, j = frame

                for k in range(len(arr)):
                    self.brushes[k] = pg.mkBrush("w")

                self.brushes[i] = pg.mkBrush("r")
                self.brushes[j] = pg.mkBrush("r")

            self.bars.setOpts(height=arr, brushes=self.brushes)

        except StopIteration:
            self.timer.stop()
