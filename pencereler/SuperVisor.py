from PyQt5.QtWidgets import QApplication, QMainWindow
from ui_pages.ui_vardiyasorumlusu import Ui_VardiyaSorumlusuMainWindow


class SuperVisorWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_VardiyaSorumlusuMainWindow()
        self.ui.setupUi(self)
        self.show()


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    app.setStyle("fusion")
    vsorumlu = SuperVisorWindow()
    vsorumlu.show()
    sys.exit(app.exec_())
