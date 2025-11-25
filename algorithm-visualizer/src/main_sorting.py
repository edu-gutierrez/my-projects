import sys
from PyQt5.QtWidgets import QApplication
from sorting_selector import Sorting_Selector

def main():
    app = QApplication([])
    selector = Sorting_Selector()
    selector.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
