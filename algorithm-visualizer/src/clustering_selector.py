import numpy as np
from PyQt5.QtWidgets import QWidget, QLabel, QComboBox, QSpinBox, QPushButton, QVBoxLayout, QHBoxLayout
from clustering_manager import get_algorithm, ALGORITHMS_QT
from clustering_visualizer import ClusteringVisualizer

class Clustering_Selector(QWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color:#FCFAF9;")
        self.setWindowTitle("Visualizador de Clustering")
        self.setFixedSize(350, 250)

        layout = QVBoxLayout()
        
        algorithm_layout = QHBoxLayout()
        algorithm_label = QLabel("Algoritmo:")
        algorithm_label.setStyleSheet("color: #000000; font-weight: bold;")
        self.algorithm_combo = QComboBox()
        self.algorithms = ALGORITHMS_QT
        self.algorithm_combo.addItems(self.algorithms.keys())
        self.algorithm_combo.setStyleSheet( """
                                            QComboBox {
                                                background-color: #00ffff;
                                                color: #000000;  
                                                border: 2px solid #000000;
                                                border-radius: 5px;
                                                padding: 5px;
                                                padding-left: 10px;
                                                padding-right: 30px; 
                                            }

                                            QComboBox QAbstractItemView {
                                                background-color: #00bfbf;
                                                color: #000000;
                                                border: 1px solid #000000;
                                                selection-background-color: #008080;
                                                selection-color: #000000;
                                                outline: none;
                                            }
                                            """)
        algorithm_layout.addWidget(algorithm_label)
        algorithm_layout.addWidget(self.algorithm_combo)
        layout.addLayout(algorithm_layout)

        n_layout = QHBoxLayout()
        n_label = QLabel("Número de Puntos (N):")
        n_label.setStyleSheet("color: #000000; font-weight: bold;")

        self.n_spin = QSpinBox()
        self.n_spin.setRange(10, 5000)
        self.n_spin.setValue(100)
        self.n_spin.setStyleSheet("""
                                    QSpinBox {
                                        background-color: #00ffff;
                                        color: #000000;
                                        border: 2px solid #000000;
                                        border-radius: 5px;
                                        padding: 5px; 
                                        padding-left: 10px;
                                        padding-right: 30px; 
                                    }
                                    QSpinBox::selection {
                                        background-color: #00bfbf;
                                        color: #000000;
                                    }
                                    QSpinBox::up-button:hover, QSpinBox::down-button:hover {
                                        background-color: #00bfbf;
                                    }
                                    """)

        n_layout.addWidget(n_label)
        n_layout.addWidget(self.n_spin)
        layout.addLayout(n_layout)

        k_layout = QHBoxLayout()

        k_label = QLabel("Número de Clusters (K):")
        k_label.setStyleSheet("color: #000000; font-weight: bold;")

        self.k_spin = QSpinBox()
        self.k_spin.setRange(2, 10)
        self.k_spin.setValue(3)
        self.k_spin.setStyleSheet("""
                                    QSpinBox {
                                        background-color: #00ffff;
                                        color: #000000;
                                        border: 2px solid #000000;
                                        border-radius: 5px;
                                        padding: 5px; 
                                        padding-left: 10px;
                                        padding-right: 30px; 
                                    }
                                    QSpinBox::selection {
                                        background-color: #00bfbf;
                                        color: #000000;
                                    }
                                    QSpinBox::up-button:hover, QSpinBox::down-button:hover {
                                        background-color: #00bfbf;
                                    }
                                    """)

        k_layout.addWidget(k_label)
        k_layout.addWidget(self.k_spin)
        layout.addLayout(k_layout)

        self.start_button = QPushButton("Iniciar")
        self.start_button.setStyleSheet("""
                                        QPushButton {
                                            background-color: #00ffff;
                                            color: #000000;
                                            border-radius: 5px;
                                            font-size: 14px;
                                            font-weight: bold;
                                            padding: 10px;
                                        }
                                        QPushButton:hover {
                                            background-color: #00bfbf;
                                        }
                                        QPushButton:pressed {
                                            background-color: #008080;
                                            color: #000000;
                                        }
                                        """)
        self.start_button.clicked.connect(self.start)
        layout.addWidget(self.start_button)

        self.setLayout(layout)

        self.visualizer = None

    def start(self):
        alg_text = self.algorithm_combo.currentText()
        alg_key = ALGORITHMS_QT[alg_text]
        n_points = self.n_spin.value()
        k_clusters = self.k_spin.value()

        name, alg = get_algorithm(alg_key)
        print("Ejecutando "f"{name}...")

        data = []
        for _ in range(k_clusters): # Generamos puntos que esten cerca de 2 centros random para que la visualización sea divertida
            center = np.random.rand(2) * 100 
            points = center + np.random.randn(n_points // k_clusters, 2) * 10
            data.append(points)
        
        data = np.vstack(data)
        np.random.shuffle(data)

        self.visualizer = ClusteringVisualizer(data, k_clusters, name)
        self.visualizer.win.show()
        
        generator = alg(data, k_clusters)
        self.visualizer.set_generator(generator)