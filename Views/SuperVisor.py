from PyQt5.QtWidgets import QApplication, QMainWindow
from ui_pages.ui_vardiyasorumlusu import Ui_VardiyaSorumlusuMainWindow
from Controllers.SuperVisor import SuperVisor
from Controllers.Admin import Admin
from PyQt5.QtGui import QPixmap
import os


class SuperVisorWindow(QMainWindow):
    def __init__(self, SuperVisor: SuperVisor):
        super().__init__()
        self.ui = Ui_VardiyaSorumlusuMainWindow()
        self.ui.setupUi(self)
        self.person = SuperVisor
        self.ui_settings()
        self.setImage()
        self.initSlots()
        self.show()

    def initSlots(self):
        self.ui.action_VardiyaEkle.triggered.connect(self.getVardiyaEkleWindow)

    def setImage(self):
        print("test")
        path = os.getcwd().split("\\")[:-1]
        path = "/".join(path)
        imgPath = path + "/ui_pages/icons/user.png"
        print(imgPath)
        self.ui.image_vardiyaSorumlusu.setPixmap(QPixmap(imgPath).scaled(263, 211))
        self.ui.image_vardiyaSorumlusu.setScaledContents(True)

    def getVardiyaEkleWindow(self):
        from AddShift import AddShiftWindow
        self.vardiyaEkle = AddShiftWindow()

    def ui_settings(self):
        self.ui.text_AdSoyad.setEnabled(False)
        self.ui.text_AdSoyad.setText(self.person.full_name)
        self.ui.text_Vardiyasi.setText(self.person.vardiya)
        self.ui.cmb_Model.setEnabled(False)
        self.ui.cmb_Metrik.setEnabled(False)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    app.setStyle("fusion")
    # newUser = SuperVisor("test", "123123").getSupervisor()
    newUser = SuperVisor(username="test")
    newAdmin = Admin()
    newAdmin.username = "admin"
    newAdmin.password = "123123"
    vsorumlu = SuperVisorWindow(SuperVisor=newUser)
    vsorumlu.show()
    sys.exit(app.exec_())
