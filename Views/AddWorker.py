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
        self.home1 = str(Path.home())
        self.home = self.home1 + "/.faceAnalytics/program/worker/"
        self.UI_Settings()
        self.sayac = 0
        self.show()

    def UI_Settings(self):
        self.ui.actionStart_Camera.setEnabled(False)
        self.ui.actionStop_Camera.setEnabled(False)
        self.ui.btn_resimCek.setEnabled(False)
        self.ui.btn_kayit.clicked.connect(self.isciEkle)
        self.ui.actionStart_Camera.triggered.connect(self.startCam)
        self.ui.actionStop_Camera.triggered.connect(self.stopCam)
        self.ui.btn_resimCek.clicked.connect(self.resimCek)
        # self.ui.btn_resimCek.setEnabled(True)
        # self.ui.btn_resimCek.clicked.connect(self.addWorkerToShift)

    def isciKontrol(self):
        isciler = CreateConnection()["isciler"].find_one({
            'TcNo': {"$eq": self.ui.txt_TcNo.text()}
        })
        if isciler is not None:
            return False
        else:
            tcNo = self.ui.txt_TcNo.text()
            self.imagePath = self.home + tcNo
            print(self.imagePath)
            self.createFolder(self.imagePath)
            return True

    def createFolder(self, imagePath):
        try:
            os.mkdir(imagePath)
            return True
        except FileExistsError as err:
            QMessageBox.warning(self, "Hata", f'{err}')

    def isciEkle(self):
        self.ui.btn_kayit.setEnabled(False)
        if self.isciKontrol():
            yeni_isci = Worker()
            yeni_isci.tcNo = self.ui.txt_TcNo.text()
            yeni_isci.full_name = self.ui.txt_Adi.text() + " " + self.ui.txt_Soyadi.text()
            yeni_isci.imagePath = self.home + yeni_isci.tcNo
            yeni_isci.vardiya = self.ui.cmb_Vardiyas.currentText()
            response = yeni_isci.save()
            QMessageBox.information(self, "Bilgi", "Kayıt Ekleniyor")
            if response:
                self.addWorkerToShift(yeni_isci.tcNo)
                QMessageBox.information(self, "Bilgi", "Kayıt Başarılı Oldu")
                QMessageBox.information(self, "Bilgi", "Menüden Kamerayı Açınız")

                return self.ui.actionStart_Camera.setEnabled(True)
            else:
                QMessageBox.critical(self, "Hata", "Kayıt Başarısız Oldu")

        else:
            QMessageBox.critical(self, "Hata", "Böyle bir kullanıcı var")

    def addWorkerToShift(self, tcNo):
        db = CreateConnection()["vardiya"].find_one({"vardiya_adi": self.ui.cmb_Vardiyas.currentText()})[
            'vardiya_iscileri']
        idx = CreateConnection()['isciler'].find_one({"TcNo": tcNo})["_id"]
        db.append(idx)
        CreateConnection()['vardiya'].update_one({"vardiya_adi": self.ui.cmb_Vardiyas.currentText()}, {
            "$set": {
                "vardiya_iscileri": db
            }
        })

    def startCam(self):
        self.ui.btn_resimCek.setEnabled(True)
        self.ui.actionStop_Camera.setEnabled(True)
        self.capture = cv2.VideoCapture(0)
        self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 300)
        self.capture.set(cv2.CAP_PROP_FRAME_WIDTH, 500)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(1000. / 24.0)

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

    def clear_cam(self):
        qFormat = QImage.Format_Indexed8
        resim = cv2.imread("images/clear_cam2.png")
        resim = QImage(resim, resim.shape[1], resim.shape[0], resim.strides[0], qFormat)
        return resim

    def resimCek(self):
        image = self.image
        imageName = self.imagePath + "/" + self.ui.txt_TcNo.text() + "_" + str(self.sayac) + ".jpg"
        if self.sayac < 3:
            if not os.path.isfile(self.imagePath):
                cv2.imwrite(imageName, image)
                self.sayac += 1
        else:
            QMessageBox.warning(self, "Bilgilendirme", f'{self.sayac} adet resim kayıt edildi.')
            return "test"


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    app.setStyle("fusion")
    isciekle = AddWorkerWindow()
    isciekle.show()
    sys.exit(app.exec_())
