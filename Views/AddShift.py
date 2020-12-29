from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox, QErrorMessage
from ui_pages.ui_vardiya_ekle import Ui_vardiyekle
from Controllers.SuperVisor import SuperVisor


class AddShiftWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_vardiyekle()
        self.ui.setupUi(self)
        self.supervisor = SuperVisor()
        self.initUiSettings()
        self.initSlot()
        self.show()

    def initSlot(self):
        self.ui.btn_vardiyaEkle.setEnabled(False)
        self.ui.btn_vardiyaEkle.clicked.connect(self.vardiya_degis)
        self.ui.cmb_sorumlu.currentIndexChanged.connect(self.yukle)

    def yukle(self):
        self.ui.btn_vardiyaEkle.setEnabled(True)
        currentIndex = self.ui.cmb_sorumlu.currentIndex() - 1
        self.sorumlu = str(self.getAll[currentIndex]["_id"])
        sorumlu = self.ui.cmb_sorumlu.currentText()
        if sorumlu == "Sorumlu Seçiniz":
            QMessageBox.critical(self, "Hata", "Hata oluştu")
            self.ui.lineEdit.clear()
        else:
            self.ui.lineEdit.setText(str(self.getAll[currentIndex]["vardiya"]))

    def test(self):
        print(self.ui.spin_Kontenjan.text())
        print(type(self.ui.spin_Kontenjan.text()))

    def vardiya_degis(self):
        from Controllers.CommonMethods import CommonMethods
        degisecek_vardiya = self.ui.cmb_vardiya.currentText()
        res = CommonMethods.vardiya_degistir(yeniSorumlu=self.sorumlu, degisecek_vardiya=degisecek_vardiya)
        print(res)
        QMessageBox.information(self, "Durum", "İşlem Başarılı")

    def createShift(self, sorumlu, vardiya):
        pass

    def initUiSettings(self):
        self.setSuperVisorToWindow()
        self.ui.lineEdit.setEnabled(False)

    def setSuperVisorToWindow(self):
        self.getAll = self.supervisor.getAllSuperVisor()
        print(self.getAll[0])
        for i in self.getAll:
            self.ui.cmb_sorumlu.addItem(i['full_name'])


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    app.setStyle("fusion")
    window = AddShiftWindow()
    window.show()
    sys.exit(app.exec_())
