import os
from pathlib import Path
import cv2
from PyQt5.QtCore import QTimer, pyqtSlot
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from ui_pages.ui_add_supervisor import Ui_add_SuperVisorWindow


class AddSuperVisorWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_add_SuperVisorWindow()
        self.ui.setupUi(self)
        self.home = str(Path.home())
        self.home = self.home + "/.faceAnalytics/program/supervisor/"
        print(self.home)
        self.sayac = 0
        self.initSlots()
        self.imagePath = ""

    def initSlots(self):
        self.ui.btn_resimCek.setEnabled(False)
        self.ui.actionStart_Camera.setEnabled(False)
        self.ui.actionStop_Camera.setEnabled(False)
        self.ui.btn_kayit.clicked.connect(self.addSuperVisor)
        self.ui.actionStart_Camera.triggered.connect(self.startCam)
        self.ui.actionStop_Camera.triggered.connect(self.stopCam)
        self.ui.btn_resimCek.clicked.connect(self.resimCek)

    def addSuperVisor(self):
        from Controllers.SuperVisor import SuperVisor
        superVisor = SuperVisor()
        superVisor.username = self.ui.txt_Username.text()
        superVisor.full_name = self.ui.txt_AdiSoyadi.text()
        superVisor.email = self.ui.txt_Email.text()
        superVisor.password = self.ui.txt_Password.text()
        superVisor.imagePath = self.home + self.ui.txt_Username.text()
        self.imagePath = superVisor.imagePath
        res1 = superVisor.checkUsername()
        res2 = superVisor.checkEmail()
        if res1:
            QMessageBox.warning(self, "Uyarı", "Kullanıcı Adı Kullanılmaktadır.")
            return ""
        if res2:
            QMessageBox.warning(self, "Uyarı", "Email Kullanılmaktadır.")
            return ""
        if not (res1 and res2):

            res = self.createFolder(superVisor.imagePath)
            if res:
                superVisor.save()
                QMessageBox.information(self, "Bilgi", "Kayıt Başarılı Oldu")
                self.ui.actionStart_Camera.setEnabled(True)
            else:
                QMessageBox.warning(self, "Uyarı", "Bir Sorun Oluştu!")

    def createFolder(self, imagePath):
        try:
            os.mkdir(imagePath)
            return True
        except FileExistsError as err:
            QMessageBox.warning(self, "Hata", f'{err}')

    def startCam(self):
        self.ui.btn_resimCek.setEnabled(True)
        self.ui.actionStop_Camera.setEnabled(True)
        self.capture = cv2.VideoCapture(0)
        self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 300)
        self.capture.set(cv2.CAP_PROP_FRAME_WIDTH, 500)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(1000. / 24)

    def update_frame(self):
        ret, self.image = self.capture.read()
        self.displayImage(self.image)

    def displayImage(self, img):
        qFormat = QImage.Format_Indexed8
        if len(img.shape) == 3:
            if img.shape[2] == 4:
                qFormat = QImage.Format_RGBA8888
            else:
                qFormat = QImage.Format_RGB888
        outImage = QImage(img, img.shape[1], img.shape[0], img.strides[0], qFormat)
        self.outImage = outImage.rgbSwapped()
        self.ui.label.setPixmap(QPixmap.fromImage(self.outImage))
        self.ui.label.setScaledContents(True)

    def stopCam(self):
        self.capture.release()
        self.timer.stop()
        self.ui.label.setPixmap(QPixmap.fromImage(self.clear_cam()))
        self.ui.label.setScaledContents(True)
        self.ui.actionStart_Camera.setEnabled(True)
        self.ui.btn_resimCek.setEnabled(False)

    @staticmethod
    def clearCam():
        qFormat = QImage.Format_Indexed8
        resim = cv2.imread("images/clear_cam2.png")
        resim = QImage(resim, resim.shape[1], resim.shape[0], resim.strides[0], qFormat)
        return resim

    def resimCek(self):
        image = self.image
        imageName = self.imagePath + "/" + self.ui.txt_Username.text() + "_" + str(self.sayac) + ".jpg"
        if self.sayac < 3:
            if not os.path.isfile(self.imagePath):
                cv2.imwrite(imageName, image)
                self.sayac += 1
        else:
            QMessageBox.warning(self, "Bilgilendirme", f'{self.sayac} adet resim kayıt edildi.')
            return "test"


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    app.setStyle("fusion")
    sorumluEkle = AddSuperVisorWindow()
    sorumluEkle.show()
    sys.exit(app.exec_())
