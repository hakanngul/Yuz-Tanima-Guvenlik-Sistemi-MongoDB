from PyQt5.QtWidgets import QApplication, QWidget
from ui_pages.ui_vardiyaekle import Ui_vardiyekle


class AddShiftWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui=  Ui_vardiyekle()
        self.ui.setupUi(self)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    app.setStyle("fusion")
    vardiya = AddShiftWindow()
    vardiya.show()
    sys.exit(app.exec_())
