import numpy as np
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QLabel, QComboBox, QSpinBox, QPushButton, QVBoxLayout, QHBoxLayout, QDoubleSpinBox, QSlider
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
        self.algorithm_combo.currentIndexChanged.connect(self.update_ui)
        layout.addLayout(algorithm_layout)

        dataShape_layout = QHBoxLayout()
        dataShape_label = QLabel("Forma de Datos:")
        dataShape_label.setStyleSheet("color: #000000; font-weight: bold;")
        self.dataShape_combo = QComboBox()
        self.dataShape_combo.addItems(["Blobs", "Donut"])
        self.dataShape_combo.setStyleSheet("""
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
        dataShape_layout.addWidget(dataShape_label)
        dataShape_layout.addWidget(self.dataShape_combo)
        layout.addLayout(dataShape_layout)

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

        self.k_label = QLabel("Clusters / Min Sample (K):")
        self.k_label.setStyleSheet("color: #000000; font-weight: bold;")

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

        k_layout.addWidget(self.k_label)
        k_layout.addWidget(self.k_spin)
        layout.addLayout(k_layout)

        e_layout = QHBoxLayout()

        self.e_label = QLabel("Epsilon:")
        self.e_label.setStyleSheet("color: #000000; font-weight: bold;")

        self.e_spin = QDoubleSpinBox()
        self.e_spin.setRange(1.0, 50.0)
        self.e_spin.setValue(5.0)
        self.e_spin.setSingleStep(0.5)
        self.e_spin.setStyleSheet("""
                                    QDoubleSpinBox {
                                        background-color: #00ffff;
                                        color: #000000;
                                        border: 2px solid #000000;
                                        border-radius: 5px;
                                        padding: 5px; 
                                        padding-left: 10px;
                                        padding-right: 30px;
                                    }
                                    QDoubleSpinBox::selection {
                                        background-color: #00bfbf;
                                        color: #000000;
                                    }
                                    QDoubleSpinBox::up-button:hover, QSpinBox::down-button:hover {
                                        background-color: #00bfbf;
                                    }
                                    """)

        e_layout.addWidget(self.e_label)
        e_layout.addWidget(self.e_spin)
        layout.addLayout(e_layout)

        t_layout = QHBoxLayout()
        t_label = QLabel("Delay:")
        t_label.setStyleSheet("color: #000000; font-weight: bold;")
        self.t_slider = QSlider(Qt.Horizontal)
        self.t_slider.setMinimum(1)
        self.t_slider.setMaximum(500)
        self.t_slider.setValue(250)
        t_layout.addWidget(t_label)
        t_layout.addWidget(self.t_slider)
        layout.addLayout(t_layout)

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
        self.update_ui()

    def update_ui(self):
        alg_text = self.algorithm_combo.currentText()
        
        if alg_text == "DBSCAN":
            self.k_label.setText("Min Sample:")
            self.k_spin.setRange(2, 50)
            self.k_spin.setValue(4)
            self.e_label.setText("Epsilon:")
            self.e_label.show()
            self.e_spin.show()
            self.k_label.show()
            self.k_spin.show()
        elif alg_text == "Mean Shift":
            self.e_label.setText("Radio:")
            self.e_label.show()
            self.e_spin.show()
            self.e_spin.setRange(2, 50)
            self.e_spin.setValue(20)
            self.k_label.hide()
            self.k_spin.hide()

        else:
            self.k_label.setText("Número de Clusters (K):")
            self.k_label.show()
            self.k_spin.show()
            self.k_spin.setRange(2, 10)
            self.k_spin.setValue(3)
            
            self.e_label.hide()
            self.e_spin.hide()

    def start(self):
        alg_text = self.algorithm_combo.currentText()
        alg_key = ALGORITHMS_QT[alg_text]
        n_points = self.n_spin.value()
        k_clusters = self.k_spin.value()
        shape = self.dataShape_combo.currentText()
        t = self.t_slider.value()

        name, alg = get_algorithm(alg_key)
        print("Ejecutando "f"{name}...")

        data = []
        if shape == "Blobs":
            if name == "KMeans" or name == "Hierarchical":
                for _ in range(k_clusters):
                    center = np.random.rand(2) * 100
                    points = center + np.random.randn(n_points // k_clusters, 2) * 10
                    data.append(points)
            else:
                for _ in range(4):
                    center = np.random.rand(2) * 100
                    points = center + np.random.randn(n_points // k_clusters, 2) * 10
                    data.append(points)
            data = np.vstack(data)

        elif shape == "Donut":
            n_inner = n_points // 3
            n_outer = n_points - n_inner
            
            # Circulo interior
            angles_inner = np.random.rand(n_inner) * 2 * np.pi
            radi_inner = 15 + np.random.randn(n_inner) * 3
            
            x_inner = 50 + radi_inner * np.cos(angles_inner)
            y_inner = 50 + radi_inner * np.sin(angles_inner)
            inner_points = np.column_stack((x_inner, y_inner))
            
            # Circulo exterior
            angles_outer = np.random.rand(n_outer) * 2 * np.pi
            radi_outer = 40 + np.random.randn(n_outer) * 4
            
            x_outer = 50 + radi_outer * np.cos(angles_outer)
            y_outer = 50 + radi_outer * np.sin(angles_outer)
            outer_points = np.column_stack((x_outer, y_outer))
            
            data = np.vstack((inner_points, outer_points))
        
        np.random.shuffle(data)

        if alg_key == "1" or alg_key == "3": # KMeans or Hierarchical
            generator = alg(data, k_clusters)
            self.visualizer = ClusteringVisualizer(data, name, t)
        
        elif alg_key == "2": # DBSCAN
            epsilon = self.e_spin.value()
            generator = alg(data, epsilon, k_clusters)
            self.visualizer = ClusteringVisualizer(data, name, t)
        elif alg_key == "4": # Mean Shift
            radio = self.e_spin.value()
            generator = alg(data, radio)
            self.visualizer = ClusteringVisualizer(data, name, t)

        self.visualizer.win.show()
        self.visualizer.set_generator(generator)