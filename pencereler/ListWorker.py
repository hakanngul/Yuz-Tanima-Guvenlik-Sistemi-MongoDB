from PyQt5.QtWidgets import QApplication, QWidget
from ui_pages.isci_listesi import Ui_isciListesi


class ListWorkerWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_isciListesi()
        self.ui.setupUi(self)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    app.setStyle("fusion")
    isciliste = ListWorkerWindow()
    isciliste.show()
    sys.exit(app.exec_())
