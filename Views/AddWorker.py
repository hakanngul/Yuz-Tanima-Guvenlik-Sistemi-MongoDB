from PyQt5.QtWidgets import QApplication, QMainWindow
from ui_pages.İsciEkle import Ui_isciEkleWindow


class AddWorkerWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=  Ui_isciEkleWindow()
        self.ui.setupUi(self)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    app.setStyle("fusion")
    isciekle = AddWorkerWindow()
    isciekle.show()
    sys.exit(app.exec_())
