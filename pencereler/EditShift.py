from PyQt5.QtWidgets import QApplication, QWidget
from ui_pages.ui_vardiya_duzenle import Ui_vardiyaduzenFrom


class EditShiftWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_vardiyaduzenFrom()
        self.ui.setupUi(self)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    app.setStyle("fusion")
    vduzenle = EditShiftWindow()
    vduzenle.show()
    sys.exit(app.exec_())
