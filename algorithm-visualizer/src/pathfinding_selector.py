from PyQt5.QtWidgets import QWidget, QLabel, QComboBox, QSpinBox, QPushButton, QVBoxLayout, QHBoxLayout, QSlider
from PyQt5.QtCore import Qt
from pathfinding_manager import get_algorithm, ALGORITHMS_QT
from pathfinding_visualizer import PathfindingVisualizer
from pathfinding_algorithms import generate_maze

class Pathfinding_Selector(QWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color:#FCFAF9;")
        self.setWindowTitle("Visualizador de Pathfinding")
        self.setFixedSize(350, 200)

        layout = QVBoxLayout()
        
        algorithm_layout = QHBoxLayout()
        algorithm_label = QLabel("Algoritmo:")
        algorithm_label.setStyleSheet("color: #000000; font-weight: bold;")
        self.algorithm_combo = QComboBox()
        self.algorithms = ALGORITHMS_QT
        self.algorithm_combo.addItems(self.algorithms.keys())
        self.algorithm_combo.setStyleSheet( """
                                            QComboBox {
                                                background-color: #ff8000;
                                                color: #000000;  
                                                border: 2px solid #000000;
                                                border-radius: 5px;
                                                padding: 5px;
                                                padding-left: 10px;
                                                padding-right: 30px; 
                                            }

                                            QComboBox QAbstractItemView {
                                                background-color: #bf6000;
                                                color: #000000;
                                                border: 1px solid #000000;
                                                selection-background-color: #804000;
                                                selection-color: #000000;
                                                outline: none;
                                            }
                                            """)
        algorithm_layout.addWidget(algorithm_label)
        algorithm_layout.addWidget(self.algorithm_combo)
        layout.addLayout(algorithm_layout)

        n_layout = QHBoxLayout()
        n_label = QLabel("Filas x Columnas:")
        n_label.setStyleSheet("color: #000000; font-weight: bold;")

        self.f_spin = QSpinBox()
        self.f_spin.setRange(10, 100)
        self.f_spin.setValue(50)
        self.f_spin.setStyleSheet("""
                                    QSpinBox {
                                        background-color: #ff8000;
                                        color: #000000;
                                        border: 2px solid #000000;
                                        border-radius: 5px;
                                        padding: 5px; 
                                        padding-left: 10px;
                                        padding-right: 30px; 
                                    }
                                    QSpinBox::selection {
                                        background-color: #bf6000;
                                        color: #000000;
                                    }
                                    QSpinBox::up-button:hover, QSpinBox::down-button:hover {
                                        background-color: #bf6000;
                                    }
                                    """)

        self.c_spin = QSpinBox()
        self.c_spin.setRange(10, 100)
        self.c_spin.setValue(50)
        self.c_spin.setStyleSheet("""
                                    QSpinBox {
                                        background-color: #ff8000;
                                        color: #000000;
                                        border: 2px solid #000000;
                                        border-radius: 5px;
                                        padding: 5px; 
                                        padding-left: 10px;
                                        padding-right: 30px; 
                                    }
                                    QSpinBox::selection {
                                        background-color: #bf6000;
                                        color: #000000;
                                    }
                                    QSpinBox::up-button:hover, QSpinBox::down-button:hover {
                                        background-color: #bf6000;
                                    }
                                    """)

        n_layout.addWidget(n_label)
        n_layout.addWidget(self.f_spin)
        n_layout.addWidget(self.c_spin)
        layout.addLayout(n_layout)

        p_layout = QHBoxLayout()
        p_label = QLabel("Probabilidad de muro(%):")
        p_label.setStyleSheet("color: #000000; font-weight: bold;")
        self.p_spin = QSpinBox()
        self.p_spin.setRange(1, 100)
        self.p_spin.setValue(30)
        self.p_spin.setStyleSheet("""
                                    QSpinBox {
                                        background-color: #ff8000;
                                        color: #000000;
                                        border: 2px solid #000000;
                                        border-radius: 5px;
                                        padding: 5px; 
                                        padding-left: 10px;
                                        padding-right: 30px; 
                                    }
                                    QSpinBox::selection {
                                        background-color: #bf6000;
                                        color: #000000;
                                    }
                                    QSpinBox::up-button:hover, QSpinBox::down-button:hover {
                                        background-color: #bf6000;
                                    }
                                    """)
        
        p_layout.addWidget(p_label)
        p_layout.addWidget(self.p_spin)
        layout.addLayout(p_layout)

        t_layout = QHBoxLayout()
        t_label = QLabel("Delay:")
        t_label.setStyleSheet("color: #000000; font-weight: bold;")
        self.t_slider = QSlider(Qt.Horizontal)
        self.t_slider.setMinimum(1)
        self.t_slider.setMaximum(50)
        self.t_slider.setValue(10)
        t_layout.addWidget(t_label)
        t_layout.addWidget(self.t_slider)
        layout.addLayout(t_layout)

        self.start_button = QPushButton("Iniciar")
        self.start_button.setStyleSheet("""
                                        QPushButton {
                                            background-color: #ff8000;
                                            color: #000000;
                                            border-radius: 5px;
                                            font-size: 14px;
                                            font-weight: bold;
                                            padding: 10px;
                                        }
                                        QPushButton:hover {
                                            background-color: #bf6000;
                                        }
                                        QPushButton:pressed {
                                            background-color: #804000;
                                            color: #000000;
                                        }
                                        """)
        self.start_button.clicked.connect(self.start)
        layout.addWidget(self.start_button)

        self.setLayout(layout)

        self.visualizer = None
    
    def start(self):
        algorithm_text = self.algorithm_combo.currentText()
        algorithm_key = self.algorithms[algorithm_text]
        rows = self.f_spin.value()
        columns = self.c_spin.value()
        prob = self.p_spin.value() / 100
        t = self.t_slider.value()

        name, alg = get_algorithm(algorithm_key)
        print("Ejecutando "f"{name}...")
        self.visualizer = PathfindingVisualizer(rows, columns, name, t)
        self.visualizer.win.show()
        generate_maze(self.visualizer.grid_data, prob)

        start_node = (0, 0)
        end_node = (rows - 1, columns - 1)

        self.visualizer.grid_data[start_node] = 3
        self.visualizer.grid_data[end_node] = 3

        self.visualizer.img_item.setImage(self.visualizer.grid_data, autoLevels=False)

        generator = alg(self.visualizer.grid_data, start_node, end_node)
        self.visualizer.set_generator(generator)