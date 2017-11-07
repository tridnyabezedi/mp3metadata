from PyQt5 import QtWidgets
import sys
from project.presenter.mp3mdpresenter import Presenter

def main():
    app = QtWidgets.QApplication(sys.argv)
    presenter = Presenter(app)
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()