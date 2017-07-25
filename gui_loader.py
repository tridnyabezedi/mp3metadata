from PyQt5 import QtCore, QtGui, QtWidgets, uic
import sys
import ini
import os
from getfiles import getfileslist
from mp3idmaker import SongList
from ui.mp3ui.mainwindow import Ui_MainWindow


class UiView(QtWidgets.QMainWindow):
    signal_select_dir = QtCore.pyqtSignal('QString')
    signal_apply_to_one = QtCore.pyqtSignal()
    signal_apply_to_all = QtCore.pyqtSignal()
    signal_choose_song = QtCore.pyqtSignal(int)

    def __init__(self, application, parent=None):
        QtWidgets.QMainWindow.__init__(self)
        if ini.uiorpy:
            self.__load_from_ui(ini.ui_path_ui)
        else:
            self.__load_from_py(ini.ui_path_py)
        self.__load_icons(application)
        self.setupUi_buttons()
        self.setupUi_shortcuts(application)
        self.__setup_filedialog()
        self.__set_table_props()
        self.resize(1200, 600)

    def __setup_filedialog(self):
        self.filedialog = QtWidgets.QFileDialog()
        self.filedialog.setFileMode(2)
        self.filedialog.setLabelText(3, 'Выбор рабочего каталога')

    def __set_table_props(self):
        self.ui.TableView.setColumnWidth(0, 150)
        self.ui.TableView.setColumnWidth(1, 120)
        self.ui.TableView.setColumnWidth(2, 120)
        self.ui.TableView.setColumnWidth(3, 50)
        self.ui.TableView.setColumnWidth(4, 90)
        self.ui.TableView.setColumnWidth(5, 70)
        self.ui.TableView.setColumnWidth(6, 200)

    def __load_icons(self, application):
        ico = QtGui.QIcon(ini.icon_path_main)
        ico_folder = QtGui.QIcon(ini.icon_path_folder)
        self.setWindowIcon(ico)
        application.setWindowIcon(ico)
        self.ui.PBchoosedirectory.setIcon(ico_folder)

    def __load_from_ui(self, ui_path_):
        form, base = uic.loadUiType(ui_path_)
        self.ui = form()
        self.ui.setupUi(self)

    def __load_from_py(self, ui_path_):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    def setupUi_buttons(self):
        self.ui.PBchoosedirectory.clicked.connect(self.select_dir)
        self.ui.TableView.clicked.connect(self.display_tags)
        self.ui.PBapply.clicked.connect(self.apply_to_one)
        self.ui.PBapplytoall.clicked.connect(self.apply_to_all)

    def setupUi_shortcuts(self, app):
        self.shortcuts = []
        self.__setshortcut("Ctrl+O", self.select_dir)
        self.__setshortcut("Q", self.select_dir)
        self.__setshortcut("F1", self.__testjoke)
        self.__setshortcut("Esc", app.exit)

    def __setshortcut(self, shortcut_, fuction):
        self.shortcuts.append(QtWidgets.QShortcut(QtGui.QKeySequence(shortcut_), self))
        self.shortcuts[-1].activated.connect(fuction)

    def showpath(self, workdir):
        self.ui.Edit_path.setText(workdir)

    def showdir(self, dirmodel):
        self.ui.TableView.setModel(dirmodel)

    def select_dir(self):
        self.filedialog.exec()
        dir_value = self.filedialog.selectedFiles()
        self.signal_select_dir.emit(str(dir_value[0]))
        self.activateWindow()

    def __getrow(self):
        return self.ui.TableView.selectedIndexes()[0].row()

    def display_tags(self):
        row_ = self.__getrow()
        self.signal_choose_song.emit(row_)

    def get_track_num(self):
        return self.ui.Edit_track.text()

    def get_artist(self):
        return self.ui.Edit_artist.text()

    def get_title(self):
        return self.ui.Edit_title.text()

    def get_album(self):
        return self.ui.Edit_album.text()

    def get_author(self):
        return self.ui.Edit_author.text()

    def get_year(self):
        return self.ui.Edit_year.text()

    def get_genre(self):
        return self.ui.Edit_genre.text()

    def get_comment(self):
        return self.ui.TextEdit_comment.toPlainText()

    def set_track_num(self, text):
        self.ui.Edit_track.setText(text)

    def set_artist(self, text):
        self.ui.Edit_artist.setText(text)

    def set_title(self, text):
        self.ui.Edit_title.setText(text)

    def set_album(self, text):
        self.ui.Edit_album.setText(text)

    def set_author(self, text):
        self.ui.Edit_author.setText(text)

    def set_year(self, text):
        self.ui.Edit_year.setText(text)

    def set_genre(self, text):
        self.ui.Edit_genre.setText(text)

    def set_comment(self, text):
        self.ui.TextEdit_comment.setPlainText(text)

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

    def apply_to_one(self):
        try:
            dict_ = self.__readvalues()
            row_ = self.__getrow()
            # print(dict_)
            # print(row_)
            self.songlist.changetags(row_, dict_)
            self.songlist.save(row_)
            self.showdir(self.workdir)
            self.ui.TableView.selectRow(row_)
        except:
            pass

    def apply_to_all(self):
        try:
            dict_ = self.__readvalues()
            # print(dict_)
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
    mainwin = UiView(app)   # uic.loadUi("pirate.ui")
   # loadicons(mainwin, app)
    mainwin.setupUi_buttons()
    mainwin.setupUi_shortcuts()
    mainwin.show()
    sys.exit(app.exec_())