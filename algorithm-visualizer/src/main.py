import sys
from PyQt5.QtWidgets import QApplication
from algorithm_selector import Algorithm_Selector

def main():
    app = QApplication([])
    selector = Algorithm_Selector()
    selector.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
