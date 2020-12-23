from PyQt5.QtWidgets import QApplication, QMainWindow
from ui_pages.ui_main import Ui_MainWindow
from Controllers.Admin import Admin
from Controllers.SuperVisor import SuperVisor


class MainWindowForm(QMainWindow):
    def __init__(self, Admin: Admin = None, SuperVisor: SuperVisor = None):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        if Admin:
            self.user = Admin
        else:
            self.user = SuperVisor
        self.setting_Ui()
        self.show()

    def setting_Ui(self):
        self.ui.label_username.setText(self.user.username)
        self.ui.label_name_lastname.setText(self.user.full_name)
        self.ui.label_durum.setText(self.user.user_role)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    app.setStyle("fusion")
    mainWindow = MainWindowForm()
    mainWindow.show()
    sys.exit(app.exec_())
