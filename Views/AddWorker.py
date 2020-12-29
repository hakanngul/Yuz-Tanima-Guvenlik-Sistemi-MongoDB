from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui_pages.ui_isci_ekle import Ui_Isci_ekleWindow
from PyQt5.QtGui import QDoubleValidator, QImage, QPixmap
from Controllers.Worker import Worker
import os
from pathlib import Path
from Database.DataBaseConnection import CreateConnection
import cv2


class AddWorkerWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Isci_ekleWindow()
        self.ui.setupUi(self)
        self.ui.txt_TcNo.setValidator(QDoubleValidator())
        self.ui.btn_kayit.clicked.connect(self.isciEkle)
        self.home = str(Path.home())
        self.home = self.home + "/.faceAnalytics/program/worker/"
        self.UI_Settings()

    def UI_Settings(self):
        # self.ui.actionStart_Camera.setEnabled(False)
        self.ui.actionStop_Camera.setEnabled(False)
        self.ui.btn_resimCek.setEnabled(False)
        self.ui.btn_kayit.clicked.connect(self.isciEkle)
        self.ui.actionStart_Camera.triggered.connect(self.startCam)

    def isciKontrol(self):
        isciler = CreateConnection()["isciler"].find_one({
            'TcNo': {"$eq": self.ui.txt_TcNo.text()}
        })
        if isciler is not None:
            return False
        else:
            tcNo = self.ui.txt_TcNo.text()
            self.imagePath = self.home + tcNo
            self.createFolder(self.imagePath)
            return True

    def createFolder(self, imagePath):
        try:
            os.mkdir(imagePath)
            return True
        except FileExistsError as err:
            QMessageBox.warning(self, "Hata", f'{err}')

    def isciEkle(self):
        if self.isciKontrol():
            yeni_isci = Worker()
            yeni_isci.tcNo = self.ui.txt_TcNo.text()
            yeni_isci.full_name = self.ui.txt_Adi.text() + " " + self.ui.txt_Soyadi.text()
            yeni_isci.imagePath = self.home + yeni_isci.tcNo
            yeni_isci.vardiya = self.ui.cmb_Vardiyas.currentText()
            print("asdasdas")
            response = yeni_isci.save()
            print("***xx")

            if response:
                QMessageBox.information(self, "Bilgi", "Kayıt Başarılı Oldu")
                QMessageBox.information(self, "Bilgi", "Menüden Kamerayı Açınız")
                self.ui.actionStart_Camera.setEnabled(True)
            else:
                QMessageBox.critical(self, "Hata", "Kayıt Başarısız Oldu")

        else:
            QMessageBox.critical(self, "Hata", "Böyle bir kullanıcı var")

    def startCam(self):
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
        # BGR to RGB
        self.outImage = outImage.rgbSwapped()
        self.ui.label.setPixmap(QPixmap.fromImage(self.outImage))
        self.ui.label.setScaledContents(True)

    def stopCam(self):
        self.capture.release()
        resim = self.clear_cam()
        self.ui.label.setPixmap(QPixmap.fromImage(resim))
        self.ui.label.setScaledContents(True)
        self.timer.stop()
        self.ui.actionStart_Camera.setEnabled(True)
        self.ui.btn_resimCek.setEnabled(False)

    def clear_cam(self):
        qFormat = QImage.Format_Indexed8
        resim = cv2.imread("images/clear_cam2.png")
        resim = QImage(resim, resim.shape[1], resim.shape[0], resim.strides[0], qFormat)
        return resim


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    app.setStyle("fusion")
    isciekle = AddWorkerWindow()
    isciekle.show()
    sys.exit(app.exec_())
