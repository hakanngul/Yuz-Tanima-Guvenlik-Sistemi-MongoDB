from PyQt5.QtWidgets import QApplication , QMainWindow
from ui_pages.ui_IsciAra import Ui_isciAraWindow


class FindWorkerWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=  Ui_isciAraWindow()
        self.ui.setupUi(self)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    app.setStyle("fusion")
    isciara = FindWorkerWindow()
    isciara.show()
    sys.exit(app.exec_())
