from PyQt5 import QtGui, QtWidgets
import sys
#from gui_loader import UiView
#import ini
from project.presenter.mp3mdpresenter import Presenter

def main():
    app = QtWidgets.QApplication(sys.argv)
    presenter = Presenter(app)
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()