from PyQt5.QtWidgets import QApplication
from Views.LoginWindow import LoginFormWindow

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    app.setStyle("fusion")
    loginWindow = LoginFormWindow()
    loginWindow.show()
    sys.exit(app.exec_())
