from PyQt5.QtWidgets import QApplication , QWidget
from ui_pages.isci_duzenle import Ui_IsciDuzenleForm


class EditWorkerWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui=  Ui_IsciDuzenleForm()
        self.ui.setupUi(self)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    app.setStyle("fusion")
    isciduzen = EditWorkerWindow()
    isciduzen.show()
    sys.exit(app.exec_())
