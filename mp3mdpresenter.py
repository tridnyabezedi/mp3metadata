from gui_loader import UiView
from mp3idmaker import SongList
from PyQt5 import QtGui
import ini

class Presenter:
    def __init__(self, app):
        self.view = UiView(app)
        self.view.show()
        self.connect_signals()
        # self.view.presenter = self
        self.workdir = ini.folder[8] # os.getcwd()
        self.refresh_view()

    def connect_signals(self):
        self.view.signal_select_dir.connect(self.select_dir)
        self.view.signal_choose_song.connect(self.display_tags)
        self.view.signal_apply_to_one.connect(self.apply_to_one)
        self.view.signal_apply_to_all.connect(self.apply_to_all)

    def refresh_view(self):
        self.songlist = SongList(self.workdir)
        self.show_path()
        self.show_dir()

    def show_path(self):
        self.view.showpath(str(self.workdir).replace(r'/', '\\'))

    def show_dir(self):
        dirmodel = self.get_dir_model()
        self.view.showdir(dirmodel)

    def get_dir_model(self):
        def createtable():
            table = [[song.filename] +
                     [song[word] for word in ini.tablegraphs[0]]
                     for song in self.songlist]
            return table
        dirmodel = QtGui.QStandardItemModel()
        dirlist = createtable()
        dirlist = [[QtGui.QStandardItem(x) for x in list_] for list_ in dirlist]
        for list_ in dirlist:
            dirmodel.appendRow(list_)
        dirmodel.setHorizontalHeaderLabels(list(ini.tablegraphs[1]))
        return dirmodel

    def select_dir(self, path_to_folder):
        if path_to_folder != self.workdir:
            self.workdir = path_to_folder
            self.refresh_view()

    def display_tags(self, row_):
        song = self.songlist[row_]
        self.view.set_track_num(song['tracknum'])
        self.view.set_album(song['album'])
        self.view.set_artist(song['artist'])
        self.view.set_comment(song['comment'])
        self.view.set_author(song['author'])
        self.view.set_year(song['year'])
        self.view.set_genre(song['genre'])
        self.view.set_title(song['title'])

    def apply_to_one(self, row_):
        try:
            dict_ = self.__readvalues()
            self.songlist.song(row_).change_tags(dict_)
            self.songlist.song(row_).save_changes()
            self.refresh_view()
        except:
            pass

    def apply_to_all(self):
        try:
            dict_ = self.__readvalues()
            self.songlist.change_tags_for_all(dict_)
            self.refresh_view()
        except:
            pass

    def __readvalues(self):
        dict_ = {}
        dict_['tracknum'] = self.view.get_track_num()
        dict_['artist'] = self.view.get_artist()
        dict_['title'] = self.view.get_title()
        dict_['album'] = self.view.get_album()
        dict_['author'] = self.view.get_author()
        dict_['year'] = self.view.get_year()
        dict_['genre'] = self.view.get_genre()
        dict_['comment'] = self.view.get_comment()
        for word_ in dict_:
            if dict_[word_].startswith(r"/re/:"):
                dict_[word_] = (dict_[word_][5:], True)
            else:
                dict_[word_] = (dict_[word_], False)
        return dict_




