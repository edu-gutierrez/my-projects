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
        self.plot.setXRange(-1, len(arr))

        self.bars = pg.BarGraphItem(x=list(range(len(self.arr))), height = arr, width = 0.8)
        
        self.plot.addItem(self.bars)

        self.brushes = [pg.mkBrush("w")] * len(arr)

        if algorithm_name == "Bucket Sort" or algorithm_name == "Counting Sort":
            self.win.nextRow()
            self.plot_buckets = self.win.addPlot(row=1, col=0)
            if algorithm_name == "Bucket Sort":
                 self.plot_buckets.setXRange(0, len(arr) // 10 - 1)
            elif algorithm_name == "Counting Sort":
                 self.plot_buckets.setXRange(1, len(arr) // 10)
            self.plot_buckets.setYRange(0, max(len(arr) // 2, 15))
            self.bucket_heights = [0] * len(arr)
            self.bucket_bars = pg.BarGraphItem(
                x=list(range(len(arr))),
                height=self.bucket_heights,
                width=0.8,
                brush='c'
            )
            self.plot_buckets.addItem(self.bucket_bars)
            self.bucket_content = [[] for _ in range(len(arr))]


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

            elif len(frame) == 4:
                event, arr, i, target = frame
                if event == "to_bucket":
                    val = arr[i]
                    self.brushes[i] = pg.mkBrush('y')
                    self.bucket_content[target].append(val)
                    self.bucket_heights[target] += 1
                    self.bucket_bars.setOpts(height=self.bucket_heights)
                elif event == "rebuild":
                    self.val = arr[i]
                    self.brushes[i] = pg.mkBrush('c')
                    self.bars.setOpts(height=arr, brushes=self.brushes)
            else:
                arr, i, j = frame

                for k in range(len(arr)):
                    self.brushes[k] = pg.mkBrush("w")

                self.brushes[i] = pg.mkBrush("r")
                self.brushes[j] = pg.mkBrush("r")

            self.bars.setOpts(height=arr, brushes=self.brushes)

        except StopIteration:
            self.timer.stop()
