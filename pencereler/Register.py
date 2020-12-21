from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox
from ui_pages.ui_kayit import Ui_VardiyaSorumluKayit


class RegisterWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.ui = Ui_VardiyaSorumluKayit()
        self.ui.setupUi(self)
        self.ui_setting()
        self.initSlots()
        self.show()

    def ui_setting(self):
        self.ui.txt_kullaniciAdi.setText("deneme1")
        self.ui.txt_sifre.setText("123123")
        self.ui.txt_sifreTekrar.setText("123123")
        self.ui.txt_adi.setText("deneme ad")
        self.ui.txt_soyadi.setText("deneme soyad")
        self.ui.txt_mail.setText("deneme@gmail.com")

    def initSlots(self):
        self.ui.btn_signup.clicked.connect(self.getDataFromApp)

    def getDataFromApp(self):
        name = self.ui.txt_adi.text()
        lastname = self.ui.txt_soyadi.text()
        full_name = name + " " + lastname
        userType = self.ui.cmb_vardiya.currentIndex()
        username = self.ui.txt_kullaniciAdi.text()
        password = self.ui.txt_sifre.text()
        checkPassword = self.ui.txt_sifreTekrar.text()
        phone = "5317328099"
        email = self.ui.txt_mail.text()
        data = (full_name, userType, username, password, phone, email)
        print(userType)
        if userType == 1:
            try:
                self.registerAdminFromOperations(data)
            except ValueError as err:
                print(f'Hata Oluştu {err}')
        elif userType == 2:
            try:
                self.registerSuperVisorFromOperation(data)
            except ValueError as err:
                print(f'Hata Oluştu {err}')
        else:
            QMessageBox.warning(self, "Hata", "Lütfen Kullanıcı Türünü Seçiniz")

    def registerAdminFromOperations(self, data):
        from Operations.Admin import Admin
        newAdmin = Admin()
        newAdmin.full_name = data[0]
        newAdmin.user_role = "admin"
        newAdmin.username = data[2]
        newAdmin.password = data[3]
        newAdmin.phone = data[4]
        newAdmin.email = data[5]
        result = newAdmin.register()
        if result:
            QMessageBox.information(self, "Kayıt Durumu", "Kayıt Başarlı Oldu!")
            self.ui.txt_sifre.clear()
            self.ui.txt_sifreTekrar.clear()
        else:
            QMessageBox.critical(self, "Kayıt Durumu", "Kayıt Başarısız Oldu!")

    def registerSuperVisorFromOperation(self, data):
        from Operations.SuperVisor import SuperVisor
        newSuperVisor = SuperVisor()
        newSuperVisor.full_name = data[0]
        newSuperVisor.user_role = "supervisor"
        newSuperVisor.username = data[2]
        newSuperVisor.password = data[3]
        newSuperVisor.phone = data[4]
        newSuperVisor.email = data[5]
        newSuperVisor.register()


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    app.setStyle("fusion")
    VardiyaKayitWindow = RegisterWindow()
    VardiyaKayitWindow.show()
    sys.exit(app.exec_())
