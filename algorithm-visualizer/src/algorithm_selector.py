import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QComboBox, QSpinBox, QPushButton, QVBoxLayout, QHBoxLayout
from algorithm_manager import get_algorithm, ALGORITHMS_QT
from visualizer import SortingVisualizer

class Algorithm_Selector(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Visualizador de Algoritmos")
        self.setFixedSize(350, 150)

        layout = QVBoxLayout()

        algorithm_layout = QHBoxLayout()
        algorithm_label = QLabel("Algoritmo:")
        self.algorithm_combo = QComboBox()
        self.algorithms = ALGORITHMS_QT
        self.algorithm_combo.addItems(self.algorithms.keys())
        algorithm_layout.addWidget(algorithm_label)
        algorithm_layout.addWidget(self.algorithm_combo)
        layout.addLayout(algorithm_layout)

        n_layout = QHBoxLayout()
        n_label = QLabel("Tamaño N:")
        self.n_spin = QSpinBox()
        self.n_spin.setRange(1, 1000)
        self.n_spin.setValue(100)
        n_layout.addWidget(n_label)
        n_layout.addWidget(self.n_spin)
        layout.addLayout(n_layout)

        self.start_button = QPushButton("Iniciar")
        self.start_button.clicked.connect(self.start)
        layout.addWidget(self.start_button)

        self.setLayout(layout)

    def start(self):
        algorithm_text = self.algorithm_combo.currentText()
        algorithm_key = self.algorithms[algorithm_text]
        n = self.n_spin.value()

        name, alg = get_algorithm(algorithm_key)

        arr = list(range(1, n + 1))
        random.shuffle(arr)

        generator = alg(arr)
        self.visualizer = SortingVisualizer(arr, name, generator)
        self.visualizer.start()