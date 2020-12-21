from PyQt5.QtWidgets import QApplication, QWidget
from ui_pages.ui_vadiyayaişçiEkle import Ui_VardiyaIsciEkleForm


class AddWorkerToShiftWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_VardiyaIsciEkleForm()
        self.ui.setupUi(self)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    app.setStyle("fusion")
    viekle = AddWorkerToShiftWindow()
    viekle.show()
    sys.exit(app.exec_())
