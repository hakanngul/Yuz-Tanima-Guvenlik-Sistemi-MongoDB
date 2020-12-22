from PyQt5.QtWidgets import QApplication, QMainWindow
from ui_pages.ui_vardiyasorumlusu import Ui_VardiyaSorumlusuMainWindow
from Controllers.SuperVisor import SuperVisor


class SuperVisorWindow(QMainWindow):
    def __init__(self, Person: SuperVisor):
        super().__init__()
        self.ui = Ui_VardiyaSorumlusuMainWindow()
        self.ui.setupUi(self)
        self.person = Person
        self.ui_settings()
        self.show()

    def ui_settings(self):
        self.ui.text_AdSoyad.setEnabled(False)
        self.ui.text_AdSoyad.setText(self.person.full_name)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    app.setStyle("fusion")
    vsorumlu = SuperVisorWindow()
    vsorumlu.show()
    sys.exit(app.exec_())
