from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox, QErrorMessage
from ui_pages.ui_vardiya_ekle import Ui_vardiyekle
from Database.DataBaseConnection import CreateConnection
from bson.objectid import ObjectId
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
        self.ui.btn_vardiyaEkle.clicked.connect(self.getShiftInformation)
        self.ui.cmb_sorumlu.currentIndexChanged.connect(self.yukle)

    def yukle(self):
        self.ui.btn_vardiyaEkle.setEnabled(True)

        currentUser = self.ui.cmb_sorumlu.currentIndex() - 1
        self.currentUSer = self.getAll[currentUser]
        getInfo = self.getAll[currentUser]['vardiya']
        self.ui.lineEdit.setText(str(getInfo))

    def test(self):
        print(self.ui.spin_Kontenjan.text())
        print(type(self.ui.spin_Kontenjan.text()))

    def getShiftInformation(self):
        # TODO :eskiSorumlu bulunacak
        # TODO: yeniSorumlu ile yer değiştirecek eski sorumlu null olacak
        degisecekVardiya = self.ui.lineEdit.text()
        eskiSorumlu = None
        for i in self.getAll:
            if self.ui.cmb_vardiya.currentText() == i['vardiya']:
                print("bulundu")
                eskiSorumlu = i['_id']
        print(eskiSorumlu)
        res1 = self.supervisor.editSupervisorShift(eskiSorumlu, degisecekVardiya)
        res2 = self.supervisor.editSupervisorShift(self.currentUSer['_id'], self.ui.cmb_vardiya.currentText())

        if res1 and res2 is not None:
            QMessageBox.information(self, "Bilgi", "Vardiyalar Değiştirildi")
            self.destroy(self, destroyWindow=True)
        else:
            QMessageBox.critical(self, "Bilgi", "Hata Oluştu")
            self.destroy(self, destroyWindow=True)

    def createShift(self, sorumlu, vardiya):
        pass

    def initUiSettings(self):
        self.setSuperVisorToWindow()
        self.ui.lineEdit.setEnabled(False)

    def setSuperVisorToWindow(self):
        self.getAll = self.supervisor.getAllSuperVisor()
        print(len(self.getAll))
        for i in self.getAll:
            print(i)
            self.ui.cmb_sorumlu.addItem(i['full_name'])


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    app.setStyle("fusion")
    window = AddShiftWindow()
    window.show()
    sys.exit(app.exec_())
