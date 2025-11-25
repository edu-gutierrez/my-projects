import random
from PyQt5.QtWidgets import QWidget, QLabel, QComboBox, QSpinBox, QPushButton, QVBoxLayout, QHBoxLayout
from sorting_manager import get_algorithm, ALGORITHMS_QT
from sorting_visualizer import SortingVisualizer

class Sorting_Selector(QWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color:#FCFAF9;")
        self.setWindowTitle("Visualizador de Sorting")
        self.setFixedSize(350, 150)

        layout = QVBoxLayout()

        algorithm_layout = QHBoxLayout()
        algorithm_label = QLabel("Algoritmo:")
        algorithm_label.setStyleSheet("color: #000000; font-weight: bold;")
        self.algorithm_combo = QComboBox()
        self.algorithms = ALGORITHMS_QT
        self.algorithm_combo.addItems(self.algorithms.keys())
        self.algorithm_combo.setStyleSheet( """
                                            QComboBox {
                                                background-color: #00ff00;
                                                color: #000000;  
                                                border: 2px solid #000000;
                                                border-radius: 5px;
                                                padding: 5px;
                                                padding-left: 10px;
                                                padding-right: 30px; 
                                            }

                                            QComboBox QAbstractItemView {
                                                background-color: #00bf00;
                                                color: #000000;
                                                border: 1px solid #000000;
                                                selection-background-color: #008000;
                                                selection-color: #000000;
                                                outline: none;
                                            }
                                            """)
        
        algorithm_layout.addWidget(algorithm_label)
        algorithm_layout.addWidget(self.algorithm_combo)
        layout.addLayout(algorithm_layout)

        n_layout = QHBoxLayout()
        n_label = QLabel("Tamaño N:")
        n_label.setStyleSheet("color: #000000; font-weight: bold;")
        self.n_spin = QSpinBox()
        self.n_spin.setRange(1, 1000)
        self.n_spin.setValue(100)
        self.n_spin.setStyleSheet(  """
                                    QSpinBox {
                                        background-color: #00ff00;
                                        color: #000000;
                                        border: 2px solid #000000;
                                        border-radius: 5px;
                                        padding: 5px; 
                                        padding-left: 10px;
                                        padding-right: 30px; 
                                    }
                                    QSpinBox::selection {
                                        background-color: #00bf00;
                                        color: #000000;
                                    }
                                    QSpinBox::up-button:hover, QSpinBox::down-button:hover {
                                        background-color: #00bf00;
                                    }
                                    """)
        n_layout.addWidget(n_label)
        n_layout.addWidget(self.n_spin)
        layout.addLayout(n_layout)

        self.start_button = QPushButton("Iniciar")
        self.start_button.setStyleSheet("""
                                        QPushButton {
                                            background-color: #00ff00;
                                            color: #000000;
                                            border-radius: 5px;
                                            font-size: 14px;
                                            font-weight: bold;
                                            padding: 10px;
                                        }
                                        QPushButton:hover {
                                            background-color: #00bf00;
                                        }
                                        QPushButton:pressed {
                                            background-color: #008000;
                                            color: #000000;
                                        }
                                        """)
        self.start_button.clicked.connect(self.start)
        layout.addWidget(self.start_button)

        self.setLayout(layout)

    def start(self):
        algorithm_text = self.algorithm_combo.currentText()
        algorithm_key = self.algorithms[algorithm_text]
        n = self.n_spin.value()

        name, alg = get_algorithm(algorithm_key)

        if name == "Bucket Sort":
            arr = list(random.random() for _ in range(n))
        elif name == "Counting Sort":
            arr = list(random.randint(1, n // 10) for _ in range(n))
        else:
            arr = list(range(1, n + 1))
        random.shuffle(arr)

        generator = alg(arr)
        print("Ejecutando "f"{name}...")
        self.visualizer = SortingVisualizer(arr, name, generator)
        self.visualizer.start()