from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox
from ui_pages.ui_login import Ui_LoginForm
from Controllers.CommonMethods import CommonMethods


class LoginFormWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_LoginForm()
        self.ui.setupUi(self)
        self.ui.text_kullaniciAdi.setText("yusuf")
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
            print("test")
            res = userCheck.adminLogin(username, password)
            if res:
                QMessageBox.information(self, "State", "Giriş Başarılı")
                self.goToMainPage(userType=True)
            else:
                QMessageBox.information(self, "State", "Giriş Başarılı")
                self.goToMainPage(userType=False)
        else:
            userCheck.supervisorLogin(username, password)

    def goToMainPage(self, userType):
        if userType:
            from MainWindow import MainWindowForm
            self.newWindow = MainWindowForm()
            self.destroy(destroyWindow=True)
        else:
            from SuperVisor import SuperVisorWindow
            self.newWindow = SuperVisorWindow()
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
