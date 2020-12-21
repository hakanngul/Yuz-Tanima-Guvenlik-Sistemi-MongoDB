from PyQt5.QtWidgets import QApplication , QDialog
from ui_pages.ui_vardiya_ekle import Ui_Dialog


class AddShiftWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui=  Ui_Dialog()
        self.ui.setupUi(self)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    app.setStyle("fusion")
    resim = AddShiftWindow()
    resim.show()
    sys.exit(app.exec_())
