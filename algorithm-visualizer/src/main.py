import sys
import subprocess
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QSpacerItem, QSizePolicy)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

class Launcher(QWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color:#FCFAF9;")
        self.setWindowTitle("Visualizador de Algoritmos")
        self.setFixedSize(600, 300)
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        layout.setSpacing(20)
        layout.setContentsMargins(40, 40, 40, 40)

        title = QLabel("Visualizador de Algoritmos")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("color: #000000; font-weight: bold;")
        font = QFont("Arial", 18, QFont.Bold)
        title.setFont(font)
        layout.addWidget(title)

        self.btn_sorting = QPushButton("Algoritmos de Sorting")
        self.btn_sorting.setMinimumHeight(50)
        self.btn_sorting.setStyleSheet( """
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
        self.btn_sorting.clicked.connect(self.launch_sorting)
        layout.addWidget(self.btn_sorting)

        self.btn_path = QPushButton("Algoritmos de Pathfinding")
        self.btn_path.setMinimumHeight(50)
        self.btn_path.setStyleSheet("""
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
        self.btn_path.clicked.connect(self.launch_pathfinding)
        layout.addWidget(self.btn_path)

        self.btn_sorting = QPushButton("Algoritmos de Clustering")
        self.btn_sorting.setMinimumHeight(50)
        self.btn_sorting.setStyleSheet( """
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
        self.btn_sorting.clicked.connect(self.launch_clustering)
        layout.addWidget(self.btn_sorting)
        
        self.setLayout(layout)

    def launch_sorting(self):
        print("Lanzando Sorting...")
        subprocess.Popen([sys.executable, "main_sorting.py"])

    def launch_pathfinding(self):
        print("Lanzando Pathfinding...")
        subprocess.Popen([sys.executable, "main_pathfinding.py"])
    
    def launch_clustering(self):
        print("Lanzando Clustering...")
        subprocess.Popen([sys.executable, "main_clustering.py"])

if __name__ == "__main__":
    app = QApplication([])
    launcher = Launcher()
    launcher.show()
    sys.exit(app.exec())