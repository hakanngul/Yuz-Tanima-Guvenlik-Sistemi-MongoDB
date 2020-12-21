from PyQt5.QtWidgets import QApplication, QMainWindow
from ui_pages.ui_main import Ui_MainWindow


class MainWindowForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    app.setStyle("fusion")
    mainWindow = MainWindowForm()
    mainWindow.show()
    sys.exit(app.exec_())
