import pyqtgraph as pg
from PyQt5.QtCore import QTimer

class ClusteringVisualizer:
    def __init__(self, data, algorithm_name, t):
        self.data = data
        self.algorithm_name = algorithm_name
        self.time = t

        self.win = pg.GraphicsLayoutWidget(show=True, title=f"{algorithm_name}")
        self.plot = self.win.addPlot()
        self.plot.setAspectLocked(True)

        self.plot.hideAxis('left')
        self.plot.hideAxis('bottom')
        self.win.setBackground('#FFFFFF')

        self.scatter_data = pg.ScatterPlotItem(size=10, pen=pg.mkPen(None))
        self.plot.addItem(self.scatter_data)
        
        self.scatter_centroids = pg.ScatterPlotItem(
            size=20, 
            symbol='x', 
            pen=pg.mkPen('k', width=3),
            brush=pg.mkBrush('k')
        )
        self.plot.addItem(self.scatter_centroids)

        self.colors = [
            (255, 0, 0),
            (0, 255, 0),
            (0, 0, 255),
            (255, 255, 0),
            (255, 0, 255),
            (0, 255, 255),
            (128, 0, 128),
            (128, 128, 0),
            (0, 128, 128),
            (128, 128, 128)
        ]
        
        self.brushes = [pg.mkBrush(128, 128, 128) for _ in range(len(data))]
        self.scatter_data.setData(pos=data, brush=self.brushes)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update)
        self.generator = None

    def set_generator(self, gen):
        self.generator = gen
        self.timer.start(self.time)

    def update(self):
        try:
            event, labels, centroids = next(self.generator)
            
            new_brushes = []
            for label in labels:
                if label == -1:
                    c = (128, 128, 128)
                elif label == -2:
                    c = (0, 0, 0)
                else:
                    c = self.colors[label % len(self.colors)]
                new_brushes.append(pg.mkBrush(c))

            self.scatter_data.setBrush(new_brushes)
            if centroids is not None:
                self.scatter_centroids.setData(pos=centroids)
            else:
                self.scatter_centroids.clear()

            if event == "done":
                print("Clustering terminado.")

        except StopIteration:
            self.timer.stop()