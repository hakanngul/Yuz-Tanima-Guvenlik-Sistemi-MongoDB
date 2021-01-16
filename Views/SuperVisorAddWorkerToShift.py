from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox
from ui_pages.ui_isciyi_vardiyaya_ekle import Ui_VardiyaIsciEkleForm
from Controllers.Worker import Worker


class AddWorkerToShiftWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_VardiyaIsciEkleForm()
        self.ui.setupUi(self)
        self.ui.btn_Ekle.setEnabled(False)
        self.ui.txt_Vardiya.setEnabled(False)
        self.ui.txt_KimlikNo.setText("12312312312")
        self.initUiSettings()
        self.show()

    def initUiSettings(self):
        self.ui.btn_ara.clicked.connect(self.isciAra)
        self.ui.btn_Ekle.clicked.connect(self.vardiyaDegis)

    def isciAra(self):
        tck = self.ui.txt_KimlikNo.text()
        self.isci = Worker(tcNo=tck)
        imagePath = self.isci.imagePath + self.isci.tcNo + "_0.jpg"
        print("***")
        print(self.isci)
        print(self.isci.id)
        print(type(self.isci.id))
        if self.isci is not None:
            self.ui.txt_Vardiya.setText(self.isci.vardiya)
            self.ui.txt_AdSoyad.setText(self.isci.full_name)
            self.ui.label.setPixmap(QPixmap(imagePath).scaled(263, 211))
            self.ui.label.setScaledContents(True)
            self.vardiyaYukle()

    def vardiyaDegis(self):
        print(self.isci.vardiya)
        print(self.ui.cmb_Vardiyalar.currentText())
        res = self.isci.addShift(self.isci.vardiya, self.ui.cmb_Vardiyalar.currentText())
        if res:
            QMessageBox.information(self, "Bilgi", "Güncelleme Gerçekleşti")
            self.destroy(destroyWindow=True)

    def vardiyaYukle(self):
        vardiyalar = ["Sabah", "Akşam", "Gece"]
        for vardiya in vardiyalar:
            if vardiya in self.isci.vardiya:
                continue
            else:
                self.ui.cmb_Vardiyalar.addItem(vardiya)
        self.ui.btn_Ekle.setEnabled(True)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    app.setStyle("fusion")
    viekle = AddWorkerToShiftWindow()
    viekle.show()
    sys.exit(app.exec_())
