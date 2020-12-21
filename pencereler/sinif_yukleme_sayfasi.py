from PyQt5.QtWidgets import QApplication, QWidget
from ui_pages.sinif_yukleme_sayfasi import Ui_SinifYukleForm


class sinif_yukleme_sayfasi(QWidget):
    def __init__(self):
        super().__init__()
        self.ui=  Ui_SinifYukleForm()
        self.ui.setupUi(self)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    app.setStyle("fusion")
    sinifyuklemeS = sinif_yukleme_sayfasi()
    sinifyuklemeS.show()
    sys.exit(app.exec_())
