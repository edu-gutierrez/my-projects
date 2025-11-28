import pyqtgraph as pg
from PyQt5.QtCore import QTimer

class ClusteringVisualizer:
    def __init__(self, data, k, algorithm_name):
        self.data = data
        self.k = k
        self.algorithm_name = algorithm_name

        self.win = pg.GraphicsLayoutWidget(show=True, title=f"{algorithm_name} - K={k}")
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
            (255, 0, 0),    # Rojo
            (0, 200, 0),    # Verde
            (0, 0, 255),    # Azul
            (255, 165, 0),  # Naranja
            (255, 0, 255),  # Magenta
            (0, 255, 255),  # Cyan
            (128, 0, 128),  # Morado
            (128, 128, 0),  # Oliva
            (0, 128, 128),  # Teal
            (128, 128, 128) # Gris
        ]
        
        self.brushes = [pg.mkBrush(128, 128, 128) for _ in range(len(data))]
        self.scatter_data.setData(pos=data, brush=self.brushes)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update)
        self.generator = None

    def set_generator(self, gen):
        self.generator = gen
        self.timer.start(500)

    def update(self):
        try:
            event, labels, centroids = next(self.generator)
            
            new_brushes = []
            for label in labels:
                c = self.colors[label]
                new_brushes.append(pg.mkBrush(c))

            self.scatter_data.setBrush(new_brushes)
            self.scatter_centroids.setData(pos=centroids)
            
            if event == "done":
                print("Clustering terminado.")

        except StopIteration:
            self.timer.stop()