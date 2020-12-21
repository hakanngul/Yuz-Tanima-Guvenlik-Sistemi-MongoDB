from PyQt5.QtWidgets import QApplication , QDialog
from ui_pages.ui_resimGoster import Ui_Dialog


class resimGoster(QDialog):
    def __init__(self):
        super().__init__()
        self.ui=  Ui_Dialog()
        self.ui.setupUi(self)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    app.setStyle("fusion")
    resim = resimGoster()
    resim.show()
    sys.exit(app.exec_())
