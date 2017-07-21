from PyQt5 import QtGui, QtWidgets
import sys
from gui_loader import LoadUi


def main():
    app = QtWidgets.QApplication(sys.argv)
    mainwindow = LoadUi(ini.ui_path, uiorpy=False)  # uic.loadUi("pirate.ui")
    # loadicons(mainwin, app)
    mainwindow.setupUi_buttons()
    mainwindow.setupUi_shortcuts()
    mainwindow.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()