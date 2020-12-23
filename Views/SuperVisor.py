from PyQt5.QtWidgets import QApplication, QMainWindow
from ui_pages.ui_vardiyasorumlusu import Ui_VardiyaSorumlusuMainWindow
from Controllers.SuperVisor import SuperVisor
from Controllers.Admin import Admin
from PyQt5.QtGui import QPixmap, QImage
import os


class SuperVisorWindow(QMainWindow):
    def __init__(self, SuperVisor: SuperVisor = None, Admin: Admin = None):
        super().__init__()
        self.ui = Ui_VardiyaSorumlusuMainWindow()
        self.ui.setupUi(self)
        if SuperVisor:
            self.person = SuperVisor
        else:
            self.person = Admin

        self.ui_settings()
        self.setImage()
        self.show()

    def setImage(self):
        print("test")
        path = os.getcwd().split("\\")[:-1]
        path = "/".join(path)
        imgPath = path + "/ui_pages/icons/user.png"
        print(imgPath)
        self.ui.image_vardiyaSorumlusu.setPixmap(QPixmap(imgPath).scaled(263, 211))
        self.ui.image_vardiyaSorumlusu.setScaledContents(True)

    def ui_settings(self):
        self.ui.text_AdSoyad.setEnabled(False)
        self.ui.text_AdSoyad.setText(self.person.full_name)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    app.setStyle("fusion")
    vsorumlu = SuperVisorWindow()
    vsorumlu.show()
    sys.exit(app.exec_())
