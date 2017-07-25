from gui_loader import UiView
from mp3idmaker import SongList
import os
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
        dirmodel = QtGui.QStandardItemModel()
        dirlist = self.songlist.createtable()
        dirlist = [[QtGui.QStandardItem(x) for x in list_] for list_ in dirlist]
        for list_ in dirlist:
            dirmodel.appendRow(list_)
        dirmodel.setHorizontalHeaderLabels(['Filename'] + list(self.songlist.tablegraphs))
        return dirmodel

    def connect_signals(self):
        self.view.signal_select_dir.connect(self.select_dir)
        self.view.signal_choose_song.connect(self.display_tags)
        self.view.signal_apply_to_one.connect(self.apply_to_one)
        self.view.signal_apply_to_all.connect(self.apply_to_all)

    def select_dir(self, path_to_folder):
        if path_to_folder != self.workdir:
            self.workdir = path_to_folder
            self.refresh_view()

    def display_tags(self, row_):
        val = self.songlist.list_[row_][1][self.songlist.vocabulary['tracknum'][0]]
        self.view.set_track_num(str(val))
        self.view.set_album('dddddddd')
        self.view.set_artist('ddddddd')
        self.view.set_comment('dfdfdfdgfzzzsdjf ksjsik jkd sksdjkgsj  sj gklsjg sgls ks   s'
                              'sdjg kjsk sj sgj slkglwjijujgjg]q[m z?Sknzskgjnrvji'
                              ' kfjdfndkgmgifmgdfmgfkk ljjf j ghjt kqp[ l lf mf')
        self.view.set_author('beeeth')
        self.view.set_year('errrrer')
        self.view.set_genre('muuuu')
        self.view.set_title('juuuu')

    def apply_to_one(self):
        pass

    def apply_to_all(self):
        pass





