import os
import time
from pathlib import Path

from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QImage, QPixmap
import cv2
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QMessageBox
from tqdm import tqdm

from model.basemodels import VGGFace, Facenet
from model.commons import functions
from model.extendedmodels import Emotion, Age, Gender
from ui_pages.ui_main import Ui_MainWindow
from Controllers.Admin import Admin
from Controllers.CommonMethods import CommonMethods, CreateConnection
from Controllers.SuperVisor import SuperVisor
from bson.objectid import ObjectId
from datetime import date
import pandas as pd


class MainWindowForm(QMainWindow):
    def __init__(self, Admin: Admin = None, SuperVisor: SuperVisor = None):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.liste = []
        if Admin:
            self.user = Admin
        else:
            self.user = SuperVisor
            print("*************")
            print(self.user)
            self.collection = CreateConnection()["isciler"]
            self.setting_Ui()
        self.initSlots()
        self.model_name = "VGG-Face"
        self.distance_metric = "cosine"
        self.show()

    def initSlots(self):
        self.Table()
        self.functionsSettings()
        self.ui.actionStartCam.triggered.connect(self.startCam)
        self.ui.actionStopCam.triggered.connect(self.stopCam)
        self.ui.action.triggered.connect(self.loadModel)

    def setting_Ui(self):
        self.ui.label_username.setText(self.user.username)
        self.ui.label_name_lastname.setText(self.user.full_name)
        self.ui.label_durum.setText(self.user.user_role)
        print(self.user.vardiya)
        result = CommonMethods.getInformationShift(vardiya_adi=self.user.vardiya)
        print(result)
        if result:
            self.loadWorkers(result['vardiya_iscileri'])
            self.ui.label_vardiyaAdi.setText(result['vardiya_adi'])
            self.ui.label_vardiyaKodu.setText(str(result['_id']))
            self.ui.label_vardiyaMevcudu.setText("60")

    def startCam(self):
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
        self.ui.kamera_ekrani.setPixmap(QPixmap.fromImage(self.outImage))
        self.ui.kamera_ekrani.setScaledContents(True)

    def stopCam(self):
        self.capture.release()
        self.timer.stop()
        self.ui.kamera_ekrani.setPixmap(QPixmap.fromImage(self.clear_cam()))
        self.ui.kamera_ekrani.setScaledContents(True)

    def clear_cam(self):
        qFormat = QImage.Format_Indexed8
        resim = cv2.imread("images/clear_cam2.png")
        resim = QImage(resim, resim.shape[1], resim.shape[0], resim.strides[0], qFormat)
        return resim

    def functionsSettings(self):
        self.timer = QTimer()
        self.FaceAnalysisSettings()
        self.camControl = False
        self.capture = None
        self.Kontrol = False

    def loadWorkers(self, workers):
        print("self.isciListesi")
        self.isciListesi = workers
        print(self.isciListesi)
        print(type(self.isciListesi))
        print("***")

    def yazdir(self):
        print("Df :", self.df)
        print("Model : ", self.model)
        print("Threshold : ", self.threshold)
        print("Input : ", self.input_shape)
        print("Age Model: ", self.age_model)
        print("Gender Model: ", self.gender_model)

    def loadModelandEmbedding(self, db_path):
        global input_shape
        model_name = self.model_name
        distance_metric = self.distance_metric
        employees = []
        # liste = list(db.getDersBilgileri(self.dersGenelKod))[0].split(",")
        liste = self.liste
        print(liste)
        print(len(liste))
        if len(liste) > 0:
            if os.path.isdir(db_path):
                for r, d, f in os.walk(db_path):  # r=root, d=directories, f = files
                    for file in f:
                        if file.split("_")[0] in liste:
                            if '.jpg' in file:
                                exact_path = r + "/" + file
                                employees.append(exact_path)
                            if '.png' in file:
                                exact_path = r + "/" + file
                                employees.append(exact_path)
            print("employees:", employees)
            if len(employees) > 0:
                if model_name == 'VGG-Face':
                    print("Using VGG-Face model backend and", distance_metric, "distance.")
                    model = VGGFace.loadModel()
                    input_shape = (224, 224)

                elif model_name == 'Facenet':
                    print("Using Facenet model backend", distance_metric, "distance.")
                    model = Facenet.loadModel()
                    input_shape = (160, 160)
                else:
                    raise ValueError("Invalid model_name passed - ", model_name)
                threshold = functions.findThreshold(model_name, distance_metric)
            tic = time.time()
            pbar = tqdm(range(0, len(employees)), desc='Finding embeddings')
            embeddings = []
            for index in pbar:
                employee = employees[index]
                pbar.set_description("Finding embedding for %s" % (employee.split("/")[-1]))
                embedding = []
                res = functions.detectFace(employee, input_shape)
                print(res)
                if res is not None:
                    img = functions.detectFace(employee, input_shape)
                    img_representation = model.predict(img)[0, :]
                    embedding.append(employee)
                    embedding.append(img_representation)
                    embeddings.append(embedding)
                else:
                    print(f'Resimde Yüz Bulunamadı :{employee}')
                    continue
            df = pd.DataFrame(embeddings, columns=['employee', 'embedding'])
            df['distance_metric'] = distance_metric
            toc = time.time()
            print("Embeddings found for given data set in ", toc - tic, " seconds")
            return df, model, threshold, input_shape
        else:
            QMessageBox.critical(self, "Dikkat", "Sınıf Listesi Yüklenemedi loadModelandEmbedding")

    def loadModel(self):
        from pathlib import Path
        home = str(Path.home())+"/.faceAnalytics/program/worker/"
        if not self.Kontrol:
            QMessageBox.warning(self, "Uyarı !!!", "Model Yükleniyor ...")
            self.ui.actionStartCam.setEnabled(True)

            self.df, self.model, self.threshold, self.input_shape = self.loadModelandEmbedding(home)
            print(self.df)
            self.emotion_model, self.age_model, self.gender_model = self.enable_face_analysis()
            self.yazdir()
            self.Kontrol = True

            QMessageBox.information(self, "Model Yüklemesi", "Tamamlandı")
            QMessageBox.information(self, "Vardiya Yüklemesi", "Tamamlandı")
        else:
            QMessageBox.critical(self, "Hata", "Model Zaten Yüklü")

    def enable_face_analysis(self):
        tic = time.time()
        emotion_model = Emotion.loadModel()
        print("Duygu Modeli Yükleniyor ...")
        age_model = Age.loadModel()
        print("Yaş  Modeli Yükleniyor ...")
        gender_model = Gender.loadModel()
        print("Cinsiyet Modeli Yükleniyor ...")
        toc = time.time()
        print("Yüz analiz modellerin yükleme süresi  ", toc - tic, " saniye sürdü")
        return emotion_model, age_model, gender_model

    def FaceAnalysisSettings(self):
        self.input_shape = (224, 224)
        self.time_threshold = 7
        self.frame_threshold = 5
        self.pivot_img_size = 112
        self.face_detected = False
        self.face_included_frames = 0
        self.freezed_frame = 0
        self.text_color = (67, 67, 67)
        self.freeze = False
        self.tic = time.time()
        face_detector_path = "model/haarcascade_frontalface_default.xml"
        self.face_cascade = cv2.CascadeClassifier(face_detector_path)
        self.text_color = (67, 67, 67)
        self.tic = time.time()
        self.age = None
        self.gender = None
        self.emotion = dict()
        functions.allocateMemory()
        functions.initializeFolder()

    def Table(self):
        today = date.today()
        try:
            result = self.isciListesi
            print("***")
            print(result)
            print("---")
            self.ui.vardiya_listesi.setRowCount(len(result))
            for i in range(len(result)):

                self.ui.vardiya_listesi.setItem(i, 2, QTableWidgetItem("Gelmedi"))
                self.ui.vardiya_listesi.setItem(i, 3, QTableWidgetItem("NULL"))
                self.ui.vardiya_listesi.setItem(i, 4, QTableWidgetItem(today.strftime("%d/%m/%Y")))
                veri = CommonMethods().getWorker(result[i])
                if not veri:
                    print("Sorun oldu")
                self.ui.vardiya_listesi.setItem(i, 0, QTableWidgetItem(veri['TcNo']))
                self.ui.vardiya_listesi.setItem(i, 1, QTableWidgetItem(veri['full_name']))
                self.liste.append(veri['TcNo'])

        except:
            QMessageBox.warning(self, "Uyarı", "Sınıf Listesi Yüklenemedi Table")

    def statusbarChanged(self, msg):
        if msg == "Ready":
            self.ui.statusbar.showMessage(msg)
        self.ui.statusbar.showMessage(msg, 3000)

    def TabloGuncelle(self, TcNo):
        from datetime import datetime
        now = datetime.now()
        rowCount = self.ui.vardiya_listesi.rowCount()
        for row in range(rowCount):
            if TcNo == self.ui.vardiya_listesi.item(row, 0).text():
                if len(self.ui.vardiya_listesi.item(row, 2).text()) < 7:
                    self.ui.vardiya_listesi.setItem(row, 2, QTableWidgetItem(
                        f'{now.hour}:{now.minute} {now.day}/{now.month}/{now.year}'))
                else:
                    QMessageBox.information(self, "Uyarı", f'{TcNo} daha önceden yoklaması alınmış')


if __name__ == '__main__':
    import sys

    newUser = SuperVisor(username="yussuf")
    app = QApplication(sys.argv)
    app.setStyle("fusion")
    mainWindow = MainWindowForm(SuperVisor=newUser)
    mainWindow.show()
    sys.exit(app.exec_())
