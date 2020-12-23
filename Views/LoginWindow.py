from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox
from ui_pages.ui_login import Ui_LoginForm
from Controllers.CommonMethods import CommonMethods
from Controllers.SuperVisor import SuperVisor
from Controllers.Admin import Admin


class LoginFormWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_LoginForm()
        self.ui.setupUi(self)
        self.ui.text_kullaniciAdi.setText("admin")
        self.ui.text_Sifre.setText("123123")

        self.initSlots()

    def initSlots(self):
        self.ui.btn_kayit.clicked.connect(self.RegisterFormWindow)
        self.ui.btn_login.clicked.connect(self.userControlLogin)

    def userControlLogin(self):
        username = self.ui.text_kullaniciAdi.text()
        password = self.ui.text_Sifre.text()
        userCheck = CommonMethods()
        if self.ui.check_kontrol.isChecked():
            res = userCheck.Login(username, password, True)
            if res:
                QMessageBox.information(self, "State", "Giriş Başarılı")
                self.goToMainPage(userType=True, user=res)
            else:
                QMessageBox.critical(self, "State", "Giriş Başarısız")
        else:
            res = userCheck.Login(username, password, False)
            if res:
                QMessageBox.information(self, "State", "Giriş Başarılı")
                self.goToMainPage(userType=False, user=res)
            else:
                QMessageBox.critical(self, "State", "Giriş Başarısız")

    def goToMainPage(self, userType, user):
        if userType:
            from SuperVisor import SuperVisorWindow
            admin = Admin()
            admin.id = user['_id']
            admin.full_name = user['full_name']
            admin.username = user['username']
            admin.email = user['email']
            admin.phone = user['phone']
            admin.user_role = user['user_role']
            self.newWindow = SuperVisorWindow(Admin=admin)
            self.destroy(destroyWindow=True)
        else:
            from SuperVisor import SuperVisorWindow
            supervisor = SuperVisor()
            supervisor.id = user['_id']
            supervisor.full_name = user['full_name']
            supervisor.username = user['username']
            supervisor.email = user['email']
            supervisor.phone = user['phone']
            supervisor.user_role = user['user_role']
            self.newWindow = SuperVisorWindow(SuperVisor=supervisor)
            self.destroy(destroyWindow=True)

    def RegisterFormWindow(self):
        from Views.Register import RegisterWindow
        print("Log Kayit")
        self.goToRegisterWindow = RegisterWindow()


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    app.setStyle("fusion")
    loginWindow = LoginFormWindow()
    loginWindow.show()
    sys.exit(app.exec_())
