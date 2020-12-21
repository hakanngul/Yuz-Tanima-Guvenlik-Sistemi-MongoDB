from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox
from PyQt5.QtCore import QCoreApplication
from ui_pages.ui_kayit import Ui_VardiyaSorumluKayit
from Database.DataBaseConnection import CreateConnection


class RegisterWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.ui = Ui_VardiyaSorumluKayit()
        self.ui.setupUi(self)
        self.ui_setting()
        self.initSlots()
        self.checkAdmin()
        self.show()

    def checkAdmin(self):
        cnx, cursor = CreateConnection()
        cursor.execute("Select * from kisi where user_role=%s", ('admin',))
        response = cursor.fetchone()
        if response:
            self.ui.cmb_vardiya.removeItem(2)
            _translate = QCoreApplication.translate
            self.ui.cmb_vardiya.setItemText(0, _translate("VardiyaSorumluKayit", "Rol Seçiniz"))
            self.ui.cmb_vardiya.setItemText(1, _translate("VardiyaSorumluKayit", "SuperVisor"))
        else:
            print(False)

    def testButton(self):
        test = self.ui.cmb_vardiya.currentText()
        print(test)

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
        userType = self.ui.cmb_vardiya.currentText()
        username = self.ui.txt_kullaniciAdi.text()
        password = self.ui.txt_sifre.text()
        checkPassword = self.ui.txt_sifreTekrar.text()
        phone = "5317328099"
        email = self.ui.txt_mail.text()
        data = (full_name, userType, username, password, phone, email)
        if checkPassword == password:
            if userType == "Admin":
                try:
                    self.registerAdminFromOperations(data)
                except ValueError as err:
                    print(f'Hata Oluştu {err}')
            elif userType == "SuperVisor":
                try:
                    self.registerSuperVisorFromOperation(data)
                except ValueError as err:
                    print(f'Hata Oluştu {err}')
            else:
                QMessageBox.warning(self, "Hata", "Lütfen Kullanıcı Türünü Seçiniz")
        else:
            QMessageBox.warning(self, "Şifre", "Şifreler Uyuşmuyor")

    def registerSuperVisorFromOperation(self, data):
        from Operations.SuperVisor import SuperVisor
        from Operations.CommonMethods import CommonMethods
        newSuperVisor = SuperVisor()
        checkParameters = CommonMethods()
        newSuperVisor.full_name = data[0]
        newSuperVisor.user_role = "supervisor"
        newSuperVisor.username = data[2]
        newSuperVisor.password = data[3]
        newSuperVisor.phone = data[4]
        newSuperVisor.email = data[5]
        checkUserName = checkParameters.checkUserName(newSuperVisor.username)
        checkEmail = checkParameters.checkEmail(newSuperVisor.email)
        if checkUserName:
            QMessageBox.warning(self, "Username Kontrol", f'{newSuperVisor.username} kullanılmaktadır.')
        elif checkEmail:
            QMessageBox.warning(self, "Email Kontrol", f'{newSuperVisor.email} kullanılmaktadır.')
        else:
            result = newSuperVisor.register()
            if result:
                QMessageBox.information(self, "Kayıt Durumu", "Kayıt Başarlı Oldu!")
                self.clearForm()
            else:
                QMessageBox.critical(self, "Kayıt Durumu", "Kayıt Başarısız Oldu!")

    def registerAdminFromOperations(self, data):
        from Operations.Admin import Admin
        from Operations.CommonMethods import CommonMethods
        newAdmin = Admin()
        checkParameters = CommonMethods()
        newAdmin.full_name = data[0]
        newAdmin.user_role = "admin"
        newAdmin.username = data[2]
        newAdmin.password = data[3]
        newAdmin.phone = data[4]
        newAdmin.email = data[5]
        checkUserName = checkParameters.checkUserName(newAdmin.username)
        checkEmail = checkParameters.checkEmail(newAdmin.email)

        if checkUserName:
            QMessageBox.warning(self, "Username Kontrol", f'{newAdmin.username} kullanılmaktadır.')
        elif checkEmail:
            QMessageBox.warning(self, "Email Kontrol", f'{newAdmin.email} kullanılmaktadır.')
        else:
            result = newAdmin.register()
            if result:
                QMessageBox.information(self, "Kayıt Durumu", "Kayıt Başarlı Oldu!")
                self.clearForm()
            else:
                QMessageBox.critical(self, "Kayıt Durumu", "Kayıt Başarısız Oldu!")

    def clearForm(self):
        self.ui.txt_sifre.clear()
        self.ui.txt_sifreTekrar.clear()
        self.ui.txt_kullaniciAdi.clear()
        self.ui.txt_mail.clear()
        self.ui.txt_adi.clear()
        self.ui.txt_soyadi.clear()
        self.ui.cmb_vardiya.removeItem(2)
        _translate = QCoreApplication.translate
        self.ui.cmb_vardiya.setItemText(0, _translate("VardiyaSorumluKayit", "Rol Seçiniz"))
        self.ui.cmb_vardiya.setItemText(1, _translate("VardiyaSorumluKayit", "SuperVisor"))


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    app.setStyle("fusion")
    VardiyaKayitWindow = RegisterWindow()
    VardiyaKayitWindow.show()
    sys.exit(app.exec_())
