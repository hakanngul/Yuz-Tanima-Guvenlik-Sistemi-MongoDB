from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget
from ui_pages.ui_isciyi_vardiyaya_ekle import Ui_VardiyaIsciEkleForm
from Controllers.Worker import Worker


class AddWorkerToShiftWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_VardiyaIsciEkleForm()
        self.ui.setupUi(self)
        self.ui.btn_Ekle.setEnabled(False)
        self.ui.txt_Vardiya.setEnabled(False)
        self.ui.txt_KimlikNo.setText("83469768934")
        self.initUiSettings()

    def initUiSettings(self):
        self.ui.btn_ara.clicked.connect(self.isciAra)

    def isciAra(self):
        tck = self.ui.txt_KimlikNo.text()
        self.isci = Worker()
        imagePath = self.isci['imagePath'] + self.isci['TcNo'] + "_0.jpg"
        if self.isci is not None:
            self.ui.txt_Vardiya.setText(self.isci['vardiya'])
            self.ui.txt_AdSoyad.setText(self.isci['full_name'])
            self.ui.label.setPixmap(QPixmap(imagePath).scaled(263, 211))
            self.ui.label.setScaledContents(True)
            self.vardiyaYukle()

    def vardiyaYukle(self):
        vardiyalar = ["Sabah", "Akşam", "Gece"]
        for vardiya in vardiyalar:
            if vardiya in self.isci['vardiya']:
                print("geç burayı gardaş")
            else:
                self.ui.cmb_Vardiyalar.addItem(vardiya)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    app.setStyle("fusion")
    viekle = AddWorkerToShiftWindow()
    viekle.show()
    sys.exit(app.exec_())
