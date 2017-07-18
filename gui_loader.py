from PyQt5 import QtCore, QtGui, QtWidgets, uic
import sys
import ini
import os
from getfiles import getfileslist
from mp3idmaker import SongList


class loadui(QtWidgets.QMainWindow):
    def __init__(self, ui_path, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        Form, Base = uic.loadUiType(ui_path)
        self.ui = Form()
        self.ui.setupUi(self)
        self.resize(1200, 600)
        self.ui.TableView.setColumnWidth(0, 150)
        self.ui.TableView.setColumnWidth(1, 120)
        self.ui.TableView.setColumnWidth(2, 120)
        self.ui.TableView.setColumnWidth(3, 50)
        self.ui.TableView.setColumnWidth(4, 90)
        self.ui.TableView.setColumnWidth(5, 70)
        self.ui.TableView.setColumnWidth(6, 200)
        self.workdir = os.getcwd()
        self.showpath(self.workdir)
        self.showdir(self.workdir)

    def setupUi_buttons(self):
        self.ui.PBchoosedirectory.clicked.connect(self.selectFile)
        self.ui.TableView.clicked.connect(self.displaytags)
        self.ui.PBapply.clicked.connect(self.apply_)
        self.ui.PBapplytoall.clicked.connect(self.applytoall_)

    def setupUi_shortcuts(self):
        self.shortcuts = []
        self.__setshortcut("Ctrl+O", self.selectFile)
        self.__setshortcut("Q", self.selectFile)
        self.__setshortcut("F1", self.__testjoke)

    def __setshortcut(self, shortcut_, fuction):
        self.shortcuts.append(QtWidgets.QShortcut(QtGui.QKeySequence(shortcut_), self))
        self.shortcuts[-1].activated.connect(fuction)

    def showpath(self, workdir_):
        self.ui.Edit_path.setText(str(workdir_).replace(r'/', '\\'))

    def showdir(self, workdir_):
        dirmodel = self.getdirmodel(workdir_)
        self.ui.TableView.setModel(dirmodel)

    def getdirmodel(self, workdir_):
        fileslist = getfileslist(os.path.normcase(workdir_))
        self.songlist = SongList(fileslist)
        dirmodel = QtGui.QStandardItemModel()
        dirlist = self.songlist.createtable()
        dirlist = [[QtGui.QStandardItem(x) for x in list_] for list_ in dirlist]
        for list_ in dirlist:
            dirmodel.appendRow(list_)
        dirmodel.setHorizontalHeaderLabels(['Filename'] + list(self.songlist.tablegraphs))
        return dirmodel

    def selectFile(self):
        self.filedialog = QtWidgets.QFileDialog()
        self.filedialog.setFileMode(2)
        self.filedialog.setLabelText(3,'Выбор рабочего каталога')
        self.filedialog.exec()
        dir_value = self.filedialog.selectedFiles()
        if dir_value[0] != self.workdir:
            self.workdir = dir_value[0]
            self.showpath(self.workdir)
            self.showdir(self.workdir)
        self.activateWindow()

    def __getrow(self):
        return self.ui.TableView.selectedIndexes()[0].row()

    def displaytags(self):
        row_ = self.__getrow()
        self.ui.Edit_track.setText(self.songlist.gettag(row_, 'tracknum'))
        self.ui.Edit_artist.setText(self.songlist.gettag(row_, 'artist'))
        self.ui.Edit_title.setText(self.songlist.gettag(row_, 'title'))
        self.ui.Edit_album.setText(self.songlist.gettag(row_, 'album'))
        self.ui.Edit_author.setText(self.songlist.gettag(row_, 'author'))
        self.ui.Edit_year.setText(self.songlist.gettag(row_, 'year'))
        self.ui.Edit_genre.setText(self.songlist.gettag(row_, 'genre'))
        self.ui.TextEdit_comment.setPlainText(self.songlist.gettag(row_, 'comment'))

    def __readvalues(self):
        #row_ = self.__getrow()
        dict_ = {}
        dict_['tracknum'] = self.ui.Edit_track.text()
        dict_['artist'] = self.ui.Edit_artist.text()
        dict_['title'] = self.ui.Edit_title.text()
        dict_['album'] = self.ui.Edit_album.text()
        dict_['author'] = self.ui.Edit_author.text()
        dict_['year'] = self.ui.Edit_year.text()
        dict_['genre'] = self.ui.Edit_genre.text()
        dict_['comment'] = self.ui.TextEdit_comment.toPlainText()
        for word_ in dict_:
            if dict_[word_].startswith(r"/re/:"):
                dict_[word_] = (dict_[word_][5:], True)
            else:
                dict_[word_] = (dict_[word_], False)
        return dict_

    def apply_(self):
        try:
            dict_ = self.__readvalues()
            row_ = self.__getrow()
            print(dict_)
            print(row_)
            self.songlist.changetags(row_, dict_)
            self.songlist.save(row_)
            self.showdir(self.workdir)
            self.ui.TableView.selectRow(row_)
        except:
            pass

    def applytoall_(self):
        try:
            dict_ = self.__readvalues()
            print(dict_)
            self.songlist.changetagsforall(dict_)
            self.songlist.saveall()
            self.showdir(self.workdir)
        except:
            pass

    def __testjoke(self):
        self.ui.Edit_path.setText("НЕ ЖМИ ЭТОТ КНОПКА!")

    def __testtest(self, str_='!!'):
        self.ui.Edit_path.setText("It's working!" + str_)


def loadicons(window, application):
    ico = QtGui.QIcon(ini.icon_path_main)
    ico_folder = QtGui.QIcon(ini.icon_path_folder)
    window.setWindowIcon(ico)
    application.setWindowIcon(ico)
    window.ui.PBchoosedirectory.setIcon(ico_folder)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mainwin = loadui(ini.ui_path) #uic.loadUi("pirate.ui")
    loadicons(mainwin, app)
    mainwin.setupUi_buttons()
    mainwin.setupUi_shortcuts()
    mainwin.show()
    sys.exit(app.exec_())