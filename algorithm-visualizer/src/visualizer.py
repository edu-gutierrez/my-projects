import pyqtgraph as pg
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QTimer
import sys

class SortingVisualizer:
    
    def __init__(self, arr, algorithm_name, generator):
        self.arr = arr
        self.algorithm_name = algorithm_name
        self.generator = generator

        self.app = QApplication([])
        self.win = pg.GraphicsLayoutWidget(show=True, title=f"{algorithm_name}")

        # Configuramos gráfico
        self.plot = self.win.addPlot()
        self.plot.setYRange(0, max(arr) * 1.2)
        self.plot.setXRange(0, len(arr))

        # Barras iniciales
        self.bars = pg.BarGraphItem(
            x = list(range(len(arr))),
            height = arr,
            width = 0.8
        )
        self.plot.addItem(self.bars)

        # Colores de cada barra
        self.brushes = [pg.mkBrush("w")] * len(arr)

        # Timer que llama a update cada 20 ms
        self.timer = QTimer()
        self.timer.timeout.connect(self.update)
        self.timer.start(20)

    def update(self):
        try:
            arr, i, j = next(self.generator)

            # Restablecemos colores y destacamos barras swapeadas
            for k in range(len(arr)):
                self.brushes[k] = pg.mkBrush("w")
            self.brushes[i] = pg.mkBrush("r")
            self.brushes[j] = pg.mkBrush("r")

            # Actualización de las barras 
            self.bars.setOpts(height=arr, brushes=self.brushes)

        except StopIteration:
            print("Ordenación terminada")
            self.timer.stop()

    def run(self):
        sys.exit(self.app.exec())
