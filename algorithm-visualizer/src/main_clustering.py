import sys
from PyQt5.QtWidgets import QApplication
from clustering_selector import Clustering_Selector

def main():
    app = QApplication([])
    selector = Clustering_Selector()
    selector.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()