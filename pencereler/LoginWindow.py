from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox
from ui_pages.ui_login import Ui_LoginForm
from Operations.CommonMethods import CommonMethods


class LoginFormWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_LoginForm()
        self.ui.setupUi(self)
        self.ui.text_kullaniciAdi.setText("test")
        self.ui.text_Sifre.setText("123456")

        self.initSlots()



    def initSlots(self):
        self.ui.btn_kayit.clicked.connect(self.RegisterFormWindow)
        self.ui.btn_login.clicked.connect(self.userControlLogin)

    def userControlLogin(self):
        username = self.ui.text_kullaniciAdi.text()
        password = self.ui.text_Sifre.text()
        userCheck = CommonMethods()
        userCheck = userCheck.login(username, password)
        if userCheck:
            if userCheck[-1] == "admin":
                QMessageBox.information(self, "State", "Giriş Başarılı")
                self.goToMainPage(userCheck[-1])
            elif userCheck[-1] == "vardiyasorumlusu":
                QMessageBox.information(self, "State", "Giriş Başarılı")
                self.goToMainPage(userCheck[-1])
        else:
            QMessageBox.critical(self, "Hata", "Böyle bir kullanıcı bulunamadı")

    def goToMainPage(self, userType):
        if userType == "admin":
            from MainWindow import MainWindowForm
            self.newWindow = MainWindowForm()
            self.destroy(destroyWindow=True)
        else:
            from SuperVisor import SuperVisorWindow
            self.newWindow = SuperVisorWindow()
            self.destroy(destroyWindow=True)

    def RegisterFormWindow(self):
        from pencereler.Register import RegisterWindow
        print("Log Kayit")
        self.goToRegisterWindow = RegisterWindow()


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    app.setStyle("fusion")
    loginWindow = LoginFormWindow()
    loginWindow.show()
    sys.exit(app.exec_())
